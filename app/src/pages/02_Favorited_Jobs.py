import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

SideBarLinks()

st.title("Your Favorited Co-ops")

user_id = st.text_input("Enter your User ID", placeholder="e.g., 123")

if user_id:
    url = f"http://api:4000/coop/favorites/{user_id}"
    response = requests.get(url).json()

    if response:
        st.subheader("Favorited Co-ops")
        st.dataframe(response)

        coop_id_to_delete = st.text_input("Enter the Co-op ID to remove from favorites", placeholder="e.g., 45")

        if st.button("Remove from Favorites", type="primary", use_container_width=True):
            if coop_id_to_delete:
                delete_url = f"http://api:4000/coop/favorites/{user_id}"
                delete_response = requests.delete(delete_url, json={"coopId": coop_id_to_delete})

                if delete_response.status_code == 200:
                    st.success("Co-op removed from favorites successfully!")
                    response = requests.get(url).json()
                    if response:
                        st.dataframe(response)
                    else:
                        st.warning("You haven't favorited any co-ops yet!")
                else:
                    st.error(f"Failed to remove co-op. Error: {delete_response.text}")
            else:
                st.error("Please enter a Co-op ID to remove.")
    else:
        st.warning("You haven't favorited any co-ops yet!")