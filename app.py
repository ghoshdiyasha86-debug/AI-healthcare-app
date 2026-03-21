import streamlit as st
import pandas as pd
from datetime import datetime

# 🌌 PAGE CONFIG
st.set_page_config(page_title="AI Healthcare", layout="wide")

# 🎨 UI
st.markdown("""
<style>

/* 🌌 BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    font-family: 'Segoe UI', sans-serif;
}

/* 🧠 TITLE */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #60a5fa;
    animation: fadeIn 1s ease-in-out;
}

/* ✨ FADE ANIMATION */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(-10px);}
    to {opacity: 1; transform: translateY(0);}
}

/* 📦 CARD */
div[data-testid="stVerticalBlock"] > div {
    background: rgba(30, 41, 59, 0.8);
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.3);
    margin-bottom: 12px;
    animation: fadeIn 0.8s ease-in-out;
}

/* ✍ INPUT */
textarea, input {
    background-color: #020617 !important;
    color: #e2e8f0 !important;
    border: 1px solid #3b82f6 !important;
    border-radius: 10px !important;
}

/* 🔘 BUTTON */
.stButton>button {
    background: linear-gradient(135deg, #3b82f6, #8b5cf6);
    color: white;
    border-radius: 12px;
    height: 45px;
    font-weight: bold;
    border: none;
    transition: all 0.3s ease;
}

.stButton>button:hover {
    transform: scale(1.07);
    box-shadow: 0px 0px 20px rgba(139,92,246,0.8);
}

/* 📤 FILE UPLOADER */
section[data-testid="stFileUploader"] {
    background-color: #020617 !important;
    border: 2px dashed #3b82f6 !important;
    border-radius: 12px;
    padding: 20px;
    color: #e2e8f0 !important;
}

/* 📊 SLIDER */
.stSlider {
    color: white !important;
}

/* 📋 DROPDOWN */
.stSelectbox > div {
    background-color: #020617 !important;
    color: white !important;
    border-radius: 10px;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #e0f2fe, #c7d2fe);
}

/* SUCCESS */
.stSuccess {
    background-color: #022c22 !important;
    color: #22c55e;
}

/* WARNING */
.stWarning {
    background-color: #451a03 !important;
    color: #facc15;
}

/* INFO */
.stInfo {
    background-color: #172554 !important;
    color: #60a5fa;
}

/* ERROR */
.stError {
    background-color: #450a0a !important;
    color: #f87171;
}

/* TEXT */
body, p, span, label {
    color: #e2e8f0 !important;
}

/* HEADINGS */
h1, h2, h3 {
    color: #93c5fd !important;
}

</style>
""", unsafe_allow_html=True)

# 🧠 TITLE
st.markdown('<div class="title">🧠 HEALTH SAATHI</div>', unsafe_allow_html=True)

# 🌐 LANGUAGE
lang = st.sidebar.selectbox("🌐 Language", ["English", "Hindi", "Bengali"])

# ⚙️ MODE
mode = st.sidebar.selectbox("⚙️ Mode", ["Online", "Low Connectivity"])

if mode == "Low Connectivity":
    st.sidebar.info("⚡ Low data mode enabled")

# 📌 MENU
menu = st.sidebar.radio("Choose Feature",
    ["Home", "Symptoms", "Image", "Report", "Doctor", "Patient Records"]
)

# 📚 DATASET
disease_data = {
    "fever": ("Viral Fever", "Medium", "General Physician"),
    "high fever": ("Typhoid", "High", "General Physician"),
    "cough": ("Respiratory Infection", "Medium", "Pulmonologist"),
    "persistent cough": ("Lung Issue", "High", "Pulmonologist"),
    "chest pain": ("Heart Disease", "High", "Cardiologist"),
    "headache": ("Migraine", "Low", "Neurologist"),
    "vomiting": ("Food Poisoning", "Medium", "General Physician"),
    "loose motion": ("Diarrhea", "Medium", "Gastroenterologist"),
    "stomach pain": ("Gastric Issue", "Medium", "Gastroenterologist"),
    "weight loss": ("Cancer Risk", "High", "Oncologist"),
    "lump": ("Tumor Risk", "High", "Oncologist"),
    "skin rash": ("Allergy", "Low", "Dermatologist"),
    "joint pain": ("Arthritis", "Low", "Orthopedic"),
    "fatigue": ("Weakness", "Medium", "General Physician")
}

doctor_db = [
    {"name": "Dr. Sharma", "type": "General Physician", "fee": 200, "location": "Village", "time": "Morning"},
    {"name": "Dr. Roy", "type": "Cardiologist", "fee": 700, "location": "Kolkata", "time": "Evening"},
    {"name": "Dr. Das", "type": "Oncologist", "fee": 900, "location": "District Hospital", "time": "Evening"},
    {"name": "Dr. Sen", "type": "Dermatologist", "fee": 400, "location": "Block Health Center", "time": "Morning"},
]

# 🔍 ANALYSIS FUNCTION
def analyze(symptoms):
    symptoms = symptoms.lower()
    results = []

    for key in disease_data:
        if key in symptoms:
            results.append({
                "disease": disease_data[key][0],
                "severity": disease_data[key][1],
                "doctor": disease_data[key][2]
            })

    if results:
        st.session_state.last_result = results

    return results

# 🏠 HOME
if menu == "Home":
    st.subheader("Welcome 👋")
    st.success("✔ Rural-friendly smart healthcare system")

# ✍ SYMPTOMS
elif menu == "Symptoms":
    st.header("📝 Enter Symptoms")

    user_input = st.text_area("Describe symptoms")

    if st.button("Analyze"):
        result = analyze(user_input)

        if result:
            for r in result:
                st.success(f"""
🩺 Disease: {r['disease']}
⚠️ Severity: {r['severity']}
👨‍⚕️ Doctor: {r['doctor']}
""")

                if "Cancer" in r['disease']:
                    st.error("⚠️ High Risk! Visit specialist immediately.")
        else:
            if mode == "Low Connectivity" and "last_result" in st.session_state:
                st.warning("⚡ Showing last saved result (offline)")
                for r in st.session_state.last_result:
                    st.info(f"{r['disease']} → {r['doctor']}")
            else:
                st.info("No major issue detected")

# 🖼 IMAGE
elif menu == "Image":
    st.header("🖼 Upload Image")

    file = st.file_uploader("Upload image")

    if file:
        st.image(file, width=200)

        if mode == "Low Connectivity":
            st.info("⚡ Basic detection (low data)")
            st.success("Possible skin issue → Visit nearby health center")
        else:
            st.success("Skin condition → Dermatologist")

    st.markdown("### ✍️ Describe manually")
    desc = st.text_area("Describe condition")

    if desc:
        result = analyze(desc)
        for r in result:
            st.info(f"{r['disease']} → {r['doctor']}")

# 📄 REPORT
elif menu == "Report":
    st.header("📄 Upload Report")

    file = st.file_uploader("Upload report", type=["txt"])

    if file:
        content = file.read().decode("utf-8").lower()
        result = analyze(content)

        if result:
            for r in result:
                st.success(f"""
🩺 {r['disease']}
⚠️ {r['severity']}
👨‍⚕️ {r['doctor']}
""")
        else:
            st.info("No issue detected")

    st.markdown("### ✍️ Describe report")
    manual = st.text_area("Enter report details")

    if manual:
        result = analyze(manual)
        for r in result:
            st.info(f"{r['disease']} → {r['doctor']}")

# 👨‍⚕ DOCTOR
elif menu == "Doctor":
    st.header("👨‍⚕ Find Doctor")

    location = st.text_input("Village / City")
    budget = st.slider("Budget", 100, 2000, 500)
    time = st.selectbox("Time", ["Morning", "Evening"])
    doc_type = st.selectbox("Doctor Type", ["General Physician", "Cardiologist", "Oncologist", "Dermatologist"])

    if st.button("Search"):
        found = False

        for doc in doctor_db:
            if (doc["fee"] <= budget and
                location.lower() in doc["location"].lower() and
                doc["time"] == time and
                doc["type"] == doc_type):

                st.success(f"{doc['name']} | ₹{doc['fee']} | {doc['location']}")
                found = True

        if not found:
            st.warning("No doctor found")

    st.info("🏥 Govt hospital support available | Ambulance: 108")

# 📋 PATIENT RECORDS
elif menu == "Patient Records":
    st.header("📋 Patient Tracking")

    if "patients" not in st.session_state:
        st.session_state.patients = []

    name = st.text_input("Name")
    age = st.number_input("Age", 0, 120)
    symptoms = st.text_area("Symptoms")
    location = st.text_input("Village")

    if st.button("Save"):
        st.session_state.patients.append({
            "name": name,
            "age": age,
            "symptoms": symptoms,
            "location": location,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        st.success("Saved!")

    if st.session_state.patients:
        for p in st.session_state.patients:
            st.info(f"{p['name']} | {p['symptoms']} | {p['location']}")

        df = pd.DataFrame(st.session_state.patients)
        st.download_button("⬇ Download CSV", df.to_csv(index=False), "patients.csv")

# ⚠️ DISCLAIMER
st.markdown("---")
st.warning("⚠️ Not a medical diagnosis")
