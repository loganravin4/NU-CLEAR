import logging
import pandas as pd

import requests
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Manage Modules")

url = f'http://api:4000/adm/modules'

def clear_text():
  st.session_state["text1"] = ''
  st.session_state["text2"] = ''

# popover to add a new module
with st.popover("Assign a new module", help=None, icon=None, disabled=False, use_container_width=False):
    moduleName = st.text_input("Module Name:", key="text1")
    createdBy = st.text_input("System Admin Id", key="text2")
    moduleStatus = st.selectbox('Module Status', ('active', 'inactive'))
    
    logger.info(f'moduleName = {moduleName}')
    logger.info(f'createdBy = {createdBy}')
    logger.info(f'moduleStatus = {moduleStatus}')

    filters = {
            "moduleName": moduleName,
            "moduleStatus": moduleStatus,
            "createdBy": createdBy
    }
    if st.button("Assign"):
            requests.post(url, json=filters)
            results = requests.get(url).json()

results = requests.get(url).json()

if st.button("Refresh"):
    results = requests.get(url).json()

df = pd.DataFrame(results)

st.dataframe(df, use_container_width=True)