import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome System Administrator, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Manage User Permissions', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/04_User_Management.py')

if st.button('Manage Modules', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/04_Module_Management.py')
  
if st.button('Publish a Co-op Listing', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/04_Add_Coop_Listing.py')