import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Submit a Co-op Review')

with st.form("add_review_form"):
    col1, col2 = st.columns(2)
    with col1:
        user_id = st.text_input("User ID", placeholder="e.g., 123", key="user_id")
        role = st.text_input("Role ID", placeholder="e.g., 1", key="role")
        salary = st.number_input("Salary", min_value=0.0, step=1.0, key="salary")
        rating = st.slider("Rating", min_value=0.0, max_value=5.0, step=0.1, key="rating")
    with col2:
        summary = st.text_area("Summary", placeholder="A short summary of your experience", key="summary")
        best_part = st.text_area("Best Part", placeholder="What was the best part of this co-op?", key="best_part")
        worst_part = st.text_area("Worst Part", placeholder="What was the worst part of this co-op?", key="worst_part")
        is_anonymous = st.checkbox("Post Anonymously", key="is_anonymous", value=True)

    submitted = st.form_submit_button("Submit Review")

if submitted:
    st.session_state["role"] == "student"
    if not user_id:
        st.error("User ID is required.")
    elif not role:
        st.error("Role is required.")
    elif rating < 0.0 or rating > 5.0:
        st.error("Please select a valid rating between 0.0 and 5.0.")
    else:
        review_data = {
            "role": role,
            "salary": salary,
            "rating": rating,
            "summary": summary,
            "bestPart": best_part,
            "worstPart": worst_part
        }

    url = f"http://api:4000/rev/reviews/{user_id}"

    response = requests.post(url, json=review_data)
    logger.info(response)

    if response.status_code == 200:
        st.success("Review added successfully!")
    else:
        st.error(f"Failed to add review. Error: {response.status_code} - {response.text}")