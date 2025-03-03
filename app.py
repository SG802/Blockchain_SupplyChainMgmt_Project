import streamlit as st
import pandas as pd
from datetime import datetime

# Sample product data (Mirroring the Smart Contract Structure)
products = {
    1: {"name": "T-Shirt", "description": "Comfortable", "weight": 200, "dimensions": 150, "owner": "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4", "status": "Created", "condition": 1, "history": ["0x5B38Da6a701c568545dCfcB03FcB875f56beddC4"], "createdTime": 1738495588, "deliveryTime": 1738495633, "locationHistory": ["Mumbai"]},
    2: {"name": "Trousers", "description": "Denim, Size 32", "weight": 500, "dimensions": 120, "owner": "Manufacturer", "status": "Created", "condition": 1, "history": [], "createdTime": 1738495500, "deliveryTime": None, "locationHistory": []},
    3: {"name": "Jacket", "description": "Leather, Size L", "weight": 800, "dimensions": 160, "owner": "Manufacturer", "status": "Created", "condition": 1, "history": [], "createdTime": 1738495400, "deliveryTime": None, "locationHistory": []}
}

# Streamlit UI Setup
st.title("Blockchain Supply Chain Management")
st.subheader("Clothing Product List")

# Convert product data into a Pandas DataFrame for display
df = pd.DataFrame.from_dict(products, orient='index')
st.dataframe(df)

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
    else:
        st.error("Please enter a valid owner address.")

# Update Product Status
st.subheader("Update Product Status")
status_options = ["Created", "Shipped", "In Transit", "Delivered"]
new_status = st.selectbox("Select New Status", status_options)

if st.button("Update Status"):
    products[product_id]["status"] = new_status
    st.success(f"Status of {products[product_id]['name']} updated to {new_status}")

# Updated Product List After Changes
st.subheader("Updated Clothing Product List")
df_updated = pd.DataFrame.from_dict(products, orient='index')
st.dataframe(df_updated)
