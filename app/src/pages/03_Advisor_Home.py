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


if st.button('See My Students', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/03_Advisor_Student_Dashboard.py')

if st.button("View All Reviews",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/03_Coop_Reviews.py') 

if st.button('See A Student\'s Favorited Co-ops', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/03_See_User_Favorites.py')

if st.button('Recommend Co-ops to Students', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/03_Student_Recs.py')

if st.button('View Announcements', 
             type='primary', 
             use_container_width=True):
  st.switch_page('pages/03_View_Announcements.py')

if st.button('Create, Update, Delete Announcements', 
             type='primary', 
             use_container_width=True):
  st.switch_page('pages/03_Make_and_Delete_Announcements.py')