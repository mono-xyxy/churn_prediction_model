import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Ecommerce Analytics Dashboard",
    layout="wide"
)

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("../data/cleaned/cleaned_orders.csv")

# Convert timestamp
df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])

# Create order month
df["order_month"] = df["order_purchase_timestamp"].dt.to_period("M").astype(str)

# Revenue fallback
if "revenue_per_order" not in df.columns:
    df["revenue_per_order"] = df["price"] + df["freight_value"]

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.title("Filters")

date_range = st.sidebar.date_input(
    "Select Date Range",
    [df["order_purchase_timestamp"].min(), df["order_purchase_timestamp"].max()]
)

if len(date_range) == 2:
    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])
else:
    start_date = pd.to_datetime(date_range[0])
    end_date = start_date

df_filtered = df[
    (df["order_purchase_timestamp"] >= start_date) &
    (df["order_purchase_timestamp"] <= end_date)
]

# Category Filter (safe)
if "product_category_name" in df.columns:
    categories = df["product_category_name"].dropna().unique()
    selected_cat = st.sidebar.selectbox("Category", ["All"] + list(categories))

    if selected_cat != "All":
        df_filtered = df_filtered[df_filtered["product_category_name"] == selected_cat]

# -----------------------------
# Dashboard Title
# -----------------------------
st.title("Ecommerce Business Intelligence Dashboard")

# -----------------------------
# KPI Metrics
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${df_filtered['revenue_per_order'].sum():,.0f}")

col2.metric("Total Orders", df_filtered["order_id"].nunique())

col3.metric("Average Order Value",
            f"${df_filtered['revenue_per_order'].mean():,.2f}")

# -----------------------------
# Revenue Overview
# -----------------------------
st.header("Revenue Overview")

monthly_rev = df_filtered.groupby("order_month")["revenue_per_order"].sum().reset_index()

fig1 = px.line(
    monthly_rev,
    x="order_month",
    y="revenue_per_order",
    markers=True,
    title="Monthly Revenue Trend"
)

st.plotly_chart(fig1, use_container_width=True)

# Revenue by State
if "customer_state" in df.columns:
    state_rev = df_filtered.groupby("customer_state")["revenue_per_order"].sum().reset_index()

    fig2 = px.bar(
        state_rev.sort_values("revenue_per_order", ascending=False),
        x="customer_state",
        y="revenue_per_order",
        title="Revenue by State"
    )

    st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# Product Intelligence
# -----------------------------
st.header("Product Intelligence")

if "product_category_name" in df.columns:

    category_rev = df_filtered.groupby("product_category_name")["revenue_per_order"].sum().reset_index()

    fig3 = px.treemap(
        category_rev,
        path=["product_category_name"],
        values="revenue_per_order",
        title="Category Revenue Distribution"
    )

    st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# Review Analytics
# -----------------------------
st.header("Customer Reviews")

if "review_score" in df.columns:

    fig4 = px.histogram(
        df_filtered,
        x="review_score",
        nbins=5,
        title="Review Score Distribution"
    )

    st.plotly_chart(fig4, use_container_width=True)

# -----------------------------
# Key Insights Panel
# -----------------------------
st.header("Key Insights")

st.markdown("""
**1️⃣ Revenue Growth**  
Monthly revenue trend shows steady growth across most months.

**2️⃣ Top Performing States**  
Certain states consistently generate higher order volumes and revenue.

**3️⃣ Product Categories**  
A few product categories contribute the majority of ecommerce revenue.
""")