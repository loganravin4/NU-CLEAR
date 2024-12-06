import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()  

st.title('Compare With Other Companies')

company_id = st.text_input('My Company (CompanyId)', placeholder= 'e.g, 13')
role = st.text_input('Filter by Role (Co-op ID)', placeholder='e.g., 45')

logger.info(f'role = {role}')
logger.info(f'company_id = {company_id}')


if st.button('Get Reviews', 
             type='primary', 
             use_container_width=True):
    if not company_id:
        st.error("Company ID is required.")
    filters = {}
   
    if role:
        filters['role'] = role

    url = f'http://api:4000/rev/reviews/compare/{company_id}'

    response = requests.get(url, params=filters).json()
    logger.info(response)
    st.dataframe(response)
