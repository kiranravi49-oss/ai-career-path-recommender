import streamlit as st
import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.recommender import recommend_career

# Title
st.title("AI Career Path Recommender")

# -----------------------------
# INPUT SECTION
# -----------------------------
st.subheader("Enter Your Details")

current_role = st.selectbox(
    "Current Role",
    ["Project Manager", "Business Analyst", "Software Engineer", "Tester"]
)

experience_level = st.selectbox(
    "Experience Level",
    ["mid", "senior"]
)

user_skills = st.text_input(
    "Enter your skills (comma separated)",
    "agile, delivery"
)

# -----------------------------
# RECOMMENDATION
# -----------------------------
if st.button("Get Career Recommendation"):

    results = recommend_career(current_role, experience_level, user_skills)

    if results:

        # -----------------------------
        # Top 3 Recommendations
        # -----------------------------
        st.subheader("🏆 Top Career Recommendations")

        top_3 = results[:3]

        for i, r in enumerate(top_3, start=1):
            st.markdown(f"### {i}. {r['next_role']}")
            st.write(f"Match Score: {r['match_score']}")
            st.write(f"Recommended Skills: {r['recommended_skills']}")
            st.write("---")

        # -----------------------------
        # Best Career Path
        # -----------------------------
        top_result = top_3[0]

        st.subheader("🎯 Best Career Path")
        st.success(f"{top_result['next_role']}")

        # -----------------------------
        # Career Roadmap
        # -----------------------------
        st.subheader("🛤️ Career Roadmap")

        skills = top_result["recommended_skills"].split(";")

        for step, skill in enumerate(skills, start=1):
            st.write(f"Step {step}: Learn {skill}")

        # -----------------------------
        # AI Insight
        # -----------------------------
        st.subheader("🧠 Career Insight")

        if top_result["match_score"] >= 2:
            st.info("You are very close to this role. Focus on finishing the last mile of skills.")
        elif top_result["match_score"] == 1:
            st.warning("You are partially aligned. Build 2–3 strong skills to transition.")
        else:
            st.error("You need a structured learning path before transitioning.")

    else:
        st.warning("No matching career path found")