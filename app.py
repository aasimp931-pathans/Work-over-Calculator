import streamlit as st

st.set_page_config(page_title="String Air Weight & Depth", layout="centered")

st.title("Workover Calculator 🛢️")

# --- SECTION 1: STRING AIR WEIGHT ---
st.header("1. String Air Weight")
tubular_type = st.selectbox("Tubular Type", ["BHA", "4-1/8\" RH/LH D-COLLAR", "2-7/8\" IF RH/LH DP"])
qty = st.number_input("No of Tubulars", min_value=1, value=3)
length = st.number_input("Length (m)", value=9.19)
ppf = st.number_input("PPF (lb/ft)", value=34.75)

# Calculation: Length(m) * PPF * 1.488 (conversion to kg/m) / 1000 = Metric Tons
weight_tons = (qty * length * ppf * 1.488) / 1000
st.info(f"**Weight in Ton:** {weight_tons:.4f} t")

# --- SECTION 2: BUOYANCY & TOTALS ---
st.header("2. Buoyancy & Drill-O-Meter")
brine_spgr = st.number_input("Brine SpGr", value=1.04)
buoyancy_factor = 1 - (brine_spgr / 7.85) # Standard steel density factor

st.write(f"**Buoyancy Factor:** {buoyancy_factor:.4f}")
travelling_block = st.number_input("Travelling Block (t)", value=2.0)
kelly = st.number_input("Kelly (t)", value=1.0)

# Total Calculation
total_weight = (weight_tons * buoyancy_factor) + travelling_block + kelly
st.success(f"**Weight on Drill-O-Meter:** {total_weight:.4f} t")

# --- SECTION 3: DEPTH ---
st.header("3. Depth Calculation")
tag_depth = st.number_input("Tag Depth (m)", value=3020.00)
tally_length = st.number_input("Tally Length (m)", value=3002.57)

kelly_above_floor = tag_depth - tally_length - 23.56 # Adjust with actual Rig KB/Ground level logic
st.warning(f"**Kelly above Floor:** {kelly_above_floor:.2f} m")
