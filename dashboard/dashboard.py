# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(style="dark")

# Customer Functions
def customer_city(all_df):
    customer_city = all_df[all_df["order_id"].isna() == False].groupby(by = "customer_city").customer_unique_id.nunique().sort_values(ascending = False).reset_index()
    return customer_city
def customer_state(all_df):
    customer_state = all_df[all_df["order_id"].isna() == False].groupby(by = "customer_state").customer_unique_id.nunique().sort_values(ascending = False).reset_index()
    return customer_state
def customer_count_order_sorted(all_df):
    customer_count_order_sorted = all_df.groupby(by = "customer_unique_id").agg(
        count_order = ("order_id", "nunique"), 
        sum_order_value = ("order_value", "sum")
        ).sort_values(by = "count_order", ascending = False).reset_index()
    return customer_count_order_sorted
def customer_sum_order_value_sorted(all_df):
    customer_sum_order_value_sorted = all_df.groupby(by = "customer_unique_id").agg(
        count_order = ("order_id", "nunique"), 
        sum_order_value = ("order_value", "sum")
        ).sort_values(by = "sum_order_value", ascending = False).reset_index()
    return customer_sum_order_value_sorted

# Seller Functions
def seller_city(all_df):
    seller_city = all_df[all_df["order_id"].isna() == False].groupby(by = "seller_city").seller_id.nunique().sort_values(ascending = False).reset_index()
    return seller_city
def seller_state(all_df):
    seller_state = all_df[all_df["order_id"].isna() == False].groupby(by = "seller_state").seller_id.nunique().sort_values(ascending = False).reset_index()
    return seller_state
def seller_count_order_sorted(all_df):
    seller_count_order_sorted = all_df.groupby(by = "seller_id").agg(
        count_order = ("order_id", "nunique"), 
        sum_order_value = ("order_value", "sum")
        ).reset_index().sort_values(by = "count_order", ascending = False)
    return seller_count_order_sorted
def seller_sum_order_value_sorted(all_df):
    seller_sum_order_value_sorted = all_df.groupby(by = "seller_id").agg(
        count_order = ("order_id", "nunique"), 
        sum_order_value = ("order_value", "sum")
        ).reset_index().sort_values(by = "sum_order_value", ascending = False)
    return seller_sum_order_value_sorted

# Product Functions
def product_count_order_sorted(all_df):
    product_count_order_sorted = all_df.groupby(by = "product_id").agg(
        count_order = ("order_id", "nunique"), 
        sum_order_value = ("order_value", "sum")
        ).reset_index().sort_values(by = "count_order", ascending = False)
    return product_count_order_sorted
def product_sum_order_value_sorted(all_df):
    product_sum_order_value_sorted = all_df.groupby(by = "product_id").agg(
        count_order = ("order_id", "nunique"), 
        sum_order_value = ("order_value", "sum")
        ).reset_index().sort_values(by = "sum_order_value", ascending = False)
    return product_sum_order_value_sorted
def product_category_count_order_sorted(all_df):
    product_category_count_order_sorted = all_df.groupby(by = "product_category_name_english").agg(
        count_order = ("order_id", "nunique"), 
        sum_order_value = ("order_value", "sum")
        ).reset_index().sort_values(by = "count_order", ascending = False)
    return product_category_count_order_sorted
def product_category_sum_order_value_sorted(all_df):
    product_category_sum_order_value_sorted = all_df.groupby(by = "product_category_name_english").agg(
        count_order = ("order_id", "nunique"), 
        sum_order_value = ("order_value", "sum")
        ).reset_index().sort_values(by = "sum_order_value", ascending = False)
    return product_category_sum_order_value_sorted

# Plot Functions
def horizontal_barchart(df, n, x, y, title):
    fig, ax = plt.subplots(figsize=(8, 6))
    colors = ["#3187d4", "#b3bcc4", "#b3bcc4", "#b3bcc4", "#b3bcc4", "#b3bcc4", "#b3bcc4", "#b3bcc4", "#b3bcc4", "#b3bcc4"]
    sns.barplot(x = x, y = y, data = df.head(n), palette = colors, ax = ax)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.set_title(title, loc = "center", fontsize = 15)
    for i in range(0, len(ax.containers)):
        ax.bar_label(ax.containers[i], label_type='center')
    st.pyplot(fig)

all_df = pd.read_csv("dashboard/all_dataset.csv")

# Sidebar
with st.sidebar:
    st.sidebar.header("E-Commerce Dashboard")
    genre = st.selectbox(
        label="Analyze by",
        options=("Customer", "Seller", "Product")
    )

# If Sidebar = Customer
if genre == "Customer":
    # Initialize Data
    city = customer_city(all_df)
    state = customer_state(all_df)
    count_order = customer_count_order_sorted(all_df)
    sum_order_value = customer_sum_order_value_sorted(all_df)
    # UI
    st.title("Customer Analysis")
    st.write("This customer analysis will conclude customer state, customer city, customer order count, and customer order value.")
    col1, col2 = st.columns(2)
    with col1:
        st.header("Customer State")
        horizontal_barchart(state, 10, "customer_unique_id", "customer_state", "Distribution of Customers Based on State")
    with col2:
        st.header("Customer City")
        horizontal_barchart(city, 10, "customer_unique_id", "customer_city", "Distribution of Customers Based on City")
    st.header("Customer Order Count")
    horizontal_barchart(count_order, 10, "count_order", "customer_unique_id", "Customers Based on Order Count")
    st.header("Customer Order Value")
    horizontal_barchart(sum_order_value, 10, "sum_order_value", "customer_unique_id", "Customers Based on Order Value")

if genre == "Seller":
    # Initialize Data
    city = seller_city(all_df)
    state = seller_state(all_df)
    count_order = seller_count_order_sorted(all_df)
    sum_order_value = seller_sum_order_value_sorted(all_df)
    # UI
    st.title("Seller Analysis")
    col1, col2 = st.columns(2)
    with col1:
        st.header("Seller State")
        horizontal_barchart(state, 10, "seller_id", "seller_state", "Distribution of Sellers Based on State")
    with col2:
        st.header("Seller City")
        horizontal_barchart(city, 10, "seller_id", "seller_city", "Distribution of Sellers Based on City")
    st.header("Seller Order Count")
    horizontal_barchart(count_order, 10, "count_order", "seller_id", "Sellers Based on Order Count")
    st.header("Seller Order Value")
    horizontal_barchart(sum_order_value, 10, "sum_order_value", "seller_id", "Sellers Based on Order Value")

if genre == "Product":
    # Initialize Data
    count_order = product_count_order_sorted(all_df)
    sum_order_value = product_sum_order_value_sorted(all_df)
    count_order_category = product_category_count_order_sorted(all_df)
    sum_order_value_category = product_category_sum_order_value_sorted(all_df)
    # UI
    st.title("Product Analysis")
    st.header("Product Order Count")
    horizontal_barchart(count_order, 10, "count_order", "product_id", "Products Based on Order Count")
    st.header("Product Order Value")
    horizontal_barchart(sum_order_value, 10, "sum_order_value", "product_id", "Products Based on Order Value")
    st.header("Product Category Order Count")
    horizontal_barchart(count_order_category, 10, "count_order", "product_category_name_english", "Product Categories Based on Order Count")
    st.header("Product Category Order Value")
    horizontal_barchart(sum_order_value_category, 10, "sum_order_value", "product_category_name_english", "Product Categories Based on Order Value")



