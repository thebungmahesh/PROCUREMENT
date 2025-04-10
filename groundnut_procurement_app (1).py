
import streamlit as st

st.title("🌰 Groundnut Procurement Price Calculator")

# Input: Market Rate Inputs
st.header("1. Enter Market Base Prices (₹/kg)")
price_75_90 = st.number_input("👉 Price for 75-90 Counts per Ounce", min_value=0.0, step=0.1, value=85.0)
price_90_110 = st.number_input("👉 Price for 90-110 Counts per Ounce", min_value=0.0, step=0.1, value=80.0)

# Input: Lot Category
st.header("2. Select Lot Category")
category = st.radio("Choose Kernel Count Category", ["75-90", "90-110"])

# Input: Impurities
st.header("3. Enter Lot Quality Details")
moisture = st.number_input("💧 Moisture Content (kg)", min_value=0.0, step=0.1, value=5.0)
soil_stones = st.number_input("🪨 Soil & Stones (kg)", min_value=0.0, step=0.1, value=3.0)

# Constants
total_lot_weight = 100  # 1 Quintal

# Calculate Net Weight and Adjusted Bid Price
net_weight = total_lot_weight - (moisture + soil_stones)
selected_price = price_75_90 if category == "75-90" else price_90_110
adjusted_bid_price = selected_price * net_weight

# Results
st.header("📊 Calculated Result")
st.write(f"✅ **Net Usable Weight**: {net_weight:.2f} kg")
st.write(f"💰 **Adjusted Procurement Price**: ₹{adjusted_bid_price:.2f} per Quintal based on selected kernel quality.")
