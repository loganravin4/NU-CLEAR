
import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()  

st.title('View Announcements')

#View announcement
url = 'http://api:4000/announcements'
  
response = requests.get(url)
logger.info(response)
st.dataframe(response)   

st.title('Delete Announcement')

job_id = st.text_input("Job ID")
student_id = st.text_input("Student ID")


if st.button("Delete Recommendation"):
    url = 'http://api:4000/announcements'
  
    response = requests.delete(url)
    #logger.info(response)
    #st.dataframe(response)
  