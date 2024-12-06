import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Co-op Reviews')

col1, col2, col3 = st.columns(3)

with col1:
    created_by = st.text_input('Filter by Created By (User ID)', placeholder='e.g., 123')
    role = st.text_input('Filter by Role (Job ID)', placeholder='e.g., 45')
    rating_min = st.number_input('Minimum Rating', min_value=0.0, max_value=5.0, step=0.5)

with col2:
    salary_min = st.number_input('Minimum Salary', min_value=0.0, value=0.0, step=500.0)
    is_anonymous = st.checkbox('Show Only Anonymous Reviews')
    would_recommend = st.checkbox('Would Recommend')

logger.info(f'created_by = {created_by}')
logger.info(f'role = {role}')
logger.info(f'rating_min = {rating_min}')
logger.info(f'salary_min = {salary_min}')
logger.info(f'is_anonymous = {is_anonymous}')
logger.info(f'would_recommend = {would_recommend}')

if st.button('Get Reviews', 
             type='primary', 
             use_container_width=True):
    url = 'http://api:4000/rev/reviews'
    filters = {}
    if created_by:
        filters['createdBy'] = created_by
    if role:
        filters['role'] = role
    if rating_min > 0.0:
        filters['rating'] = rating_min
    if salary_min > 0.0:
        filters['salary'] = salary_min
    if is_anonymous:
        filters['isAnonymous'] = 'true'
    if would_recommend:
        filters['wouldRecommend'] = 'true'

    response = requests.get(url, params=filters)
    logger.info(response)
    st.dataframe(response)