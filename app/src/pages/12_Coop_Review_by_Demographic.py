import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Filter Reviews by Student Demographics')

coopLevel_options = ['All', 1, 2] 
coopLevel_input = st.selectbox('Select Student Co-op Level(Optional):', coopLevel_options)

year_options = ['All', 1, 2,3,4,5] 
year_input = st.selectbox('Select Student Year (Optional):', year_options)


major_input = st.text_input('Enter Major (Optional):', '')

 
if st.button('Filter Reviews'):
    params = {}
    if coopLevel_input != 'All':
        params['coopLevel'] = coopLevel_input
    if major_input:
        params['major'] = major_input
    if year_input:
        params['year'] = year_input

    url = 'http://api:4000/rev/reviews'  
    response = requests.get(url, params=params)
        
    if response.status_code == 200:
        reviews = response.json() 
        if reviews:
            st.write(f"Found {len(reviews)} reviews")
            if coopLevel_input != 'All':
                st.write(f"Filtered by coopLevel: {coopLevel_input}")
            if major_input:
                st.write(f"Filtered by Major: {major_input}")
            if year_input:
                st.write(f"Filtered by Year: {year_input}")
            st.write(":")
            for review in reviews:
                st.write(f"Review ID: {review['reviewId']}")
                st.write(f"Role: {review['role']}")
                st.write(f"Salary: {review['salary']}")
                st.write(f"Rating: {review['rating']}")
                st.write(f"Summary: {review['summary']}")
                st.write(f"Student: {review['firstName']} {review['lastName']}")
                st.write(f"Major: {review['major']}")
                st.write(f"Year: {review['year']}")
                st.write("----")
        else:
            st.write("No reviews found for the specified filters.")
    else:
        st.write("Error fetching data. Please try again later.")

