import streamlit as st

career_paths = {
    "Data Science": ["Python", "Statistics", "Data Analysis"],
    "Machine Learning": ["Python", "Math", "ML Algorithms"],
    "NLP": ["Python", "Text Processing", "Linguistics"],
    "Computer Vision": ["Python", "Image Processing", "OpenCV"],
    "AI Ethics": ["Philosophy", "AI", "Ethical AI"],
    "AI Engineering": ["Python", "Deployment", "Cloud"],
}

st.title("AI Career Path Recommender")

st.write("**Select your skills or interests:**")
options = list(set(skill for skills in career_paths.values() for skill in skills))
selected_skills = st.multiselect("Choose skills:", options)

recommended = []

for path, skills in career_paths.items():
    match_count = len(set(selected_skills) & set(skills))
    if match_count >= 2:
        recommended.append((path, match_count))

if st.button("Get Recommendation"):
    if recommended:
        recommended.sort(key=lambda x: x[1], reverse=True)
        st.success("Recommended Career Paths:")
        for path, _ in recommended:
            st.write(f"- {path}")
    else:
        st.warning("No strong match found. Try selecting more skills.")
