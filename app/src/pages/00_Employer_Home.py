import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Employer, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('My Company Reviews', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/00_My_company.py')

if st.button('Other Companies Reviews', 
             type='primary',
             use_container_width=True):
  st.switch_page('app/src/pages/00_Other_company_reviews.py')


if st.button('Summary of Reviews', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/00_summary_reviews.py')