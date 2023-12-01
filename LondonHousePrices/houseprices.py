import pickle
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np

# Load the Random Forest model
with open('rfmodel2.sav', 'rb') as model_file:
    model = pickle.load(model_file)

df = pd.read_csv('completelondon.csv')

# Create a function for prediction
def housing_prediction(input):
    input_array = np.asarray(input)
    input_reshape = input_array.reshape(1, -1)
    prediction = model.predict(input_reshape)
    return prediction[0]  # Return the prediction value

# Main function
def main():
    st.set_page_config(page_title="London Housing Predictor", layout='wide')

    # Set main title
    st.title('London Housing Predictor using Random Forest Regressor')

    # Add image
    image = Image.open('london1.jpeg')
    st.image(image, use_column_width=True)

    # Set sub title
    st.write('Enter your data to get your London Pricing evaluation')

    # Specify the input variables from the user
    year = st.number_input('What year are you thinking of buying the property:', min_value=1999, step=1)
    mean_salary = st.number_input('What is your annual average salary:', min_value=0, step=1)
    median_salary = st.number_input('Please enter your mid annual salary :', min_value=0, step=1)
    area = st.number_input('What is your Borough of choice? Please enter the borough encrypted number, choose from the table below:', min_value=0, step=1)



    image = Image.open('areacodes.png')
    st.image(image, width=400)

    # Code for prediction
    predict = ''  

    # Button for prediction
    if st.button('Predict'):
        prediction_value = housing_prediction([year, mean_salary, median_salary, area])
        predict = prediction_value

    # Show the prediction result
    if predict:
        st.success(f'Predicted Housing Price: £{predict:,.2f}')

if __name__ == '__main__':
    main()
