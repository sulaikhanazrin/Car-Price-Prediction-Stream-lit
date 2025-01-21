import streamlit as st
import pandas as pd
import pickle

# Define the correct path to your model file
import os

# Define the model file path dynamically
model_file_path = os.path.join(os.getcwd(), "model", "gradient_boosting_regressor_model.pkl")

# Try to load the model
try:
    with open(model_file_path, 'rb') as model_file:
        model = pickle.load(model_file)
    st.write("Model loaded successfully.")
except FileNotFoundError:
    st.error(f"Error: The file at '{model_file_path}' was not found.")
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")

# If the model is loaded successfully, proceed with the app
if 'model' in globals():
    st.title("Car Price Prediction")

    # Your input fields and logic go here (same as your previous code)
    car_name = st.selectbox("Car Name", ['Audi A4', 'Audi A6', 'Audi A8', 'Audi Q7', 'BMW 3', 'BMW 5', 'BMW 6', 'BMW 7', 'BMW X1'])
    vehicle_age = st.slider("Vehicle Age (in years)", 0, 29, 5)
    km_driven = st.number_input("Kilometers Driven", min_value=581, max_value=1325000, step=1)
    mileage = st.number_input("Mileage (km/l)", min_value=4.0, max_value=33.54, value=15.0)
    engine = st.number_input("Engine (in cc)", min_value=793, max_value=6592, value=1500)
    max_power = st.number_input("Max Power (in bhp)", min_value=38.4, max_value=626.0, value=100.0)
    seller_type = st.selectbox("Seller Type", ['Dealer', 'Individual', 'Trustmark Dealer'])
    fuel_type = st.selectbox("Fuel Type", ['CNG', 'Diesel', 'Electric', 'LPG', 'Petrol'])
    transmission_type = st.selectbox("Transmission Type", ['Automatic', 'Manual'])
    seats = st.selectbox("Seats", [2, 4, 5, 6, 7, 8, 9])

    # Prepare the input data for prediction
    input_data = pd.DataFrame({
        'car_name': [car_name],
        'vehicle_age': [vehicle_age],
        'km_driven': [km_driven],
        'mileage': [mileage],
        'engine': [engine],
        'max_power': [max_power],
        'seller_type': [seller_type],
        'fuel_type': [fuel_type],
        'transmission_type': [transmission_type],
        'seats': [seats]
    })

    # Predict the price if button is pressed
    if st.button("Predict Price"):
        if 'model' in globals():
            prediction = model.predict(input_data)
            st.write(f"Predicted Price: ₹{prediction[0]:,.2f}")
        else:
            st.error("Model is not loaded. Please try again.")
else:
    st.error("Model could not be loaded.")
