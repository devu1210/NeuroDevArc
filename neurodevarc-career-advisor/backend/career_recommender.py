# backend/career_recommender.py
import os, json

def load_careers():
    base_path = os.path.dirname(os.path.dirname(__file__))  # go up from backend/
    data_path = os.path.join(base_path, "data", "skills.json")
    with open(data_path, "r") as f:
        return json.load(f)


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


def load_careers():
    # Path relative to this file
    current_dir = Path(__file__).parent
    skills_file = current_dir / "data" / "skills.json"
    
    with open(skills_file, "r") as f:
        data = json.load(f)
    return data




