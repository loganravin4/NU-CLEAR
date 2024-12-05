import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Advisor, {st.session_state['first_name']}.")
st.write('')
st.write('')

if st.button('Make an announcement', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/61_Make_announcement.py')

if st.button('Recommend Jobs to Students', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/62_Recs_students.py')

if st.button("View Classification Demo",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_Classification.py')