import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Co-op Reviews')

col1, col2 = st.columns(2)

with col1:
    role = st.text_input('Filter by Role (Job ID)', placeholder='e.g., 45')
    rating_min = st.number_input('Minimum Rating', min_value=0.0, max_value=5.0, step=0.5)

with col2:
    salary_min = st.number_input('Minimum Salary', min_value=0.0, value=0.0, step=500.0)
    would_recommend = st.checkbox('Would Recommend')

logger.info(f'role = {role}')
logger.info(f'rating_min = {rating_min}')
logger.info(f'salary_min = {salary_min}')
logger.info(f'would_recommend = {would_recommend}')

if st.button('Get Reviews', 
             type='primary', 
             use_container_width=True):
    url = 'http://api:4000/rev/reviews'
    filters = {}
    if role:
        filters['role'] = role
    if rating_min > 0.0:
        filters['rating'] = rating_min
    if salary_min > 0.0:
        filters['salary'] = salary_min
    if would_recommend:
        filters['wouldRecommend'] = 'true'

    response = requests.get(url, params=filters).json()
    logger.info(response)
    st.dataframe(response)
