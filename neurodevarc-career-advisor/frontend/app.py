# frontend/app.py
import streamlit as st
import sys
import os
from PIL import Image

# Ensure backend can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.career_recommender import get_career_advice

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="NeuroDevArc Career Advisor",
    page_icon="🚀",
    layout="wide"
)

# --- 2. CUSTOM CSS ---
st.markdown("""
<style>
/* --- Background Gradient --- */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #667eea, #764ba2);
}

/* --- Main Card --- */
[data-testid="stAppViewContainer"] > .main > div:first-child {
    background-color: rgba(255, 255, 255, 0.95);
    padding: 3rem;
    border-radius: 25px;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    border: 1px solid rgba(255, 255, 255, 0.18);
    max-width: 850px;
    margin: 2rem auto;
    text-align: center;
}

/* --- Logo --- */
.logo-center {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 180px;
}

/* --- Title --- */
h1 {
    font-size: 3rem;
    font-weight: bold;
    color: #2c3e50;
    margin-top: 15px;
}

/* --- Description --- */
.description {
    color: #34495e;
    font-size: 1.2rem;
    margin-bottom: 20px;
}

/* --- Input Box --- */
div[data-testid="stTextInput"] input {
    border-radius: 12px;
    border: 2px solid #bdc3c7;
    padding: 14px;
    font-size: 1.15rem;
}

/* --- Button --- */
div[data-testid="stButton"] > button {
    background: linear-gradient(90deg, #667eea, #764ba2);
    color: white;
    font-weight: bold;
    border-radius: 12px;
    padding: 14px 25px;
    border: none;
    width: 100%;
    font-size: 1.2rem;
    transition: transform 0.15s ease-in-out;
}
div[data-testid="stButton"] > button:hover {
    transform: scale(1.03);
}

/* --- Expander/Accordion --- */
div[data-testid="stExpander"] {
    border: 1px solid #764ba2;
    border-radius: 12px;
    background-color: #f8f9fa;
    text-align: left;
    padding: 10px;
    margin-bottom: 10px;
}

/* --- Card spacing inside expander --- */
div[data-testid="stExpander"] p {
    margin: 5px 0;
    font-size: 1rem;
}
</style>
""", unsafe_allow_html=True)

# --- 3. LOGO ---
try:
    logo = Image.open("assets/logo.png")
    st.image(logo, width=180, use_column_width=False)
except FileNotFoundError:
    st.warning("⚠️ assets/logo.png not found.")

# --- 4. TITLE & DESCRIPTION ---
st.markdown('<h1>NeuroDevArc Career Advisor</h1>', unsafe_allow_html=True)
st.markdown('<p class="description">Enter your desired career to get a customized roadmap, including skills, resources, and steps you need to succeed! 🚀</p>', unsafe_allow_html=True)

# --- 5. INPUT BOX ---
career_goal = st.text_input(
    "Enter your career goal:", 
    label_visibility="collapsed",
    placeholder="e.g., Data Scientist, Web Developer, UX Designer"
)

# --- 6. BUTTON & BACKEND LOGIC ---
if st.button("🔍 Get Career Advice"):
    if career_goal.strip() == "":
        st.warning("⚠️ Please enter your career goal.")
    else:
        result = get_career_advice(career_goal)
        if result:
            st.success(f"🎯 Recommended Path for **{career_goal.title()}**")
            
            with st.expander("🛠 Skills Required", expanded=True):
                st.write(", ".join(result["skills"]))
            
            with st.expander("📚 Suggested Resources", expanded=True):
                for r in result["resources"]:
                    st.write(f"- {r}")
            
            with st.expander("🗺 Career Roadmap", expanded=True):
                for i, step in enumerate(result["roadmap"], start=1):
                    st.write(f"{i}. {step}")
            
            st.info("✨ Tip: Start with the first skill in the roadmap and stay consistent!")
        else:
            st.error("❌ Sorry, this career isn’t in the database yet. Try Data Scientist, Web Developer, or UX Designer.")
