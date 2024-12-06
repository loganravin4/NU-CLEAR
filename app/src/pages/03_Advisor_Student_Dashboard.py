
import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()  

st.title('My Students')


user_id = st.text_input('Enter your ID Number')
logger.info(f'user_id = {user_id}')

if st.button("Search",type='primary',
             use_container_width=True):
      
        filters = {}
        if user_id:
            filters['userId'] = user_id


        url = f'http://api:4000/advi/student_dashboard'

        response = requests.get(url, params=filters).json()
        logger.info(response)
        st.dataframe(response)  