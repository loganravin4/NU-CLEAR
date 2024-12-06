import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()  

st.title('Summary of My Company\'s Reviews')

company_id = st.text_input("Company ID", placeholder="e.g., 123", key="company_id")


if st.button('Get Summary', 
             type='primary', 
             use_container_width=True):
    url = f'http://api:4000/rev/analysis/summary_report/{company_id}'

    response = requests.get(url).json()
    logger.info(response)
    st.dataframe(response)
