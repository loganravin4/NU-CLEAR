import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()  

st.title('View My Announcements')


url = f'http://api:4000/advi/announcements'

response = requests.get(url, params=None).json()
logger.info(response)
st.dataframe(response)  



