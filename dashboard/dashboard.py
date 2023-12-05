import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')


sum_order_items_df = pd.read_csv("data/Products.csv")
total_transaction_per_customer = pd.read_csv("data/Transactions.csv")
customer_counts = pd.read_csv("data/Customers.csv")

st.header('E-Commerces Dashboard')

st.subheader("Best & Worst Performing Product")
 
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(25, 10))
 
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
 
sns.barplot(x="total", y="product name", data=sum_order_items_df.head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Best Performing Product", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=30)
ax[0].tick_params(axis='x', labelsize=30)
 
sns.barplot(x="total", y="product name", data=sum_order_items_df.sort_values(by="total", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Worst Performing Product", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=30)
ax[1].tick_params(axis='x', labelsize=30)
 
st.pyplot(fig)

st.subheader("Total Transactions in Several Years")
 
plt.figure(figsize=(10, 5))
plt.plot(total_transaction_per_customer["order_purchase_year"], total_transaction_per_customer["payment_value"], marker='o', linewidth=2, color="#72BCD4")
plt.title("Total Transaction 2016-2018", loc="center", fontsize=20)
plt.xticks([2016, 2017, 2018], fontsize=10)
plt.yticks(fontsize=10)
st.pyplot(plt)

st.subheader("Total Customers by City")
 
plt.figure(figsize=(10, 5))

sns.barplot(
    y="total",
    x="City",
    data=customer_counts.head(3),
    palette=colors
)
plt.title("Top 3 total of Customer by City", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
 
st.pyplot(plt)
 
st.caption('Copyright (c) Daniel Alvaro 2023')













