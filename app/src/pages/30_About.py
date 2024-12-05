import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About this App")

st.markdown (
    """
    Every year, thousands of Northeastern students take on co-op placements, 
    yet the feedback system does not give students, employers, or advisors the 
    insights they need. As a result, students struggle with limited information, 
    employers lack guidance to improve their programs, and advisors can not access
    real-time data to support students effectively. Meet NU CLEAR, a data-driven 
    application designed to transform the way Northeastern students, advisors, and 
    co-op employers engage with the acclaimed experiential learning initiative. 
    """
)

st.markdown (
    """
    CLEAR collects, analyzes, and presents detailed co-op feedback, allowing students to 
    review co-ops and access other peer insights, helping employers improve their programs, 
    and providing advisors with real-time data to supplement their guidance—all in one place.
    Unlike basic surveys or feedback forms, CLEAR is a centralized solution that offers 
    personalized dashboards for administrators needing a high-level view of program impact, 
    as well as students looking for peer-to-peer co-op reviews and anonymous feedback to employers 
    to provide movement for change. This platform is not just gathering data; it is contextualizing it 
    to reveal the bigger picture, making experiential learning at Northeastern more transparent, informed, and impactful.
"""
        )
