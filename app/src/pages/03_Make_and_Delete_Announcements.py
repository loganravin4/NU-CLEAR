import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()  

st.title('Make Announcement to Students')

announcement = st.text_area("Announcement Text")
user = st.text_input("What is your User ID?")


if st.button("Enter Announcement"):
    if not all([announcement]):
        st.error("All required fields must be filled!")
    else:
        data = {
            'userId' : user,
            "announcement": announcement
        }
    api = 'http://api:4000/advi/announcements'
   
    response = requests.post(api, json=data)
    if response.status_code == 200:
        st.success("Announcement posted succesfully!")
    else:
        st.error(f"Failed to add announcement. Error: {response.status_code} - {response.text}")


st.title('Update Announcement')

announcementId = st.text_input("Announcement ID To Update")
announcementText = st.text_input("Announcement Text To Update To")


if st.button("Update Announcement"):
    if not all([announcementId, announcementText]):
        st.error("All required fields must be filled!")
    else:
        data = {
            'announcementText' : announcementText,
            'announcementId' : announcementId
        }
    url = 'http://api:4000/advi/announcements'

    response = requests.put(url, json=data)
    if response.status_code == 200:
        st.success("Announcement updated succesfully!")
    else:
        st.error(f"Failed to update announcement. Error: {response.status_code} - {response.text}")


st.title('Delete Announcement')

announcementId = st.text_input("Announcement ID")


if st.button("Delete Announcement"):
    if not all([announcementId]):
        st.error("All required fields must be filled!")
    else:
        data = {
            'announcementId' : announcementId,
        }
    url = 'http://api:4000/advi/announcements'

    response = requests.delete(url, json=data)
    if response.status_code == 200:
        st.success("Announcement deleted succesfully!")
    else:
        st.error(f"Failed to delete announcement. Error: {response.status_code} - {response.text}")
 

  
