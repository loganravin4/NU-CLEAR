import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()  

st.title('Add Visualization Report')


company_id = st.text_input("Company ID")
visualization_type = st.text_input("Visualization Type")
filters = st.text_input("Filters")
created_by = st.text_input("Created By (Data Analyst ID)")
 
  


if st.button("Add Visualization"):
    if not all([company_id, visualization_type, filters, created_by]):
        st.error("All required fields must be filled!")
    else:
        data = {
            "vizType": visualization_type,
            'filters': filters,
            "createdBy": created_by
        }

    
        api = f'http://api:4000/rev/analysis/visualization/{company_id}'
        response = requests.post(api, json=data)


    if response.status_code == 200:
        st.success("Visualization added succesfully!")
    else:
        st.error(f"Failed to add visualization. Error: {response.status_code} - {response.text}")
 

