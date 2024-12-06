import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()  

st.title('Compare With Another Company')

col1, col2, col3 = st.columns(3)

with col1:
    company_id = st.text_input('My Company (CompanyId)', placeholder= 'e.g, 123')
    role = st.text_input('Filter by What Role (Job ID)', placeholder='e.g., 45')

with col2:
    date_from = st.date_input('Start Date')
    compare_company_id = st.text_input('What Company you want to compare to', placeholder='e.g. 53')

with col3:
    date_to = st.date_input('End Date')

logger.info(f'role = {role}')
logger.info(f'rating_min = {company_id}')
logger.info(f'date_from = {date_from}')
logger.info(f'date_to = {date_to}')


if st.button('Get Reviews', 
             type='primary', 
             use_container_width=True):
    url = 'http://api:4000/rev/reviews/compare/{company_id}'
    filters = {}
   
    if role:
        filters['role'] = role
    if company_id:
        filters['company'] = company_id
    if date_from:
        filters['dateFrom'] = date_from.strftime('%Y-%m-%d')
    if date_to:
        filters['dateTo'] = date_to.strftime('%Y-%m-%d')

    response = requests.get(url, params=filters)
    logger.info(response)
    st.dataframe(response)
