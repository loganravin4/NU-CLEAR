import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()  

st.title('Make Announcement to Students')

announcement = st.text_area("Start typing your announcement here")


if st.button("Enter Announcement"):
    if not all([announcement]):
        st.error("All required fields must be filled!")
    else:
        data = {
            "announcement": announcement,
        }
    url = 'http://api:4000/announcements'
  
    response = requests.post(url)
    logger.info(response)
    st.dataframe(response)     
    #how to make sure its added 
    #how to see other previously posted announcements 


st.title('Delete Announcement')

job_id = st.text_input("Job ID")
student_id = st.text_input("Student ID")


if st.button("Delete Announcement"):
    url = 'http://api:4000/announcements'
  
    response = requests.delete(url)
    logger.info(response)
    st.dataframe(response)
  
