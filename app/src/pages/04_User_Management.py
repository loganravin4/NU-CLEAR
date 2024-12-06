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

url = 'http://api:4000/announcements/'
  
response = requests.get(url)
logger.info(response)

## dummy dataframe view for now bc endpoint for users hasn't been tested yet
df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

st.dataframe(df, use_container_width=True)