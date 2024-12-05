import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()  

st.title('My Companies Reviews')


col1, col2, col3 = st.columns(3)

with col1:
    rating_min = st.number_input('Minimum Rating', min_value=0.0, max_value=5.0, step=0.1)
    role = st.text_input('Filter by Role (Job ID)', placeholder='e.g., 45')

with col2:
    date_from = st.date_input('Start Date')

with col3:
    date_to = st.date_input('End Date')