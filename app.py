import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("house_price_model.pkl")

st.title("House Price Prediction App")

overall_qual = st.slider("Overall Quality", 1, 10, 5)
gr_liv_area = st.number_input("Above Ground Living Area", min_value=0)
total_bsmt_sf = st.number_input("Total Basement Area", min_value=0)
age = st.number_input("House Age", min_value=0)
lot_area = st.number_input("Lot Area", min_value=0)
garage_area = st.number_input("Garage Area", min_value=0)
garage_cars = st.slider("Garage Cars", 0, 5, 1)
tot_rooms = st.slider("Total Rooms Above Ground", 1, 15, 6)
full_bath = st.slider("Full Bathrooms", 0, 5, 1)

lot_area_log = np.log(lot_area) if lot_area > 0 else 0

features = [
    "OverallQual",
    "GrLivArea",
    "TotalBsmtSF",
    "Age",
    "LotArea_log",
    "GarageArea",
    "GarageCars",
    "TotRmsAbvGrd",
    "FullBath"
]

input_data = pd.DataFrame([{
    "OverallQual": overall_qual,
    "GrLivArea": gr_liv_area,
    "TotalBsmtSF": total_bsmt_sf,
    "Age": age,
    "LotArea_log": lot_area_log,
    "GarageArea": garage_area,
    "GarageCars": garage_cars,
    "TotRmsAbvGrd": tot_rooms,
    "FullBath": full_bath
}])

input_data = input_data[features]

if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted House Price: ${prediction:,.0f}")
