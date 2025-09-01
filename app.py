import streamlit as st
import pandas as pd
import base64

# --- Page Config ---
st.set_page_config(page_title="Rexy's Dashboard", page_icon="👨‍💻", layout="wide")

# --- Custom CSS Buttons ---
st.markdown("""
    <style>
    .btn-container {
        text-align: center;
        margin-bottom: 30px;
    }
    .switch-btn {
        display: inline-block;
        margin: 5px;
        padding: 12px 25px;
        font-size: 16px;
        font-weight: bold;
        color: white;
        background: linear-gradient(135deg, #6a11cb, #2575fc);
        border: none;
        border-radius: 25px;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
    }
    .switch-btn:hover {
        transform: scale(1.1);
        box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
    }
    </style>
""", unsafe_allow_html=True)



# Inject CSS
st.markdown(f"""
    <style>
    .hero {{
        text-align: center;
        padding: 40px;
    }}
    .hero h1 {{
        font-size: 52px;
        color: #FFD700;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.6);
    }}
    .hero h3 {{
        color: #f0f0f0;
        font-weight: 300;
    }}
    .section h2 {{
        color: #FFD700;
        border-bottom: 2px solid #FFD700;
        padding-bottom: 5px;
        margin-bottom: 20px;
    }}
    .footer {{
        text-align: center;
        color: #ccc;
        font-size: 14px;
        padding: 20px;
        border-top: 1px solid #555;
        background: rgba(0,0,0,0.6);
    }}
    </style>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("<div class='hero'><h1>👋 Hi, I'm Rexy</h1><h3>Data Science | Computer Vision | Digital Forensics</h3></div>", unsafe_allow_html=True)

# --- About Me ---
st.markdown("<div class='section'><h2>👤 About Me</h2></div>", unsafe_allow_html=True)
st.write("""
I am a Master’s graduate in Informatics with strong interest in **Data Analysis** and **Digital Forensics**.  
Skilled in handling large datasets (15,000+ images processed), **Python, R, SQL, OpenCV**,  
and experienced in **data integrity & information security**.  
🌱 Currently exploring Deep Learning & AI for social impact.
""")

# --- Education & Experience (2 Columns) ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='section'><h2>🎓 Education</h2></div>", unsafe_allow_html=True)
    st.markdown("""
    - 🎓 **Master in Informatics (M.Kom)**, Atma Jaya Yogyakarta (2023–2025) — GPA: 3.94  
    - 🎓 **Bachelor in Informatics (S.Kom)**, Atma Jaya Yogyakarta (2020–2024) — GPA: 3.60  
    """)

with col2:
    st.markdown("<div class='section'><h2>💼 Experience</h2></div>", unsafe_allow_html=True)
    st.markdown("""
    - 👮 **Internship at Polda Papua (2024)**  
      Managed & secured communication infrastructure (HT, Repeater, SSB).  
      Enhanced device security & network authentication.  

    - 🤖 **Real-time Sign Language Recognition (2025)**  
      Achieved **Precision 98.8%, Recall 99.3%, mAP50 98.9%**.  
      Optimized for low-light conditions (50–350 lux).  
    """)


# --- Skills ---
st.markdown("<div class='section'><h2>⚡Skills</h2></div>", unsafe_allow_html=True)

skills = {
    "Digital Forensics": 80,
    "Data Analysis": 100,
    "Image Processing": 100,
    "Ethical Hacking": 80,
    "IoT": 90,
    "Big Data": 90,
    "Intelligence System": 90
}

for skill, level in skills.items():
    st.progress(level)
    st.write(f"{skill} — {level}%")


# # --- Projects ---
# st.markdown("<div class='section'><h2>Highlighted Project</h2></div>", unsafe_allow_html=True)
# st.image("images/profiles.jpg", width=500)
# st.subheader("Real-time Sign Language Recognition")
# st.write("A computer vision project with YOLO for detecting Indonesian Sign Language in low-light conditions.")

# --- Portfolio Documents (CV, Skripsi, Tesis) ---
st.markdown("<div class='section'><h2>📂 Portfolio Documents</h2></div>", unsafe_allow_html=True)


# CV (Link / Download Manual)
st.subheader("📄 Curriculum Vitae")
st.markdown("👉 [Lihat CV Saya](https://drive.google.com/file/d/1asleyZ_TaIOp5jtiduKvcXigPXezwDNt/view?usp=sharing)")
  
# Skripsi
st.subheader("📕 Skripsi")
st.markdown("👉 [Lihat Skripsi Saya](https://repository.uajy.ac.id/id/eprint/32769)")

# Tesis
st.subheader("📘 Tesis")
st.markdown("👉 [Lihat Tesis Saya](https://drive.google.com/your_tesis_link)")

# --- Footer ---
st.markdown("""
<div class='footer'>
📧 imaderexy@gmail.com | 📱 +62-823-9972-2509 | 📍 Jayapura, Indonesia
</div>
""", unsafe_allow_html=True)
