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
updated_by = st.text_input("Updated By (If Updated)")  
 
  


if st.button("Add Visualization"):
    if not all([company_id, visualization_type, filters, created_by]):
        st.error("All required fields must be filled!")
    else:
        data = {
            "vizType": visualization_type,
            'filters': filters,
            "createdBy": created_by,
        } 
 
        if updated_by.strip():   
            data["updatedBy"] = updated_by

    
        api = f'http://localhost:4000/analysis/visualization/{company_id}'
        response = requests.post(api, json=data)
