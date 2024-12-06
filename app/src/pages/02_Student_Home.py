import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Student, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View Co-op Listings', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_Coop_Listings.py')

if st.button('View Co-op Reviews', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_Coop_Reviews.py')

if st.button('Create a Co-op Review', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_Create_Review.py')

if st.button("View Your Existing Reviews",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_User_Reviews.py')

if st.button("View Your Favorited Jobs",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_Favorited_Jobs.py')