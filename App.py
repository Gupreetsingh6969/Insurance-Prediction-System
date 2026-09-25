import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Insurance Prediction System",
    page_icon="🏥",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("linear_regression_model.pkl")
scaler = joblib.load("scaler.pkl")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f172a,#1e3a8a,#2563eb);
}

h1,h2,h3,h4,p,label{
color:white !important;
}

[data-testid="stSidebar"]{
background:#111827;
}

[data-testid="stSidebar"] *{
color:white;
}

div[data-testid="stForm"]{
background:white;
padding:25px;
border-radius:20px;
box-shadow:0px 8px 25px rgba(0,0,0,0.25);
}

div[data-testid="stForm"] label{
color:black !important;
}

.stButton>button{
width:100%;
height:55px;
font-size:20px;
font-weight:bold;
background:#2563eb;
color:white;
border-radius:12px;
border:none;
}

.stButton>button:hover{
background:#1d4ed8;
}

.result-box{
background:#16a34a;
padding:25px;
border-radius:15px;
text-align:center;
font-size:30px;
font-weight:bold;
color:white;
margin-top:20px;
}

.footer{
text-align:center;
margin-top:40px;
color:white;
font-size:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.title("🏥 Insurance Prediction")

    st.markdown("---")

    st.header("📊 Model")

    st.success("Linear Regression")

    st.metric("Features","8")

    st.metric("Version","1.0")

    st.markdown("---")

    st.header("📖 About")

    st.write("""
This application predicts medical insurance charges using a Machine Learning model.

### Technologies

- Streamlit
- Python
- Pandas
- Scikit-Learn
- Joblib
""")

    st.markdown("---")

    st.header("💡 Health Tips")

    st.info("🏃 Exercise Regularly")

    st.info("🥗 Eat Healthy Food")

    st.info("🚭 Avoid Smoking")

    st.info("💧 Drink Enough Water")

    st.markdown("---")

    st.header("👨‍💻 Developer")

    st.write("**Gurpreet Singh**")

    st.caption("BCA Graduate")

# ---------------- TITLE ----------------
st.markdown(
"""
<h1 style='text-align:center;'>
🏥 Medical Insurance Charges Prediction
</h1>
""",
unsafe_allow_html=True
)

st.write("")

# ---------------- INPUT FORM ----------------
with st.form("prediction_form"):

    col1,col2=st.columns(2)

    with col1:

        age=st.slider("🎂 Age",18,80,25)

        gender=st.selectbox(
            "👤 Gender",
            ["Male","Female"]
        )

        bmi=st.number_input(
            "⚖ BMI",
            10.0,
            60.0,
            24.5
        )

        children=st.slider(
            "👶 Children",
            0,
            5,
            0
        )

    with col2:

        smoker=st.selectbox(
            "🚬 Smoker",
            ["No","Yes"]
        )

        region=st.selectbox(
            "📍 Region",
            [
                "Southwest",
                "Southeast",
                "Northwest",
                "Northeast"
            ]
        )

        st.subheader("📋 Input Summary")

        st.write(f"Age : {age}")

        st.write(f"BMI : {bmi}")

        st.write(f"Children : {children}")

        st.write(f"Gender : {gender}")

        st.write(f"Smoker : {smoker}")

    predict=st.form_submit_button("🔍 Predict Insurance Charges")

# ---------------- PREDICTION ----------------
if predict:

    is_female=1 if gender=="Female" else 0
    is_smoker=1 if smoker=="Yes" else 0

    region_southeast=1 if region=="Southeast" else 0
    region_northwest=1 if region=="Northwest" else 0

    bmi_category_obese=1 if bmi>=30 else 0

    data=pd.DataFrame([[
        age,
        is_female,
        bmi,
        children,
        is_smoker,
        region_southeast,
        bmi_category_obese,
        region_northwest
    ]],
    columns=[
        "age",
        "is_female",
        "bmi",
        "children",
        "is_smoker",
        "region_southeast",
        "bmi_category_obese",
        "region_northwest"
    ])

    try:
        scaled_data=scaler.transform(data)
        prediction=model.predict(scaled_data)[0]
    except:
        prediction=model.predict(data)[0]

    st.markdown(
        f"""
        <div class="result-box">
        💰 Estimated Insurance Charges<br><br>
        ₹ {prediction:,.2f}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.balloons()

# ---------------- FOOTER ----------------
st.markdown(
"""
<div class="footer">
❤️ Developed using Streamlit & Machine Learning
</div>
""",
unsafe_allow_html=True
)