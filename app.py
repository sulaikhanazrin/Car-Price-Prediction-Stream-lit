import streamlit as st
import pandas as pd
import pickle

# Correct path to model file
model_file_path = "model/gradient_boosting_regressor_model.pkl"

# Load model
model = None  # Initialize model variable

try:
    with open(model_file_path, 'rb') as model_file:
        model = pickle.load(model_file)
    st.write("Model loaded successfully.")
except FileNotFoundError:
    st.error(f"Error: The model file at '{model_file_path}' was not found.")
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")

# Proceed only if the model is loaded
if model is not None:
    st.title("Car Price Prediction")

    # Create the input fields for the user
    car_name = st.selectbox("Car Name", ['Audi A4', 'Audi A6', 'Audi A8', 'Audi Q7', 'BMW 3', 'BMW 5', 'BMW 6', 'BMW 7', 'BMW X1', 'BMW X3', 'BMW X4', 'BMW X5', 'BMW Z4', 'Bentley Continental', 'Datsun GO', 'Datsun RediGO', 'Datsun redi-GO', 'Ferrari GTC4Lusso', 'Force Gurkha', 'Ford Aspire', 'Ford Ecosport', 'Ford Endeavour', 'Ford Figo', 'Ford Freestyle', 'Honda Amaze', 'Honda CR', 'Honda CR-V', 'Honda City', 'Honda Civic', 'Honda Jazz', 'Honda WR-V', 'Hyundai Aura', 'Hyundai Creta', 'Hyundai Elantra', 'Hyundai Grand', 'Hyundai Santro', 'Hyundai Tucson', 'Hyundai Venue', 'Hyundai Verna', 'Hyundai i10', 'Hyundai i20', 'ISUZU MUX', 'Isuzu D-Max', 'Jaguar F-PACE', 'Jaguar XE', 'Jaguar XF', 'Jeep Compass', 'Jeep Wrangler', 'Kia Carnival', 'Kia Seltos', 'Land Rover Rover', 'Lexus ES', 'Lexus RX', 'MG Hector', 'Mahindra Alturas', 'Mahindra Bolero', 'Mahindra KUV', 'Mahindra KUV100', 'Mahindra Marazzo', 'Mahindra Scorpio', 'Mahindra Thar', 'Mahindra XUV300', 'Mahindra XUV500', 'Maruti Alto', 'Maruti Baleno', 'Maruti Celerio', 'Maruti Ciaz', 'Maruti Dzire LXI', 'Maruti Dzire VXI', 'Maruti Dzire ZXI', 'Maruti Eeco', 'Maruti Ertiga', 'Maruti Ignis', 'Maruti S-Presso', 'Maruti Swift', 'Maruti Swift Dzire', 'Maruti Vitara', 'Maruti Wagon R', 'Maruti XL6', 'Maserati Ghibli', 'Maserati Quattroporte', 'Mercedes-Benz C-Class', 'Mercedes-Benz CLS', 'Mercedes-Benz E-Class', 'Mercedes-Benz GL-Class', 'Mercedes-Benz GLS', 'Mercedes-Benz S-Class', 'Mini Cooper', 'Nissan Kicks', 'Nissan X-Trail', 'Porsche Cayenne', 'Porsche Macan', 'Porsche Panamera', 'Renault Duster', 'Renault KWID', 'Renault Triber', 'Rolls-Royce Ghost', 'Skoda Octavia', 'Skoda Rapid', 'Skoda Superb', 'Tata Altroz', 'Tata Harrier', 'Tata Hexa', 'Tata Nexon', 'Tata Safari', 'Tata Tiago', 'Tata Tigor', 'Toyota Camry', 'Toyota Fortuner', 'Toyota Glanza', 'Toyota Innova', 'Toyota Yaris', 'Volkswagen Polo', 'Volkswagen Vento', 'Volvo S90', 'Volvo XC', 'Volvo XC60', 'Volvo XC90'],index=None,placeholder="Select the Car...") 

    # Vehicle Age
    vehicle_age = st.slider("Vehicle Age (in years)", 0, 29, 5,)

    # Kilometers Driven
    km_driven = st.number_input("Kilometers Driven", min_value=581, max_value=1325000, value=None,step=1, placeholder="Enter kms driven")

    # Mileage
    mileage = float(st.number_input("Mileage (km/l)", min_value=4.0, max_value=33.54, value=15.0))

    # Engine
    engine = st.number_input("Engine (in cc)", min_value=793, max_value=6592, value=1500)

    # Max Power
    max_power = float(st.number_input("Max Power (in bhp)", min_value=38.4, max_value=626.0, value=100.0))

    # Seller Type
    seller_type = st.selectbox("Seller Type", ['Select an option', 'Dealer', 'Individual', 'Trustmark Dealer'])

    # Fuel Type
    fuel_type = st.selectbox("Fuel Type", ['Select an option', 'CNG', 'Diesel', 'Electric', 'LPG', 'Petrol'])

    # Transmission Type
    transmission_type = st.selectbox("Transmission Type", ['Select an option', 'Automatic', 'Manual'])

    # Seats
    seats = st.selectbox("Seats", [None, 2, 4, 5, 6, 7, 8, 9])  # Added None as an option

    # Validation for Select Boxes
    if seller_type == "Select an option":
        st.warning("Please select a valid Seller Type.")

    if fuel_type == "Select an option":
        st.warning("Please select a valid Fuel Type.")

    if transmission_type == "Select an option":
        st.warning("Please select a valid Transmission Type.")

    if seats is None:
        st.warning("Please select a valid number of Seats.")

    # Proceed only if all inputs are valid
    if (
        seller_type != "Select an option"
        and fuel_type != "Select an option"
        and transmission_type != "Select an option"
        and seats is not None
    ):
        st.success("All inputs are valid!")

    # Create a DataFrame from the user input
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

    # Predict the price using the pipeline
    if st.button("Predict Price"):
        prediction = model.predict(input_data)
        st.write(f"Predicted Price: ₹{prediction[0]:,.2f}")
