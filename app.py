import streamlit as st

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Sneha Pundalik Lad | HR Portfolio",
    page_icon="💼",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

.hero {
    background: linear-gradient(135deg,#0F172A,#1E293B);
    border-radius:20px;
    padding:50px;
    color:white;
    margin-bottom:30px;
}

.gold {
    color:#D4AF37;
}

.card {
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

.skill-card{
    background:#fff;
    padding:15px;
    border-left:5px solid #D4AF37;
    border-radius:10px;
}

.footer{
    text-align:center;
    color:gray;
    padding:30px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ---------------- #

col1, col2 = st.columns([2,1])

with col1:

    st.markdown("""
    <div class="hero">

    <h4 class="gold">
    ASPIRING HUMAN RESOURCE PROFESSIONAL
    </h4>

    <h1>
    Sneha Pundalik Lad
    </h1>

    <p>
    PGDM (Human Resource) student with practical HR internship experience,
    strong communication abilities, and a passion for people development,
    employee engagement, recruitment support, and organizational growth.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col2:

    try:
        st.image(
            "profile.jpg",
            use_container_width=True
        )
    except:
        st.info("Upload profile.jpg to repository")

# ---------------- RESUME DOWNLOAD ---------------- #

st.subheader("📄 Resume")

try:
    with open("resume.pdf", "rb") as file:
        st.download_button(
            label="Download Resume",
            data=file,
            file_name="Sneha_Pundalik_Lad_Resume.pdf",
            mime="application/pdf"
        )
except:
    st.warning("Upload resume.pdf to enable download.")

# ---------------- ABOUT ME ---------------- #

st.markdown("---")
st.header("About Me")

st.markdown("""
Looking forward to gaining knowledge and experience to enhance my skills and
use my business studies background for organizational success.

Currently pursuing PGDM in Human Resource Management with a strong academic
foundation in Management Studies. I am interested in employee engagement,
recruitment, workplace culture, people development, and continuous learning.

I aspire to contribute to people-centric organizations and support workforce
development through effective HR practices and communication.
""")

# ---------------- EDUCATION ---------------- #

st.markdown("---")
st.header("Education")

education = [
    ("PGDM - Human Resource", "Sasmira's Business School, Worli", "Pursuing"),
    ("Bachelor of Management Studies", "Sasmira's Institute of Commerce & Science", "CGPA: 7.34"),
    ("Higher Secondary Certificate (HSC)", "K.P.B. Hinduja College of Commerce", "81%"),
    ("Secondary School Certificate (SSC)", "I.E.S. V.N. Sule Guruji", "67%")
]

for degree, institute, result in education:
    st.markdown(f"""
    <div class="card">
    <h4>{degree}</h4>
    <p><b>{institute}</b></p>
    <p>{result}</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- SKILLS ---------------- #

st.markdown("---")
st.header("Skills & Abilities")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="skill-card">

    ✅ MS-CIT

    ✅ Typing English-30

    ✅ Canva

    ✅ Quick Learner

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="skill-card">

    ✅ Adaptable & Flexible

    ✅ Problem Solving Ability

    ✅ Decision Making

    ✅ Communication

    </div>
    """, unsafe_allow_html=True)

# ---------------- EXPERIENCE ---------------- #

st.markdown("---")
st.header("Internship Experience")

st.markdown("""
<div class="card">

<h3>HR Intern</h3>

<b>
True Value Marketing Services Pvt. Ltd.
(Granules & Beans)
</b>

<br><br>

• Conducted training sessions on HR policies for the Service Department.

• Created PowerPoint presentations used as training material.

• Interviewed candidates at college campuses for recruitment activities.

</div>
""", unsafe_allow_html=True)

# ---------------- EXTRACURRICULAR ---------------- #

st.markdown("---")
st.header("Leadership & Extracurricular Activities")

st.success(
    "Volunteered at HRIA Conclave 2025 organized by Sasmira's Business School"
)

st.success(
    "Served as BMS Club Co-ordinator for Spontania Event 2024"
)

st.success(
    "Served as Technical Head for Youthon Event 2026"
)

# ---------------- PROJECTS ---------------- #

st.markdown("---")
st.header("Projects & Case Studies")

st.info("""
Add your HR projects, recruitment studies,
employee engagement research, and case studies here.
""")

# ---------------- CERTIFICATIONS ---------------- #

st.markdown("---")
st.header("Certifications & Workshops")

st.info("""
Add your certifications and workshop details here.
""")

# ---------------- PERSONAL DETAILS ---------------- #

st.markdown("---")
st.header("Personal Details")

st.markdown("""
**Date of Birth:** 9 December 2003

**Marital Status:** Unmarried

**Languages Known:** English, Marathi, Hindi

**Hobbies:** Listening to Music, Cooking
""")

# ---------------- CONTACT ---------------- #

st.markdown("---")
st.header("Contact Information")

st.markdown("""
📧 **Email:** snehaplad0903@gmail.com

📱 **Phone:** 8082271971

📍 **Location:** Mumbai, Maharashtra

🔗 **LinkedIn:** Add Your LinkedIn URL
""")

# ---------------- CONTACT FORM ---------------- #

st.markdown("---")
st.header("Send a Message")

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")

if st.button("Submit"):
    st.success("Thank you for visiting my portfolio.")

# ---------------- FOOTER ---------------- #

st.markdown("---")

st.markdown("""
<div class="footer">

<h3>Sneha Pundalik Lad</h3>

Aspiring Human Resource Professional

<br><br>

© 2026 All Rights Reserved

</div>
""", unsafe_allow_html=True)