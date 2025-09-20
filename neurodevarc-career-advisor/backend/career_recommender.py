# backend/career_recommender.py
import json

def load_careers():
    """Load career data from JSON file"""
    with open("data/skills.json", "r") as f:
        return json.load(f)

def get_career_advice(career_goal: str):
    """Return career details if available"""
    data = load_careers()
    key = career_goal.lower()
    return data.get(key, None)

from pathlib import Path
import json

def load_careers():
    # Path relative to this file
    current_dir = Path(__file__).parent
    skills_file = current_dir / "data" / "skills.json"
    
    with open(skills_file, "r") as f:
        data = json.load(f)
    return data
