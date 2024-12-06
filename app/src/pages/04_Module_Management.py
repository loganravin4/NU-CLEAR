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

# popover to add a new module
with st.popover("Assign a new module", help=None, icon=None, disabled=False, use_container_width=False):
    moduleName = st.text_input("Module Name:")
    createdBy = st.text_input("System Admin Id")
    if st.button("Assign"):
        filters = {
            "moduleName": moduleName,
            "moduleStatus": 'pending',
            "createdBy": createdBy
        }
        requests.post(url, json=filters)

results = requests.get(url).json()

df = pd.DataFrame(results)

st.dataframe(df, use_container_width=True)