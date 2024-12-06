
import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()  

st.title('Announcements')

#View announcement
url = 'http://api:4000/announcements'
  
response = requests.get(url)
logger.info(response)
st.dataframe(response)   

if st.button('Make Announcements', 
             type='primary', 
             use_container_width=True):
  st.switch_page('pages/03_Make_Announcements.py')