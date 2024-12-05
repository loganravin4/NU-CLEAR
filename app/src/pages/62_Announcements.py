
import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()  

st.title('Delete and View Announcements')

url = 'http://api:4000/announcements'
  
response = requests.get(url)
logger.info(response)
st.dataframe(response)      

