import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Rexy's Dashboard", page_icon="👨‍💻", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
    body {background-color: #0E1117;}
    .hero {
        text-align: center;
        padding: 30px;
    }
    .hero h1 {
        font-size: 48px;
        color: #FFD700;
    }
    .hero h3 {
        color: #ccc;
        font-weight: normal;
    }
    .section {
        padding: 40px 20px;
        margin-bottom: 20px;
    }
    .card {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }
    .footer {
        text-align: center;
        color: #aaa;
        font-size: 14px;
        padding: 20px;
        border-top: 1px solid #333;
    }
    </style>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("<div class='hero'><h1>👋 Hi, I'm Rexy</h1><h3>Data Science | Computer Vision | Digital Forensics</h3></div>", unsafe_allow_html=True)

# --- About Me ---
st.markdown("<div class='section'><h2>About Me</h2></div>", unsafe_allow_html=True)
st.write("""
I am a Master’s graduate in Informatics with strong interest in **Data Analysis** and **Digital Forensics**.  
Skilled in handling large datasets (15,000+ images processed), **Python, R, SQL, OpenCV**,  
and experienced in **data integrity & information security**.  
🌱 Currently exploring Deep Learning & AI for social impact.
""")

# --- Education & Experience (2 Columns) ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='section'><h2>Education</h2></div>", unsafe_allow_html=True)
    st.markdown("""
    - 🎓 **Master in Informatics (M.Kom)**, Atma Jaya Yogyakarta (2023–2025) — GPA: 3.94  
    - 🎓 **Bachelor in Informatics (S.Kom)**, Atma Jaya Yogyakarta (2020–2024) — GPA: 3.60  
    """)

with col2:
    st.markdown("<div class='section'><h2>Experience</h2></div>", unsafe_allow_html=True)
    st.markdown("""
    - 👮 **Internship at Polda Papua (2024)**  
      Managed & secured communication infrastructure (HT, Repeater, SSB).  
      Enhanced device security & network authentication.  

    - 🤖 **Real-time Sign Language Recognition (2025)**  
      Achieved **Precision 98.8%, Recall 99.3%, mAP50 98.9%**.  
      Optimized for low-light conditions (50–350 lux).  
    """)

# --- Skills ---
st.markdown("<div class='section'><h2>Skills</h2></div>", unsafe_allow_html=True)
skills = ["Digital Forensics", "Data Analysis", "Image Processing", "Ethical Hacking", "IoT", "Big Data", "Intelligence System"]
for s in skills:
    st.progress(80)  # nilai bisa diatur sesuai kepercayaan diri
    st.write(s)

# --- Projects ---
st.markdown("<div class='section'><h2>Highlighted Project</h2></div>", unsafe_allow_html=True)
st.image("images/profiles.jpg", width=500)
st.subheader("Real-time Sign Language Recognition")
st.write("A computer vision project with YOLO for detecting Indonesian Sign Language in low-light conditions.")

# --- Footer ---
st.markdown("""
<div class='footer'>
📧 imaderexy@gmail.com | 📱 +62-823-9972-2509 | 📍 Jayapura, Indonesia
</div>
""", unsafe_allow_html=True)
