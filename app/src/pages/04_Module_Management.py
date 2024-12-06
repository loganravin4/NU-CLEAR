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

# search for a module
search = st.text_input("Search for a module...", "")
button_clicked = st.button("OK")

# popover to add a new module
st.popover("Assign a new module", help=None, icon=None, disabled=False, use_container_width=False)

results = requests.get('http://api:4000/adm/modules').json()

## dummy dataframe view for now bc endpoint for modules hasn't been tested yet
df = pd.DataFrame(results)
print(results)

st.dataframe(df, use_container_width=True)