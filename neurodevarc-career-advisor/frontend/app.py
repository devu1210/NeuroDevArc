import streamlit as st
import sys
import os
from PIL import Image

# --- Backend import ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.career_recommender import get_career_advice

# --- Page config ---
st.set_page_config(
    page_title="NeuroDevArc Career Advisor",
    page_icon="🚀",
    layout="wide"
)

# --- Custom CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

body, .css-1d391kg {font-family: 'Poppins', sans-serif;}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #667eea, #764ba2);
    background-attachment: fixed;
}

.card {
    background: rgba(255, 255, 255, 0.85);
    border-radius: 25px;
    padding: 2.5rem;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    border: 1px solid rgba(255, 255, 255, 0.18);
    max-width: 850px;
    margin: 2rem auto;
    text-align: center;
}

.logo {
    border-radius: 25px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    margin-bottom: 1rem;
}

h1 {
    font-size: 3rem;
    font-weight: 700;
    color: #2c3e50;
    margin-bottom: 10px;
}

.description {
    font-size: 1.2rem;
    color: #34495e;
    margin-bottom: 25px;
}

input {
    border-radius: 15px !important;
    border: 2px solid #bdc3c7 !important;
    padding: 14px !important;
    font-size: 1.15rem !important;
}

button {
    background: linear-gradient(90deg, #667eea, #764ba2) !important;
    color: white !important;
    font-weight: 600 !important;
    border-radius: 15px !important;
    padding: 14px 25px !important;
    border: none !important;
    font-size: 1.2rem !important;
    width: 100% !important;
    transition: transform 0.15s ease-in-out;
}
button:hover {
    transform: scale(1.05);
}

.expander {
    border-radius: 15px !important;
    padding: 12px !important;
    margin-bottom: 10px;
    background: #f8f9fa !important;
    border: 1px solid #764ba2 !important;
}

.chip {
    display: inline-block;
    background: linear-gradient(90deg, #667eea, #764ba2);
    color: white;
    border-radius: 25px;
    padding: 6px 15px;
    margin: 3px;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# --- App card ---
st.markdown('<div class="card">', unsafe_allow_html=True)

# --- Logo ---
try:
    logo = Image.open("assets/logo.png")
    st.image(logo, width=180, use_column_width=False)
except FileNotFoundError:
    st.warning("⚠️ assets/logo.png not found.")

# --- Title & description ---
st.markdown('<h1>NeuroDevArc Career Advisor</h1>', unsafe_allow_html=True)
st.markdown('<p class="description">Enter your desired career to get a customized roadmap, including skills, resources, and steps you need to succeed! 🚀</p>', unsafe_allow_html=True)

# --- Input ---
career_goal = st.text_input(
    "Enter your career goal:", 
    label_visibility="collapsed",
    placeholder="e.g., Data Scientist, Web Developer, UX Designer"
)

# --- Button & Backend Logic ---
if st.button("🔍 Get Career Advice"):
    if career_goal.strip() == "":
        st.warning("⚠️ Please enter your career goal.")
    else:
        result = get_career_advice(career_goal)
        if result:
            st.success(f"🎯 Recommended Path for **{career_goal.title()}**")

            with st.expander("🛠 Skills Required", expanded=True):
                for skill in result["skills"]:
                    st.markdown(f'<span class="chip">{skill}</span>', unsafe_allow_html=True)

            with st.expander("📚 Suggested Resources", expanded=True):
                for r in result["resources"]:
                    st.write(f"- {r}")

            with st.expander("🗺 Career Roadmap", expanded=True):
                for i, step in enumerate(result["roadmap"], start=1):
                    st.markdown(f'<span class="chip">{i}. {step}</span>', unsafe_allow_html=True)

            st.info("✨ Tip: Start with the first skill in the roadmap and stay consistent!")
        else:
            st.error("❌ Sorry, this career isn’t in the database yet. Try Data Scientist, Web Developer, or UX Designer.")

st.markdown('</div>', unsafe_allow_html=True)
