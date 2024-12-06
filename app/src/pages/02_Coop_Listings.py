import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Co-op Listings')

col1, col2 = st.columns(2)

with col1:
    job_title = st.text_input('Job Title', placeholder='e.g., Software Engineer Co-Op')
    city = st.text_input('Location City', placeholder='e.g., Boston')

with col2:
    state = st.text_input('Location State', placeholder='e.g., Massachusetts')
    country = st.text_input('Location Country', placeholder='e.g., United States')

logger.info(f'job_title = {job_title}')
logger.info(f'city = {city}')
logger.info(f'state = {state}')
logger.info(f'country = {country}')

if st.button('Find Co-ops',
             type='primary',
             use_container_width=True):
    url = 'http://api:4000/coop/coop'
    filters = {}
    if job_title:
        filters['title'] = job_title
    if city:
        filters['locationCity'] = city
    if state:
        filters['locationState'] = state
    if country:
        filters['locationCountry'] = country
    
    response = requests.get(url, params=filters).json()
    logger.info(response)
    st.dataframe(response)

if st.button('Add Job Listing to Favorites List',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/02_Add_Favorited_Jobs.py')