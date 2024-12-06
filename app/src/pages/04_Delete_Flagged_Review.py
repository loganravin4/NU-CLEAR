import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()  

reviewId = st.text_input("Review Id: ")
userId = st.text_input("User Id of reviewer: ")

if st.button('Delete', 
             type='primary', 
             use_container_width=True):
    filters = {}
    #need to add a line so it only filters by the users company
    if not all([reviewId, userId]):
        st.error("All required fields must be filled!")
    else:
        url = f'http://api:4000/rev/reviews/{userId}/{reviewId}'
        filters = {
            "userId": userId,
            "reviewId": reviewId
        }

    response = requests.delete(url, json=filters)
    logger.info(response)
    if response.status_code == 200:
        st.success("Review successfully deleted!")
    else:
        st.error(f"Failed to remove review. Error: {response.status_code} - {response.text}")


