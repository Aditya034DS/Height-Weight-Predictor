# 📦 STEP 1: Import Required Libraries
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# ========================================
# 📦 STEP 2: Load Data & Train Model Inline (Temporary)
# NOTE: In a real app you'd load a trained model with joblib
# ========================================
df = pd.read_excel("dataset.xlsx")
X = df[['Weight']]
y = df['Height']

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train a simple linear regression model
model = LinearRegression()
model.fit(X_scaled, y)

# ========================================
# 🖥️ STEP 3: Streamlit App UI
# ========================================
st.title("📏 Height Predictor from Weight")
st.write("This app predicts your height (in cm) based on your weight (in kg) using a simple Linear Regression model.")

# User input for weight
weight = st.number_input("Enter your weight (kg):", min_value=30, max_value=150, value=70)

# Predict when button is clicked
if st.button("Predict Height"):
    scaled_input = scaler.transform([[weight]])
    predicted_height = model.predict(scaled_input)[0]
    st.success(f"📐 Predicted Height: {predicted_height:.2f} cm")

# Optional: Show the formula
st.markdown("---")
st.subheader("📈 Model Equation")
st.write(f"Height = {model.intercept_:.2f} + {model.coef_[0]:.2f} × standardized weight")

# Optional: Show data
with st.expander("📊 See Sample Dataset"):
    st.dataframe(df.head())
