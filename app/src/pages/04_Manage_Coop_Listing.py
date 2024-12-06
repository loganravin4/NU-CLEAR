import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()  

st.title('Publish a Co-op Listing')

company_id = st.text_input("Company ID")
title = st.text_input("Title")
desc = st.text_input("Description")
city = st.text_input("Location City")
state = st.text_input("Location State")
country = st.text_input("Location Country")

if st.button('Add New Co-op Listing', 
             type='primary', 
             use_container_width=True):
    url = f'http://api:4000/coop/coop'
    filters = {}
    #need to add a line so it only filters by the users company
    if not all([company_id,title,desc,city,state,country]):
        st.error("All required fields must be filled!")
    else:
        filters = {
            "locationCity": city,
            "locationState": state,
            "locationCountry": country,
            "title": title,
            "description": desc,
            "company": company_id
        }

        response = requests.post(url, json=filters)
        logger.info(response)
        if response.status_code == 200:
            st.success("Job succesfully added to co op listings!")
        else:
            st.error(f"Failed to add to listings. Error: {response.status_code} - {response.text}")