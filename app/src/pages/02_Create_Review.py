import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Submit a Co-op Review')

col1, col2 = st.columns(2)
with col1:
    user_id = st.text_input("User ID", placeholder="e.g., 123", key="user_id")
    coop = st.text_input("Coop ID", placeholder="e.g., 1", key="coop")
    salary = st.number_input("Salary", min_value=0.0, step=1.0, key="salary")
    rating = st.slider("Rating", min_value=0.0, max_value=5.0, step=0.1, key="rating")
with col2:
    summary = st.text_area("Summary", placeholder="A short summary of your experience", key="summary")
    best_part = st.text_area("Best Part", placeholder="What was the best part of this co-op?", key="best_part")
    worst_part = st.text_area("Worst Part", placeholder="What was the worst part of this co-op?", key="worst_part")

if st.button("Submit Review"):
    if not user_id:
        st.error("User ID is required.")
    elif not coop:
        st.error("Coop is required.")
    elif rating < 0.0 or rating > 5.0:
        st.error("Please select a valid rating between 0.0 and 5.0.")
    else:
        review_data = {
            "coop": coop,
            "salary": salary,
            "rating": rating,
            "summary": summary,
            "bestPart": best_part,
            "worstPart": worst_part
        }
    api = f"http://api:4000/rev/reviews/{user_id}"
   
    response = requests.post(api, json=review_data)

    if response.status_code == 200:
        st.success("Review added successfully!")
    else:
        st.error(f"Failed to add review. Error: {response.status_code} - {response.text}")

    SideBarLinks()