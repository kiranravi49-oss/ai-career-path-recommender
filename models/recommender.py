import pandas as pd

# Load dataset properly
df = pd.read_csv("../data/career_paths.csv")

def recommend_career(current_role, experience_level, user_skills):
    
    # Normalize user input
    user_skills = set([skill.strip().lower() for skill in user_skills.split(",")])

    matches = []

    for _, row in df.iterrows():
        if (
            row["current_role"].strip().lower() == current_role.lower()
            and row["experience_level"].strip().lower() == experience_level.lower()
        ):

            required_skills = set([s.strip().lower() for s in row["skills"].split(";")])

            match_score = len(user_skills.intersection(required_skills))

            matches.append({
                "next_role": row["next_role"],
                "match_score": match_score,
                "recommended_skills": row["recommended_skills"]
            })

    # Sort best matches
    matches = sorted(matches, key=lambda x: x["match_score"], reverse=True)

    return matches