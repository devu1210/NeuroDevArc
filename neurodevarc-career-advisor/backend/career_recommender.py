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
