import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()  

st.title('Summaries of my Companies Data')

col1, col2, col3 = st.columns(3)

with col1:
    avg_rating = st.checkbox('Show Average Ratings by Year')
    count = st.checkbox('Count of bad reviews and good reviews')
    
    
with col2:
    top_benefit = st.checkbox('Show Top Benefit')

with col3:
    top_problem = st.checkbox('Show Top Problem')

logger.info(f'avg_rating = {avg_rating}')
logger.info(f'top_problem = {top_problem}')
logger.info(f'top_benefit = {top_benefit}')

if st.button('Get Summary', 
             type='primary', 
             use_container_width=True):
    url = 'http://api:4000/analysis/summary_report/{company_id}'
    filters = {}
    
    #need to add a line so it only filters by the users company
    #figure out what to do to connect the to backend so that it actually does summaries 
  
    #need to add a line so it only filters by the users company
    if avg_rating:
        filters['avg_rating'] = True
    if count:
        filters['count'] = True
    if top_benefit:
        filters['top_benefit'] = True
    if top_problem:
        filters['top_problem'] = True

    response = requests.get(url, params=filters)
    logger.info(response)
    st.dataframe(response)


    response = requests.get(url, params=filters)
    logger.info(response)
    st.dataframe(response)

