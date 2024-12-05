import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()  

st.title('Make Announcement to Students')

announcement = st.text_area("Start typing your announcement here")


if st.button("Add Summary"):
    if not all([announcement]):
        st.error("All required fields must be filled!")
    else:
        data = {
            "announcement": announcement,
        }
    #how to make sure its added 
    #how to see other previously posted announcements 
        




