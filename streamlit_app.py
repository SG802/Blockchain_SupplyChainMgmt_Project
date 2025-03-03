import streamlit as st
import pandas as pd
from datetime import datetime

# Sample product data (Mirroring the Smart Contract Structure)
products = {
    1: {"name": "Laptop", "price": 1000, "owner": "Manufacturer", "status": "Created"},
    2: {"name": "Phone", "price": 700, "owner": "Manufacturer", "status": "Created"},
    3: {"name": "Tablet", "price": 500, "owner": "Manufacturer", "status": "Created"}
}

# Streamlit UI Setup
st.title("Blockchain Supply Chain Management")
st.subheader("Product List")

# Convert product data into a Pandas DataFrame for display
df = pd.DataFrame.from_dict(products, orient='index')
st.dataframe(df)

# Ownership Transfer Section
st.subheader("Transfer Product Ownership")
product_id = st.selectbox("Select Product ID", list(products.keys()))
new_owner = st.text_input("Enter New Owner Address")

if st.button("Transfer Ownership"):
    if new_owner:
        products[product_id]["owner"] = new_owner
        products[product_id]["status"] = "Ownership Transferred"
        st.success(f"Ownership of {products[product_id]['name']} transferred to {new_owner}")
    else:
        st.error("Please enter a valid owner address.")

# Updated Product List After Transfer
st.subheader("Updated Product List")
df_updated = pd.DataFrame.from_dict(products, orient='index')
st.dataframe(df_updated)
