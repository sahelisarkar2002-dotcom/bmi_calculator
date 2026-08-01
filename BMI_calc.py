import google.genai as genai
import streamlit as st


GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=GOOGLE_API_KEY)

st.title("BMI Calculator with AI Nutritionist")
wt = st.number_input("Enter your weight in kilograms: ")
ht = st.number_input("Enter your height in meters: ")

bmi = wt / (ht ** 2)
st.write(f"Your BMI is: {bmi:.2f}")

prompt = f"Act like an expert Nutritionist, comment on the BMI with the following data: height as {ht}, weight as {wt}, BMI as {bmi}"

if st.button('Analyze your BMI with AI:'):
    st.write("Analyzing your BMI with AI...")
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )
    st.write(response.text)