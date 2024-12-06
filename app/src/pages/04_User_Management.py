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

# search for a module
search = st.text_input("Search for a user by name...", "")
button_clicked = st.button("OK")

results = requests.get('http://api:4000/adm/user_permissions').json()

df = pd.DataFrame(results)

logger.info(results)

st.dataframe(df, use_container_width=True)