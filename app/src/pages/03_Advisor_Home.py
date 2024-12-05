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


if st.button('Make an Announcement', 
             type='primary', 
             use_container_width=True):
  st.switch_page('pages/61_Make_announcement.py')

  if st.button('Delete and View Announcements', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/62_Delete_and_View_Announcements.py')

if st.button('Recommend Jobs to Students', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/63_Recs_students.py')

if st.button("View All Reviews",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_Coop_Reviews.py') 
  