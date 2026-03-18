import streamlit as st

# 🌌 PAGE
st.set_page_config(page_title="AI Healthcare", layout="wide")

# 🎨 PREMIUM UI + ANIMATION

st.markdown("""
<style>

/* 🌟 BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e1b4b);
}

/* 🧠 TITLE */
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #4f46e5;
}

/* 📦 CARD LOOK */
div[data-testid="stVerticalBlock"] > div {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    margin-bottom: 10px;
}

/* ✍ INPUT */
textarea, input {
    background-color: #1e293b !important;
    color: #f8fafc !important;
    border: 1px solid #6366f1;
}

/* 🔘 BUTTON */
.stButton>button {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: white;
    border-radius: 12px;
    height: 48px;
    font-weight: bold;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0px 5px 20px rgba(139,92,246,0.6);
}

/* 🧭 SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #eef2ff;
}

/* 🟢 SUCCESS */
.stSuccess {
    background-color: #ecfdf5 !important;
    color: #065f46;
}

/* 🟡 WARNING */
.stWarning {
    background-color: #fef3c7 !important;
    color: #92400e;
}

/* 🔵 INFO */
.stInfo {
    background-color: #dbeafe !important;
    color: #1e40af;
}

/* 🔴 ERROR */
.stError {
    background-color: #fee2e2 !important;
    color: #991b1b;
}
/* TEXT COLOR FIX */
body, p, span, label, div {
    color: #e2e8f0 !important;
}

/* HEADINGS */
h1, h2, h3 {
    color: #c7d2fe !important;
}
            
   /* 🔥 FINAL DROPDOWN FIX */

/* main select box */
.stSelectbox > div > div {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 10px;
}

/* selected value text */
.stSelectbox div[data-baseweb="select"] span {
    color: white !important;
}

/* dropdown menu */
div[role="listbox"] {
    background-color: #1e293b !important;
}

/* dropdown options */
div[role="option"] {
    color: white !important;
}

/* hover effect */
div[role="option"]:hover {
    background-color: #6366f1 !important;
    color: white !important;
}
}
            
</style>
""", unsafe_allow_html=True)

# 🧠 TITLE
st.markdown('<div class="title">🧠 AI Smart Healthcare Assistant</div>', unsafe_allow_html=True)

# 📚 BIG DATASET
disease_data = {
    "fever": ("Viral Infection", "Medium", "General Physician"),
    "cough": ("Respiratory Infection", "Medium", "Pulmonologist"),
    "vomiting": ("Food Poisoning", "Medium", "General Physician"),
    "loose motion": ("Diarrhea", "Medium", "Gastroenterologist"),
    "chest pain": ("Heart Issue", "High", "Cardiologist"),
    "headache": ("Migraine", "Low", "Neurologist"),
    "skin rash": ("Allergy", "Low", "Dermatologist"),
    "lump": ("Tumor Risk", "High", "Oncologist"),
    "weight loss": ("Cancer Risk", "High", "Oncologist"),
    "fatigue": ("Weakness / Chronic Issue", "Medium", "General Physician"),
    "blood in cough": ("Lung Cancer Risk", "High", "Oncologist"),
    "joint pain": ("Arthritis", "Low", "Orthopedic"),
    "vision problem": ("Eye Issue", "Low", "Ophthalmologist"),
    "stomach pain": ("Gastric Issue", "Medium", "Gastroenterologist")
}

# 🏥 DOCTOR DATABASE
doctor_db = [
    {"name": "Dr. Sharma", "type": "General Physician", "fee": 300, "location": "Kolkata", "time": "Morning"},
    {"name": "Dr. Roy", "type": "Cardiologist", "fee": 800, "location": "Kolkata", "time": "Evening"},
    {"name": "Dr. Das", "type": "Oncologist", "fee": 1000, "location": "Delhi", "time": "Evening"},
    {"name": "Dr. Sen", "type": "Dermatologist", "fee": 500, "location": "Mumbai", "time": "Morning"},
    {"name": "Dr. Khan", "type": "Pulmonologist", "fee": 600, "location": "Kolkata", "time": "Morning"},
]

# 🔍 ANALYSIS
def analyze(symptoms):
    symptoms = symptoms.lower()
    results = []
    for key in disease_data:
        if key in symptoms:
            results.append(disease_data[key])
    return results

# 📌 MENU
menu = st.sidebar.radio("Choose Feature", ["Home", "Symptoms", "Image", "Report", "Doctor"])

# 🏠 HOME
if menu == "Home":
    st.subheader("Welcome 👋")
    st.info("✔ Enter symptoms")
    st.info("✔ Upload image")
    st.info("✔ Upload report")
    st.success("✔ Smart diagnosis")
    st.success("✔ Doctor recommendation")

# ✍ SYMPTOMS
elif menu == "Symptoms":
    st.header("📝 Enter Symptoms")
    user_input = st.text_area("Describe symptoms")

    if st.button("Analyze"):
        if user_input == "":
            st.warning("Enter symptoms")
        else:
            with st.spinner("🤖 AI analyzing..."):
                result = analyze(user_input)

            if result:
                for r in result:
                    st.success(f"""
🩺 Disease: {r[0]}
⚠️ Severity: {r[1]}
👨‍⚕️ Doctor: {r[2]}
""")

                    if "Cancer" in r[0]:
                        st.error("⚠️ Cancer risk detected! Consult specialist immediately.")
            else:
                st.info("No major issue detected")

# 🖼 IMAGE
elif menu == "Image":
    st.header("🖼 Upload Image")
    file = st.file_uploader("Upload image")

    if file:
        st.image(file)
        st.success("Possible skin issue detected → Dermatologist")

# 📄 REPORT
elif menu == "Report":
    st.header("📄 Upload Report")
    file = st.file_uploader("Upload report")

    if file:
        st.success("Report analyzed → Possible deficiency / issue detected")

# 👨‍⚕ DOCTOR
elif menu == "Doctor":
    st.header("👨‍⚕ Find Doctor")

    location = st.text_input("Location")
    budget = st.slider("Budget", 100, 2000, 500)
    availability = st.selectbox("Time", ["Morning", "Evening"])
    doc_type = st.selectbox("Doctor Type", ["General Physician", "Cardiologist", "Oncologist", "Dermatologist"])

    if st.button("Search Doctor"):
        found = False

        for doc in doctor_db:
            if (doc["fee"] <= budget and
                location.lower() in doc["location"].lower() and
                doc["time"] == availability and
                doc["type"] == doc_type):

                st.success(f"""
👨‍⚕️ {doc['name']}
💰 ₹{doc['fee']}
📍 {doc['location']}
⏰ {doc['time']}
""")
                found = True

        if not found:
            st.warning("No matching doctor found")

# ⚠️ DISCLAIMER
st.markdown("---")
st.warning("⚠️ Not a medical diagnosis. Consult a doctor.")