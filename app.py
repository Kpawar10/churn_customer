import streamlit as st
import pandas as pd
import pickle

# -------------------------------
# Load Model
# -------------------------------
model = pickle.load(open('models/churn_model.pkl', 'rb'))

# -------------------------------
# App Title
# -------------------------------
st.title("📊 Customer Churn Prediction")
st.write("Enter customer details to predict churn risk")

#sidebar
st.sidebar.title("About")
st.sidebar.info("""
This app predicts customer churn using Machine Learning.

Built with:
- Scikit-learn
- Streamlit
""")


# -------------------------------
# User Inputs
# -------------------------------
tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.slider("Monthly Charges", 0, 150, 70)

contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

payment = st.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer", "Credit card"]
)

# -------------------------------
# Create Input DataFrame
# -------------------------------
# Create empty dataframe with all model features
input_data = pd.DataFrame(columns=model.feature_names_in_)

# Add one row filled with 0
input_data.loc[0] = 0

# Fill numerical values
input_data['tenure'] = tenure
input_data['MonthlyCharges'] = monthly_charges

# Encode categorical features
input_data['Contract_Two year'] = 1 if contract == "Two year" else 0
input_data['Contract_One year'] = 1 if contract == "One year" else 0
input_data['PaymentMethod_Electronic check'] = 1 if payment == "Electronic check" else 0

# Ensure correct column order
input_data = input_data[model.feature_names_in_]
paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

input_data['PaperlessBilling_Yes'] = 1 if paperless == "Yes" else 0
input_data['InternetService_Fiber optic'] = 1 if internet == "Fiber optic" else 0

# -------------------------------
# Threshold (ADVANCED FEATURE 🔥)
# -------------------------------
threshold = st.slider("Set Churn Threshold", 0.1, 0.9, 0.3)
input_data = input_data + 0.1
# -------------------------------
# Prediction
# -------------------------------
st.write(input_data)
st.subheader("📊 Prediction Result")

if st.button("Predict"):
    prob = model.predict_proba(input_data)[0][1]
    prediction = 1 if prob > 0.3 else 0

    st.write(f"Churn Probability: **{prob:.2f}**")
    

    if prediction == 1:
        st.markdown(
            f"""
            <div style="padding:15px;border-radius:10px;background-color:#ff4b4b;color:white;">
            ⚠️ <b>High Risk of Churn</b><br>
            Probability: {prob:.2f}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.subheader("💡 Insights")
        st.write("""
        - Customer is at high risk due to possible short tenure or high charges  
        - Recommend offering discounts or long-term contract  
        """)

    else:
        st.markdown(
            f"""
            <div style="padding:15px;border-radius:10px;background-color:#2ecc71;color:white;">
            ✅ <b>Low Risk of Churn</b><br>
            Probability: {prob:.2f}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.subheader("💡 Insights")
        st.write("""
        - Customer shows stable behavior  
        - Likely retained due to longer tenure or contract  
        """ )

    