import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

SideBarLinks()

st.title("See a Student\'s Favorited Co-ops")

user_id = st.text_input("Enter the Student ID", placeholder="e.g., 123")

if user_id:
    url = f"http://api:4000/coop/favorites/{user_id}"
    response = requests.get(url).json()

    if response:
        st.subheader("Favorited Co-ops")
        st.dataframe(response)

    else:
        st.warning("The student hasn't favorited any co-ops yet!")