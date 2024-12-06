import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()  

st.title('Make a Job Recommendation!')

job_id = st.text_input("Job ID")
student_id = st.text_input("Student ID")


if st.button('Post Summary', 
             type='primary', 
             use_container_width=True):
    url = 'http://api:4000/favorites/{user_id}'
    filters = {}
    #need to add a line so it only filters by the users company
    if not all([student_id,job_id]):
        st.error("All required fields must be filled!")
    else:
        data = {
            "comapny_id": student_id,
            "job_id": job_id,
        }

    response = requests.post(url, params=filters)
    logger.info(response)
    st.dataframe(response)
