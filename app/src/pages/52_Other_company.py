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
    company = st.text_input('Filter by Company (CompanyId)', placeholder= 'e.g, 123')
    role = st.text_input('Filter by Role (Job ID)', placeholder='e.g., 45')

with col2:
    date_from = st.date_input('Start Date')

with col3:
    date_to = st.date_input('End Date')

logger.info(f'role = {role}')
logger.info(f'rating_min = {company}')
logger.info(f'date_from = {date_from}')
logger.info(f'date_to = {date_to}')


if st.button('Get Reviews', 
             type='primary', 
             use_container_width=True):
    url = 'http://api:4000/reviews'
    filters = {}
    #need to add a line so it only filters by the users company
    if role:
        filters['role'] = role
    if company > 0.0:
        filters['company'] = company
    if date_from:
        filters['dateFrom'] = date_from.strftime('%Y-%m-%d')
    if date_to:
        filters['dateTo'] = date_to.strftime('%Y-%m-%d')

    response = requests.get(url, params=filters)
    logger.info(response)
    st.dataframe(response)
