from analyzer.skill_extractor import extract_skills

text = """
i am a software engineer with experience in python, django, and machine learning. I have worked on several projects involving data
analysis, web development, and natural language processing. My skills include programming in Python, JavaScript, and SQL, as well as using frameworks like Django and Flask. I am also familiar with cloud platforms such as AWS and Azure.
"""

extracted_skills = extract_skills(text)
print("Extracted Skills:", extracted_skills)