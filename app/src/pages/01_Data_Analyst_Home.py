import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Data Analyst, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Add a Summary Report for a Company', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_Summary_Report.py')
 
if st.button('Look at Co-op Reviews and Student Demographics', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_Coop_Review_by_Demographic.py')

if st.button("Add Visualizations from Reviews",
             type='primary', 
             use_container_width=True): 
  st.switch_page('pages/13_Add_Visualizations.py')    