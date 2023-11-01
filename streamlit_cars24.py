import streamlit as st
import datetime
import pickle
import pandas as pd

cars_df = pd.read_csv("cars24-car-price.csv")

st.write("# Cars24 Used Car price prediction")
st.info("NOTE: No EDA has been done except encoding.")
st.dataframe(cars_df.head())

encode_dict = {
  "fuel_type": {'Diesel': 5,'Petrol': 4,'CNG': 3,'LPG': 2,'Electric': 1},
  "seller_type": {'Dealer': 1, 'Individual': 2, 'Trustmark Dealer': 3},
  "transmission_type": {"Manual": 2, "Automatic": 1}
}



def model_pred(fuel_type, transmission_type, engine, seats):
    ## loading the model
    with open("linear_regression_model.pkl", 'rb') as file:
        reg_model = pickle.load(file)

    input_features = [[2018.0, 20000, 9.7, engine, 86.30, seats, 2, fuel_type, transmission_type]]
    return reg_model.predict(input_features)


# fuel_type = "Diesel"
# transmission_type = "Manual"
# engine = 600
# seats = 4
# fuel_type = encode_dict['fuel_type'][fuel_type]
# transmission_type = encode_dict['transmission_type'][transmission_type]
# price = model_pred(fuel_type, transmission_type, engine, seats)
# st.text("Predicted Price of the car is: " + str(price) + "Lakhs")


col1, col2 = st.columns(2)

fuel_type = col1.selectbox("Select the fuel type",
                            ["Diesel", "Petrol", "CNG", "LPG", "Electric"])
# we could also do df["fuel_type"].unique.tolist()
engine = col1.slider("Set the Engine Power",
                      500, 5000, step=100)
# here i could take the min and max values.
transmission_type = col2.selectbox("Select the transmission type",
                                    ["Manual", "Automatic"])
seats = col2.selectbox("Enter the number of seats",
                        [4,5,7,9,11])

if (st.button("Predict Price")):
    fuel_type = encode_dict['fuel_type'][fuel_type]
    transmission_type = encode_dict['transmission_type'][transmission_type]
    price = model_pred(fuel_type, transmission_type, engine, seats)
    st.text("Predicted Price of the car is: "+ str(price) + "Lakhs")