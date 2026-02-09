# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 01:27:38 2026

@author: akash
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved model

# ================== Diabetes ==================
diabetes_model = pickle.load(open(r'C:\Users\akash\Documents\Multiple disease deploy models\Deploy multi model\trained_model.sav', 'rb'))

diabetes_scaler = pickle.load(open(r'C:\Users\akash\Documents\Multiple disease deploy models\Deploy multi model\scaler.sav', 'rb'))


# ================== Heart Disease ==================
heart_model = pickle.load(open(r'C:\Users\akash\Documents\Multiple disease deploy models\Deploy multi model\Heart_disease_model.sav', 'rb'))


# ================== Parkinson ==================
parkinson_model = pickle.load(open(r'C:\Users\akash\Documents\Multiple disease deploy models\Deploy multi model\parkinson_model.sav', 'rb'))

parkinson_scaler = pickle.load(open(r'C:\Users\akash\Documents\Multiple disease deploy models\Deploy multi model\scaler_par.sav', 'rb'))


#sidebar for navigate

with st.sidebar:

    #brand header
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #ff4b4b, #ff9a9a);
            padding:18px;
            border-radius:16px;
            text-align:center;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
        ">
            <h2 style="color:white; margin-bottom:5px;">🏥 MedAI Care</h2>
            <p style="color:white; font-size:13px; margin:0;">
                Smart Multi-Disease Prediction
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # ================= STATUS BADGE =================
    st.markdown(
        """
        <div style="
            background-color:#e6fff2;
            padding:8px 12px;
            border-radius:10px;
            text-align:center;
            border-left:4px solid #00c853;
            font-size:13px;
        ">
            🟢 System Status: <b>Online</b>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # ================= MENU =================
    selected = option_menu(
        "🧭 Select Health Check",
        [
            "Diabetes Prediction",
            "Heart Disease Prediction",
            "Parkinson Prediction"
        ],
        icons=[
            "activity",
            "heart-pulse",
            "person-lines-fill"
        ],
        menu_icon="clipboard2-pulse",
        default_index=0,
        styles={
            "container": {
                "padding": "0!important",
                "background-color": "#f9f9f9",
            },
            "icon": {
                "font-size": "20px",
                "color": "#ff4b4b",
            },
            "nav-link": {
                "font-size": "16px",
                "padding": "12px 15px",
                "border-radius": "12px",
                "margin": "6px",
                "font-weight": "500",
            },
            "nav-link-selected": {
                "background": "linear-gradient(90deg, #ff4b4b, #ff7b7b)",
                "color": "white",
                "box-shadow": "0px 4px 8px rgba(255,75,75,0.4)",
                "font-weight": "700",
            },
        },
    )

    st.write("")

    # ================= TRUST MESSAGE =================
    st.markdown(
        """
        <div style="
            background:#f0f2f6;
            padding:12px;
            border-radius:12px;
            font-size:13px;
        ">
            🔐 Your data is <b>not stored</b><br>
            ⚕️ For awareness & early risk detection
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # ================= FOOTER =================
    st.markdown(
        """
        <hr>
        <div style="text-align:center; font-size:12px; color:gray;">
            🔬 Powered by Machine Learning<br>
            🚀 Built with Streamlit
        </div>
        """,
        unsafe_allow_html=True
    )


    
# ========================= DIABETES =========================
if selected == 'Diabetes Prediction':

    # Header section
    st.markdown(
        """
        <div style="background: linear-gradient(90deg, #ff4b4b, #ff7b7b);
                    padding:20px;
                    border-radius:15px">
            <h2 style="color:white; text-align:center;">🩸 Diabetes Risk Assessment</h2>
            <p style="color:white; text-align:center;">
                A smart ML-powered health check in seconds
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.info("👋 Don’t worry! Just enter the details honestly. We’ll do the analysis.")

    # Progress feeling
    st.markdown("### 📝 Patient Health Details")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### 👩‍⚕️ Personal")
        Pregnancies = st.number_input("Number of Pregnancies", min_value=0)
        Age = st.number_input("Age (years)", min_value=1)

    with col2:
        st.markdown("#### 🧪 Blood Test")
        Glucose = st.number_input("Glucose Level (mg/dL)", min_value=0)
        BloodPressure = st.number_input("Blood Pressure (mm Hg)", min_value=0)
        Insulin = st.number_input("Insulin Level", min_value=0)

    with col3:
        st.markdown("#### 📊 Body Metrics")
        SkinThickness = st.number_input("Skin Thickness", min_value=0)
        BMI = st.number_input("BMI (Body Mass Index)", min_value=0.0, format="%.1f")
        DiabetesPedigreeFunction = st.number_input(
            "Genetic Risk (DPF)", min_value=0.0, format="%.3f"
        )

    st.write("")
    st.markdown("---")

    # Big CTA button
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        predict = st.button("🔍 Check Diabetes Risk", use_container_width=True)

    if predict:
        with st.spinner("🧠 Analyzing health data... Please wait"):
            input_data = [[
                Pregnancies,
                Glucose,
                BloodPressure,
                SkinThickness,
                Insulin,
                BMI,
                DiabetesPedigreeFunction,
                Age
            ]]

            input_data = diabetes_scaler.transform(input_data)
            prediction = diabetes_model.predict(input_data)

        st.markdown("### 📋 Prediction Report")

        if prediction[0] == 1:
            st.markdown(
                """
                <div style="background-color:#ffe6e6;
                            padding:20px;
                            border-radius:15px;
                            border-left:6px solid red;">
                    <h4>⚠️ High Risk Detected</h4>
                    <p>The model indicates a <b>higher chance of Diabetes</b>.</p>
                    <p>📌 Please consult a healthcare professional.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                """
                <div style="background-color:#e6fff2;
                            padding:20px;
                            border-radius:15px;
                            border-left:6px solid green;">
                    <h4>✅ Low Risk Detected</h4>
                    <p>The model indicates <b>No signs of Diabetes</b>.</p>
                    <p>🎉 Keep maintaining a healthy lifestyle!</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.caption("⚕️ This tool supports decision-making and does not replace medical diagnosis.")

    
    
# ========================= HEART DISEASE =========================

if selected == 'Heart Disease Prediction':

    # ===== HEADER CARD =====
    st.markdown(
        """
        <div style="
            background: linear-gradient(90deg, #ff6b6b, #ff8787);
            padding:20px;
            border-radius:16px;
            text-align:center;
            box-shadow:0 6px 12px rgba(0,0,0,0.15);
        ">
            <h2 style="color:white;">❤️ Heart Health Risk Assessment</h2>
            <p style="color:white; font-size:14px;">
                AI-powered early heart disease screening
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.info("🫀 Your heart matters. Fill the details carefully for accurate analysis.")

    st.markdown("### 📝 Patient Clinical Information")

    # ===== INPUT SECTIONS =====
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("👤 Personal")
        age = st.number_input('Age (years)', min_value=1)
        sex = st.selectbox('Sex', ['Male', 'Female'])
        sex = 1 if sex == 'Male' else 0

        cp = st.selectbox(
            'Chest Pain Type',
            ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic']
        )

        cp = {
            'Typical Angina': 0,
            'Atypical Angina': 1,
            'Non-anginal Pain': 2,
            'Asymptomatic': 3
        }[cp]

    with col2:
        st.subheader("🧪 Vital Signs")
        trestbps = st.number_input('Resting Blood Pressure (mm Hg)')
        chol = st.number_input('Serum Cholesterol (mg/dl)')
        fbs = st.selectbox(
            'Fasting Blood Sugar > 120 mg/dl?',
            ['No', 'Yes']
        )
        fbs = 1 if fbs == 'Yes' else 0

        restecg = st.selectbox(
            'Resting ECG Result',
            ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy']
        )
        restecg = {
            'Normal': 0,
            'ST-T Wave Abnormality': 1,
            'Left Ventricular Hypertrophy': 2
        }[restecg]

    with col3:
        st.subheader("🏃 Exercise Test")
        thalach = st.number_input('Maximum Heart Rate Achieved')
        exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])
        exang = 1 if exang == 'Yes' else 0

        oldpeak = st.number_input('ST Depression', format="%.1f")

        slope = st.selectbox(
            'Slope of ST Segment',
            ['Upsloping', 'Flat', 'Downsloping']
        )
        slope = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}[slope]

        ca = st.number_input('Major Vessels Colored (0–3)', min_value=0, max_value=3)

        thal = st.selectbox(
            'Thalassemia',
            ['Normal', 'Fixed Defect', 'Reversible Defect']
        )
        thal = {'Normal': 1, 'Fixed Defect': 2, 'Reversible Defect': 3}[thal]

    st.markdown("---")

    # ===== BIG CTA BUTTON =====
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        check_heart = st.button(
            '❤️ Analyze Heart Disease Risk',
            use_container_width=True
        )

    # ===== PREDICTION RESULT =====
    if check_heart:
        with st.spinner("🧠 Analyzing heart health data..."):
            input_data = [[
                age, sex, cp, trestbps, chol, fbs,
                restecg, thalach, exang, oldpeak,
                slope, ca, thal
            ]]

            prediction = heart_model.predict(input_data)

        st.markdown("### 📋 Heart Health Report")

        if prediction[0] == 1:
            st.markdown(
                """
                <div style="
                    background:#ffe6e6;
                    padding:20px;
                    border-radius:15px;
                    border-left:6px solid red;
                ">
                    <h4>⚠️ High Risk Detected</h4>
                    <p>The model indicates a <b>possible risk of heart disease</b>.</p>
                    <p>🩺 Please consult a cardiologist.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                """
                <div style="
                    background:#e6fff2;
                    padding:20px;
                    border-radius:15px;
                    border-left:6px solid green;
                ">
                    <h4>✅ Low Risk Detected</h4>
                    <p>No signs of heart disease detected.</p>
                    <p>💪 Keep up a healthy lifestyle!</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.caption("⚕️ This tool supports early risk detection and does not replace medical diagnosis.")

    
    
# ========================= PARKINSON =========================
if selected == 'Parkinson Prediction':

    # ================= HERO HEADER =================
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            padding:22px;
            border-radius:18px;
            text-align:center;
            box-shadow:0 8px 16px rgba(0,0,0,0.2);
        ">
            <h2 style="color:white;">🧠 Parkinson’s Voice Analysis</h2>
            <p style="color:white; font-size:14px;">
                AI-powered early neurological risk detection
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.info("🎙️ This test analyzes **voice signal measurements**. Small decimal values are normal.")

    st.markdown("### 🧪 Voice Signal Parameters")
    st.markdown("---")

    # ================= INPUT SECTIONS =================
    col1, col2, col3 = st.columns(3)

    # ---------- COLUMN 1 ----------
    with col1:
        st.subheader("🔊 Frequency")
        MDVP_Fo = st.number_input('MDVP:Fo(Hz)', format="%.3f")
        MDVP_Fhi = st.number_input('MDVP:Fhi(Hz)', format="%.3f")
        MDVP_Flo = st.number_input('MDVP:Flo(Hz)', format="%.3f")

        st.subheader("📉 Jitter")
        MDVP_Jitter_percent = st.number_input(
            'MDVP:Jitter(%)', format="%.6f", step=0.000001
        )
        MDVP_Jitter_Abs = st.number_input(
            'MDVP:Jitter(Abs)', format="%.8f", step=0.00000001
        )
        MDVP_RAP = st.number_input(
            'MDVP:RAP', format="%.6f", step=0.000001
        )
        MDVP_PPQ = st.number_input(
            'MDVP:PPQ', format="%.6f", step=0.000001
        )

    # ---------- COLUMN 2 ----------
    with col2:
        st.subheader("📈 Shimmer")
        Jitter_DDP = st.number_input(
            'Jitter:DDP', format="%.6f", step=0.000001
        )
        MDVP_Shimmer = st.number_input(
            'MDVP:Shimmer', format="%.6f", step=0.000001
        )
        MDVP_Shimmer_dB = st.number_input(
            'MDVP:Shimmer(dB)', format="%.6f", step=0.000001
        )
        Shimmer_APQ3 = st.number_input(
            'Shimmer:APQ3', format="%.6f", step=0.000001
        )
        Shimmer_APQ5 = st.number_input(
            'Shimmer:APQ5', format="%.6f", step=0.000001
        )
        MDVP_APQ = st.number_input(
            'MDVP:APQ', format="%.6f", step=0.000001
        )
        Shimmer_DDA = st.number_input(
            'Shimmer:DDA', format="%.6f", step=0.000001
        )

    # ---------- COLUMN 3 ----------
    with col3:
        st.subheader("🧠 Neurological Features")
        NHR = st.number_input('NHR', format="%.6f", step=0.000001)
        HNR = st.number_input('HNR', format="%.3f")
        RPDE = st.number_input('RPDE', format="%.6f", step=0.000001)
        DFA = st.number_input('DFA', format="%.6f", step=0.000001)
        spread1 = st.number_input('spread1', format="%.6f", step=0.000001)
        spread2 = st.number_input('spread2', format="%.6f", step=0.000001)
        D2 = st.number_input('D2', format="%.6f", step=0.000001)
        PPE = st.number_input('PPE', format="%.6f", step=0.000001)

    st.markdown("---")

    # ================= CTA BUTTON =================
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        analyze = st.button(
            "🧠 Analyze Parkinson’s Risk",
            use_container_width=True
        )

    # ================= PREDICTION =================
    if analyze:
        with st.spinner("🔬 Analyzing voice patterns with Machine Learning..."):

            input_data = [[
                MDVP_Fo,
                MDVP_Fhi,
                MDVP_Flo,
                MDVP_Jitter_percent,
                MDVP_Jitter_Abs,
                MDVP_RAP,
                MDVP_PPQ,
                Jitter_DDP,
                MDVP_Shimmer,
                MDVP_Shimmer_dB,
                Shimmer_APQ3,
                Shimmer_APQ5,
                MDVP_APQ,
                Shimmer_DDA,
                NHR,
                HNR,
                RPDE,
                DFA,
                spread1,
                spread2,
                D2,
                PPE
            ]]

            input_data = parkinson_scaler.transform(input_data)
            prediction = parkinson_model.predict(input_data)

        st.markdown("### 📋 Neurological Assessment Report")

        if prediction[0] == 1:
            st.markdown(
                """
                <div style="
                    background:#fbe9e9;
                    padding:22px;
                    border-radius:16px;
                    border-left:6px solid #d32f2f;
                ">
                    <h4>⚠️ Elevated Risk Detected</h4>
                    <p>The model indicates a <b>possible presence of Parkinson’s disease</b>.</p>
                    <p>🩺 Early medical consultation is strongly recommended.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                """
                <div style="
                    background:#e8f5e9;
                    padding:22px;
                    border-radius:16px;
                    border-left:6px solid #2e7d32;
                ">
                    <h4>✅ No Risk Detected</h4>
                    <p>The analysis shows <b>no signs of Parkinson’s disease</b>.</p>
                    <p>🌱 Maintain vocal & neurological health.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.caption("⚕️ This AI tool supports early screening and does not replace clinical diagnosis.")
    