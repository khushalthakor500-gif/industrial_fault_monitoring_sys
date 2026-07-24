import json
import streamlit as st
import pandas as pd
import plotly.express as px
import random
from streamlit_autorefresh import st_autorefresh
from datetime import datetime

# ---------------- PAGE ----------------
st.set_page_config(
    page_title="Industrial Fault Monitoring System",
    page_icon="🏭",
    layout="wide"
)
st_autorefresh(interval=1000, key="refresh")
# ---------------- TITLE ----------------
st.title("🏭 Industrial Fault Monitoring System")
st.caption("Real-Time Predictive Monitoring Dashboard")
st.divider()

# ---------------- SIDEBAR ----------------
st.sidebar.title("🏭 Machine Information")

st.sidebar.markdown("### System")
st.sidebar.write("**Machine ID:** IND-001")
st.sidebar.write("**Controller:** Arduino UNO")
st.sidebar.write("**Location:** Laboratory")

st.sidebar.markdown("---")

st.sidebar.markdown("### Sensors")

st.sidebar.success("🌡 DHT11 (Temp & Humidity)")
st.sidebar.success("⚡ ACS712 Current")
st.sidebar.success("📳 SW420 Vibration")
st.sidebar.success("🌫 MQ-2 Gas Sensor")

st.sidebar.markdown("---")

st.sidebar.markdown("---")

st.sidebar.header("📊 Dashboard")

st.sidebar.write("**Version:** 3.0")
st.sidebar.write("**Mode:** Real-Time Monitoring")
st.sidebar.write("**Refresh Rate:** 1 sec")

st.sidebar.markdown("---")

st.sidebar.header("📁 Project")

st.sidebar.write("**Project:** Industrial Fault Monitoring System")
st.sidebar.write("**Course:** Design Engineering-II")
st.sidebar.write("**Developer:** Khushal Parmar")


# ---------------- TIME ----------------
current_time = datetime.now().strftime("%d-%m-%Y  %H:%M:%S")
st.write("**Current Time:**", current_time)

st.markdown("---")
# ---------------- THRESHOLD SETTINGS ----------------

st.sidebar.markdown("---")
st.sidebar.header("⚙ Threshold Settings")  

temp_threshold = st.sidebar.slider(
    "🌡 Temperature Threshold (°C)",
    20,
    80,
    40
)

current_threshold = st.sidebar.slider(
    "⚡ Current Threshold (A)",
    0.10,
    2.00,
    0.40,
    0.01
)

gas_threshold = st.sidebar.slider(
    "🌫 Gas Threshold",
    100,
    600,
    180
)
# ---------------- SAMPLE VALUES ----------------
temperature = 0
humidity = 0
current = 0
gas = 0
vibration = "Normal"
motor = "Running"

try:
    with open("sensor_data.json", "r") as f:
        sensor = json.load(f)

    temperature = sensor["temperature"]
    current = sensor["current"]
    gas = sensor["gas"]

    if sensor["vibration"] == 1:
        vibration = "Fault"
    else:
        vibration = "Normal"

except Exception as e:
    st.error(f"Data Error: {e}")
    
fault_count = 0

fault_count = 0

if temperature > temp_threshold:
    fault_count += 1

if current > current_threshold:
    fault_count += 1

if gas > gas_threshold:
    fault_count += 1

if vibration == "Fault":
    fault_count += 1 

st.info(f"🚨 Active Faults : {fault_count}")
# ---------------- STATUS ----------------
# ---------------- STATUS ----------------

status_col1, status_col2, status_col3 = st.columns(3)
fault = (
    temperature > temp_threshold or
    current > current_threshold or
    gas > gas_threshold or
    vibration == "Fault"
)
with status_col1:
    if fault:
        st.error("🔴 SYSTEM : FAULT")
    else:
        st.success("🟢 SYSTEM : HEALTHY")

with status_col2:
    st.info(f"🕒 {current_time}")

with status_col3:
    st.success("🔌 Arduino : Connected")

# ---------------- CARDS ----------------
col1,col2,col3=st.columns(3)
col4,col5,col6=st.columns(3)
col1.metric("🌡 Temperature", f"{temperature} °C")
col2.metric("💧 Humidity", f"{humidity} %")
col3.metric("⚡ Current", f"{current} A")

col4.metric("🌫 Gas", gas)
col5.metric("📳 Vibration", vibration)
col6.metric("⚙ Motor", motor)

st.markdown("---")

st.subheader("🚨 Active Alarm Panel")

if temperature > temp_threshold:
    st.error("🌡 Temperature : HIGH")
else:
    st.success("🌡 Temperature : NORMAL")

if current > current_threshold:
    st.warning("⚡ Current : HIGH")
else:
    st.success("⚡ Current : NORMAL")

if gas > gas_threshold:
    st.error("🌫 Gas : GAS DETECTED")
else:
    st.success("🌫 Gas : SAFE")

if vibration == "Fault":
    st.error("📳 Vibration : FAULT")
else:
    st.success("📳 Vibration : NORMAL")

if motor == "Running":
    st.success("⚙ Motor : RUNNING")
else:
    st.warning("⚙ Motor : STOPPED")

# ---------------- GRAPH DATA ----------------
temp_data=pd.DataFrame({
    "Reading":list(range(1,11)),
    "Temperature":[30,31,30,32,31,33,32,31,34,temperature]
})

current_data=pd.DataFrame({
    "Reading":list(range(1,11)),
    "Current":[0.18,0.20,0.17,0.19,0.21,0.20,0.22,0.21,0.19,current]
})

# ---------------- GRAPHS ----------------
left,right=st.columns(2)

with left:
    fig=px.line(
        temp_data,
        x="Reading",
        y="Temperature",
        title="Temperature Trend"
    )
    st.plotly_chart(fig, width="stretch")

with right:
    fig2=px.line(
        current_data,
        x="Reading",
        y="Current",
        title="Current Trend"
    )
    st.plotly_chart(fig2, width="stretch")

st.markdown("---")

# ---------------- HISTORY ----------------
st.subheader("Recent Fault History")
history = pd.DataFrame({
    "Time": ["21:35", "21:41", "21:45", "21:48"],
    "Fault": [
        "Gas Level High",
        "Gas Normal",
        "Vibration Detected",
        "System Healthy"
    ]
})

st.table(history)
