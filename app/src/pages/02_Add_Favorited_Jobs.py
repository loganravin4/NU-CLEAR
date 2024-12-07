import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()  

st.title('Add a Job to Favorites!')

user_id = st.text_input("Student ID")
job_id = st.text_input("Job ID")


if st.button('Add Favorite', 
             type='primary', 
             use_container_width=True):
    url = f'http://api:4000/coop/favorites/{user_id}'
    filters = {}
    #need to add a line so it only filters by the users company
    if not all([user_id,job_id]):
        st.error("All required fields must be filled!")
    else:
        filters = {
            "userId": user_id,
            "coopId": job_id,
        }

    response = requests.post(url, json=filters)
    logger.info(response)
    if response.status_code == 200:
        st.success("Job succesfully added to favorites!")
    else:
        st.error(f"Failed to add to favorite. Error: {response.status_code} - {response.text}")
