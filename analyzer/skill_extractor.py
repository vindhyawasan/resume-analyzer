from .skills import SKILLS
import re

def extract_skills(text):

    text = text.lower()
    found_skills = []

    for skill in SKILLS:
        if re.search(r'\b' + re.escape(skill.lower()) + r'\b', text):
            found_skills.append(skill)

    return found_skills