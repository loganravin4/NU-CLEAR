import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Filter Reviews by Student Demographics')

coopLevel_options = ['All',1, 2] 
coopLevel_input = st.selectbox('Select Student Co-op Level(Optional):', coopLevel_options)

year_options = ['All',1, 2,3,4,5] 
year_input = st.selectbox('Select Student Year (Optional):', year_options)


major_input = st.text_input('Enter Major (Optional):', '')

 
logger.info(f'coopLevel = {coopLevel_input}')
logger.info(f'year = {year_input}')
logger.info(f'major = {major_input}')


if st.button('Find Reviews',
             type='primary',
             use_container_width=True):
    url = f'http://api:4000/rev/reviews'

    filters = {
    }
    if coopLevel_input != 'All':
        filters['coopLevel'] = coopLevel_input
    if year_input != 'All':
        filters['year'] = year_input
    if major_input != 'All':
        filters['major'] = major_input
    
    
    response = requests.get(url, params=filters).json()
    logger.info(response)
    st.dataframe(response)

   
   

    

        

  