#Briyani App
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load the trained model
with open('jeeva.pkl', 'rb') as file: model = pickle.load(file)

#Creating custom background 

page_bg_img = """
<style>
[data-testid='stAppViewContainer'] {
background-image: url("https://img.onmanorama.com/content/dam/mm/en/food/features/images/2021/2/3/biryani.jpg.transform/845x440/image.jpg");
opacity: 0.8;
background-size: cover;
}
[data-testid="stHeader"] {
background-color: rgba(0,0,0,0);
}
[data-testid="stSidebarContent"] {
background-color: rgba(0,0,0,0);
}
</style>
"""

# Create the Streamlit app
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Biryani Price Predictor")

# Input fields for features
chicken_price = st.number_input("**Enter your Chicken Price(Per Kg Briyani)** ", min_value=0)
rice_price = st.number_input("**Enter your Rice Price(Per Kg Briyani)** ", min_value=0)
spice_price = st.number_input("**Enter the Spice Price(Per Kg Briyani)** ", min_value=0)
vegetable_price = st.number_input("**Enter the Vegetable Price(Per Kg Briyani)** ", min_value=0)
chef_experience = st.number_input("**Chef Experience (Years of Experience)** ", min_value=0)


# Predict button
if st.button("Predict"):
  input_data = [[chicken_price, rice_price, spice_price, vegetable_price, chef_experience]]
  prediction = model.predict(input_data)[0]
  st.header(f"Predicted Biryani Price: Rs.{prediction:.2f}")
  st.snow()

# Feedback Section
with st.sidebar :
  st.image('Briyani_logo.png',width = 350)
  st.header('Thanks for Spicing your price with Us!!')
  st.write('Rate us from the count of 1 to 5 based on your experience with Briyani Price Prediction.')
  ratings = ['1','2','3','4','5']
  selected = st.feedback("stars")
  if st.button('Rate Us'):
      st.balloons()
      st.write(f'Thanks for your valuable feedback! You have rated us {selected+1} out of 5.')
  st.markdown('**Want to share your thoughts? Share it with us :**')
  user_feedback = st.text_area('')
  if st.button('Submit your Respose here'): 
      st.write("Thanks for your Feedback! It will help us Improve our Services!")
      st.balloons()
