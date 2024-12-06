import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()  

st.title('My Company\'s Reviews')

col1, col2, col3 = st.columns(3)

with col1:
    rating_min = st.number_input('Minimum Rating', min_value=0.0, max_value=5.0, step=1.0)
    role = st.text_input('Filter by Role (Co-op ID)', placeholder='e.g. 45')

with col2:
    company_id = st.text_input('My Company', placeholder='e.g 123')
    company_name = st.text_input('My Company Name', placeholder='e.g. Google')

logger.info(f'role = {role}')
logger.info(f'rating_min = {rating_min}')
logger.info(f'company_id = {company_id}')
logger.info(f'company_name = {company_name}')


if st.button('Get Reviews', 
             type='primary', 
             use_container_width=True):
    if not company_id:
        st.error("Company ID is required.")
    if not company_name:
        st.error("Company Name is required.")
    url = f'http://api:4000/rev/reviews/{company_name}/{company_id}'
    filters = {}
    
    if role:
        filters['role'] = role
    if rating_min > 0.0:
        filters['rating'] = rating_min

    response = requests.get(url, params=filters).json()
    logger.info(response)
    st.dataframe(response)

