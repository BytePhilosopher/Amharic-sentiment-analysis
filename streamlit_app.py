# streamlit_app.py

import streamlit as st
import pickle
import numpy as np

# --------------------------
# Load Model and Vectorizer
# --------------------------
@st.cache_resource
def load_model_and_vectorizer():
    with open("models/logistic_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("models/tfidf_vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

model, vectorizer = load_model_and_vectorizer()

# --------------------------
# Page Config and Styling
# --------------------------
st.set_page_config(page_title="QalAnalyzer | ቃል Analyzer", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .stTextArea textarea {
            font-size: 18px;
            font-family: "Noto Sans Ethiopic", sans-serif;
        }
        .stButton button {
            background-color: #1a73e0;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
        }
    </style>
""", unsafe_allow_html=True)

# --------------------------
# App Title and Intro
# --------------------------
st.markdown("<h1 style='text-align: center; color: #1a73e0;'>🌍 QalAnalyzer | ቃል Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #fff;'>🔍 Amharic Sentiment Classification using Machine Learning</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Paste or type an Amharic sentence below to detect its sentiment!</p>", unsafe_allow_html=True)

# --------------------------
# Input Box
# --------------------------
amharic_input = st.text_area("✍️ **Enter Amharic text here:**", height=150)

# --------------------------
# Predict Button and Result
# --------------------------
if st.button("🔎 Analyze Sentiment"):
    if amharic_input.strip() == "":
        st.warning("⚠️ Please enter some Amharic text to analyze.")
    else:
        with st.spinner("Analyzing sentiment..."):
            transformed_text = vectorizer.transform([amharic_input])
            prediction = model.predict(transformed_text)[0]

        st.markdown("---")
        st.markdown(f"<h2 style='text-align: center;'>🧠 Predicted Sentiment: <span style='color: #0b8043;'>`{prediction.upper()}`</span></h2>", unsafe_allow_html=True)

        if prediction == "1":
            st.success("🎉 That sounds uplifting!")
        elif prediction == "0":
            st.error("😟 That doesn't sound great.")

