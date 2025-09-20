# frontend/app.py
import streamlit as st
import sys
import os
from PIL import Image



st.image("assets/logo.png", width=150)

# backend/career_recommender.py
with open("data/skills.json", "r") as f:



# Ensure the backend module can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.career_recommender import get_career_advice

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="NeuroDevArc Career Advisor", 
    page_icon="🤖", 
    layout="wide"
)

# --- 2. UPDATED CUSTOM CSS ---
st.markdown("""
<style>
    /* --- Main App Background --- */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #667eea, #764ba2);
    }

    /* --- THIS IS THE NEW, MORE RELIABLE METHOD TO CREATE THE CARD --- */
    /* We are styling Streamlit's own main content block directly */
    [data-testid="stAppViewContainer"] > .main > div:first-child {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
        max-width: 800px;
        margin: 2rem auto;
        text-align: center;
    }
    .st-emotion-cache-13k62yr {
    position: absolute;
    background: rgb(14, 17, 23);
    color: rgb(8 7 7);
    inset: 0px;
    color-scheme: dark;
    overflow: hidden;
}

    /* --- Typography (no changes needed here) --- */
    h1 {
        font-size: 2.8rem;
        font-weight: bold;
        color: #2c3e50;
    }
    
    p {
        color: #34495e;
        font-size: 1.1rem;
    }

    /* --- Input Box and Button (no changes needed here) --- */
    div[data-testid="stTextInput"] input {
        border-radius: 10px;
        border: 2px solid #bdc3c7;
        padding: 12px;
        font-size: 1.1rem;
    }
    
    div[data-testid="stButton"] > button {
        background: linear-gradient(90deg, #667eea, #764ba2);
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 12px 20px;
        border: none;
        width: 100%;
        font-size: 1.2rem;
        transition: transform 0.1s ease-in-out;
    }
    div[data-testid="stButton"] > button:hover {
        transform: scale(1.02);
    }
    
    /* --- Expander/Accordion Styles --- */
    div[data-testid="stExpander"] {
        border: 1px solid #764ba2;
        border-radius: 12px;
        background-color: #f8f9fa;
        text-align: left
        text-color: black;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. APP LAYOUT (NO MORE DIV WRAPPERS) ---

# Logo
try:
    logo = Image.open("assets/logo.png")
    st.image(logo, width=120) 
except FileNotFoundError:
    st.warning("assets/logo.png not found.")

# Title and Description
st.title("NeuroDevArc Career Advisor")
st.markdown("<p>Enter your desired career to get a customized roadmap, including the skills, resources, and steps you need to succeed! 🚀</p>", unsafe_allow_html=True)

# Input
career_goal = st.text_input(
    "Enter your career goal:", 
    label_visibility="collapsed",
    placeholder="e.g., Data Scientist, Web Developer, UX Designer"
)

# --- 4. BACKEND LOGIC (UNCHANGED) ---
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
