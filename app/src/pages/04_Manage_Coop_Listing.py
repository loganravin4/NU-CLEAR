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

url = f'http://api:4000/coop/coop'
filters = {}

if st.button('Add New Co-op Listing', 
             type='primary', 
             use_container_width=True):
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
            st.success("Co-op succesfully added to co op listings!")
        else:
            st.error(f"Failed to add to listings. Error: {response.status_code} - {response.text}")
            
st.title('Update A Co-op Listing')

coopId = st.text_input("Co-op ID To Update")
title = st.text_input("Title To Update (optional)")
desc = st.text_input("Description To Update (optional)")
city = st.text_input("Location City To Update (optional)")
state = st.text_input("Location State To Update (optional)")
country = st.text_input("Location Country To Update (optional)")


if st.button("Update Announcement"):
    data = {
            'coopId' : coopId,
            'title' : title,
            'description' : desc,
            'locationCity' : city,
            'locationState' : state,
            'locationCountry' : country
        }
    url = f'http://api:4000/coop/coop'

    response = requests.put(url, json=data)
    if response.status_code == 200:
        st.success("Co-op listing updated succesfully!")
    else:
        st.error(f"Failed to update co-op listing. Error: {response.status_code} - {response.text}")


st.title('Delete Co-op Listing')

coopId = st.text_input("Co-op ID To Delete")


if st.button("Delete Co-op Listing"):
    if not all([coopId]):
        st.error("All required fields must be filled!")
    else:
        data = {
            'coopId' : coopId,
        }
    url = f'http://api:4000/coop/coop'

    response = requests.delete(url, json=data)
    if response.status_code == 200:
        st.success("Co-op listing deleted succesfully!")
    else:
        st.error(f"Failed to delete co-op listing. Error: {response.status_code} - {response.text}")