import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

SideBarLinks()

st.title('Your Existing Reviews')

user_id = st.text_input("Enter your User ID", placeholder="e.g., 123")

if user_id:
    url = f"http://api:4000/rev/reviews/{st.session_state['first_name']}/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        reviews = response.json()
    else:
        st.error(f"Failed to fetch reviews. Error: {response.status_code} - {response.text}")
        reviews = []

    if reviews:
        st.table(reviews)

        review_id = st.selectbox(
            "Select a review to edit or delete",
            options=[review['reviewId'] for review in reviews],
            key="review_id"
        )

        try:
            selected_review = next(review for review in reviews if review['reviewId'] == review_id)
        except StopIteration:
            st.error("Review not found. Please refresh the page.")
            selected_review = {}

        if selected_review:
            with st.form("update_review_form"):
                st.subheader("Edit Review")
                summary = st.text_area("Summary", value=selected_review.get('summary', ""))
                best_part = st.text_area("Best Part", value=selected_review.get('bestPart', ""))
                worst_part = st.text_area("Worst Part", value=selected_review.get('worstPart', ""))
                rating = st.slider(
                    "Rating",
                    min_value=0.0,
                    max_value=5.0,
                    value=selected_review.get('rating', 0.0),
                    step=0.5
                )

                submitted_update = st.form_submit_button("Update Review")
                if submitted_update:
                    updated_data = {
                        "reviewId": review_id,
                        "summary": summary,
                        "bestPart": best_part,
                        "worstPart": worst_part,
                        "rating": rating
                    }

                    url_update = f"http://api:4000/rev/reviews/{user_id}/{review_id}"
                    response = requests.put(url_update, json=updated_data)

                    if response.status_code == 200:
                        st.success("Review updated successfully!")
                    else:
                        st.error(f"Failed to update review. Error: {response.status_code} - {response.text}")

                if st.form_submit_button("Delete Review"):
                    url_delete = f"http://api:4000/rev/reviews/{user_id}/{review_id}"
                    response = requests.delete(url_delete)

                    if response.status_code == 200:
                        st.success("Review deleted successfully!")
                    else:
                        st.error(f"Failed to delete review. Error: {response.status_code} - {response.text}")
