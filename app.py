from streamlit.runtime.scriptrunner import RerunException
import streamlit as st
import pandas as pd
from datetime import datetime
import random

# Function to generate random Ethereum-like addresses
def generate_eth_address():
    return "0x" + "".join(random.choices("0123456789abcdef", k=40))

# Sample product data (Mirroring the Smart Contract Structure)
products = {
    1: {"name": "T-Shirt", "description": "Comfortable", "weight": 200, "dimensions": 150, "owner": generate_eth_address(), "status": "Created", "condition": 1, "history": [generate_eth_address()], "createdTime": 1738495588, "deliveryTime": 1738495633, "locationHistory": ["Mumbai"]},
    2: {"name": "Trousers", "description": "Denim, Size 32", "weight": 500, "dimensions": 120, "owner": generate_eth_address(), "status": "Created", "condition": 1, "history": [generate_eth_address()], "createdTime": 1738495500, "deliveryTime": None, "locationHistory": []},
    3: {"name": "Jacket", "description": "Leather, Size L", "weight": 800, "dimensions": 160, "owner": generate_eth_address(), "status": "Created", "condition": 1, "history": [generate_eth_address()], "createdTime": 1738495400, "deliveryTime": None, "locationHistory": []}
}

# Function to convert Unix timestamp to readable date
def format_timestamp(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S') if timestamp else "Not Delivered Yet"

# Streamlit UI Setup
st.title("Blockchain Supply Chain Management Demo")
st.subheader("Clothing Product List")

# Convert product data into a Pandas DataFrame for display
def get_dataframe():
    temp_products = {pid: product.copy() for pid, product in products.items()}
    for product in temp_products.values():
        product["createdTime"] = format_timestamp(product["createdTime"])
        product["deliveryTime"] = format_timestamp(product["deliveryTime"])
    return pd.DataFrame.from_dict(temp_products, orient='index')

st.dataframe(get_dataframe())

# Ownership Transfer Section
st.subheader("Transfer Clothing Product Ownership")
product_id = st.selectbox("Select Product ID", list(products.keys()))
new_owner = st.text_input("Enter New Owner Address")

if st.button("Transfer Ownership"):
    if new_owner:
        products[product_id]["history"].append(products[product_id]["owner"])
        products[product_id]["owner"] = new_owner
        products[product_id]["status"] = "Ownership Transferred"
        st.success(f"Ownership of {products[product_id]['name']} transferred to {new_owner}")
        try:
            st.rerun()
        except RerunException:
            pass
    else:
        st.error("Please enter a valid owner address.")

# Update Product Status
st.subheader("Update Product Status")
status_options = ["Created", "Shipped", "In Transit", "Delivered"]
new_status = st.selectbox("Select New Status", status_options)

if st.button("Update Status"):
    products[product_id]["status"] = new_status
    if new_status == "Delivered":
        products[product_id]["deliveryTime"] = int(datetime.utcnow().timestamp())
    st.success(f"Status of {products[product_id]['name']} updated to {new_status}")
    try:
        st.rerun()
    except RerunException:
        pass

# Updated Product List After Changes
st.subheader("Updated Clothing Product List")
updated_products = {pid: product.copy() for pid, product in products.items() if product["status"] != "Created" or len(product["history"]) > 1}
for product in updated_products.values():
    product["createdTime"] = format_timestamp(product["createdTime"])
    product["deliveryTime"] = format_timestamp(product["deliveryTime"])

st.dataframe(pd.DataFrame.from_dict(updated_products, orient='index'))
