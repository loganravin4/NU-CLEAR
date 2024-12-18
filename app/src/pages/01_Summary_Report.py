import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()   

st.title('Add a Summary Report')


company_id = st.text_input("Company ID")
average_rating = st.text_input("Average Rating (out of 5)")
generated_summary = st.text_area("Generated Summary")
generated_by = st.text_input("Generated By (Data Analyst ID)")
updated_by = st.text_input("Updated By (If Updated)")  

 
if st.button("Add Summary"):
    if not all([company_id, average_rating, generated_summary, generated_by]):
        st.error("All required fields must be filled!")
    else:
        data = {
            "averageRating": average_rating,
            "generatedSummary": generated_summary,
            "generatedBy": generated_by,
        }


        if updated_by.strip():   
                data["updatedBy"] = updated_by

        api = f'http://api:4000/rev/analysis/summary_report/{company_id}'
        response = requests.post(api, json=data)

    if response.status_code == 200:
        st.success("Summary added succesfully!")
    else:
        st.error(f"Failed to add Summary. Error: {response.status_code} - {response.text}")
 