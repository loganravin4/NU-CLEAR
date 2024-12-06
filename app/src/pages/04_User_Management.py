import logging
import pandas as pd

import requests
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Manage Users")

url = f'http://api:4000/adm/user_permissions'

def clear_text():
  st.session_state["text1"] = ''
  st.session_state["text4"] = ''

# popover to add a new permission type
with st.popover("Add a new user", help=None, icon=None, disabled=False, use_container_width=True):
    userType = st.selectbox("User Type:", 
                            ('SystemAdmin', 'Student', 'Advisor',
                             'Employer', 'DataAnalyst'), key="text3")
    
    if st.button("Add", on_click=clear_text):
        filters = {
            "userType": userType,
        }
        requests.post(url, json=filters)
        
with st.popover("Delete a user", help=None, icon=None, disabled=False, use_container_width=True):
    userId = st.text_input("User Id:", key="text4")
    if st.button("Delete", on_click=clear_text):
        filters = {
            "userId": userId
        }
        requests.delete(url, json=filters)

# popover to update permission
with st.popover("Update a permission", help=None, icon=None, disabled=False, use_container_width=True):
    userType = st.selectbox("User Type:", 
                            ('SystemAdmin', 'Student', 'Advisor',
                             'Employer', 'DataAnalyst'))
    
    ## create perms
    canCreateReview = st.selectbox('Able to create a review?', (0, 1), key="box1")
    canCreateCoopListing = st.selectbox('Able to create a co-op listing?', (0, 1), key="box2")
    canCreateModule = st.selectbox('Able to create a module?', (0, 1), key="box3")
    
    ## edit perms
    canEditPerms = st.selectbox('Able to edit permissions?', (0, 1), key="box4")
    canEditModule = st.selectbox('Able to edit modules?', (0, 1), key="box5")
    canEditAccSettings = st.selectbox('Able to edit account settings?', (0, 1), key="box6")
   
    ## view perms
    canViewReview = st.selectbox('Able to view a review?', (0, 1), key="box7")
    canViewCoopListing = st.selectbox('Able to view a co-op listing?', (0, 1), key="box8")
    canViewModule = st.selectbox('Able to view a module?', (0, 1), key="box9")
    
    ## delete perms
    canDeleteReview = st.selectbox('Able to delete a review?', (0, 1), key="box10")
    canDeleteCoopListing = st.selectbox('Able to delete a co-op listing?', (0, 1), key="box11")
    canDeleteModule = st.selectbox('Able to delete a module?', (0, 1), key="box12")
    
    if st.button("Update", on_click=clear_text):
        filters = {
            "userType": userType,
            "canEditPerms": canEditPerms,
            "canEditModule": canEditModule,
            "canEditAccSettings": canEditAccSettings,
            "canCreateReivew": canCreateReview,
            "canCreateCoopListing": canCreateCoopListing,
            "canCreateModule": canCreateModule,
            "canViewReview": canViewReview,
            "canViewCoopListing": canViewCoopListing,
            "canViewModule": canViewModule,
            "canDeleteReview": canDeleteReview,
            "canDeleteCoopListing": canDeleteCoopListing,
            "canDeleteModule": canDeleteModule
        }
        requests.put(url, json=filters)

results = requests.get(url, params=None).json()
logger.info(results)

st.dataframe(results)