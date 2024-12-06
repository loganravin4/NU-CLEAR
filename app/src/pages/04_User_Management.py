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

results = requests.get(url, params=None).json()
logger.info(results)

st.dataframe(results)