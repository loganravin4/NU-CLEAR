# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home")


def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About")


#### ------------------------ Employer Role ------------------------
def EmployerHomeNav():
    st.sidebar.page_link("pages/00_Employer_Home.py", label="Employer Home")


#### ------------------------ Data Analyst Role ------------------------
def DataAnalystHomeNav():
    st.sidebar.page_link("pages/01_Data_Analyst_Home.py", label="Data Analyst Home")


#### ------------------------ Student Role ------------------------
def StudentHomeNav():
    st.sidebar.page_link("pages/02_Student_Home.py", label="Student Home", icon="👤")



#### ------------------------ Advisor Role ------------------------
def AdvisorHomeNav():
    st.sidebar.page_link("pages/03_Advisor_Home.py", label="Advisor Home")


#### ------------------------ System Admin Role ------------------------
def AdminPageNav():
    st.sidebar.page_link("pages/04_Admin_Home.py", label="System Admin")


# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width=150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # Employer Role Pages
        if st.session_state["role"] == "employer":
            EmployerHomeNav()

        # Student Role Pages
        if st.session_state["role"] == "student":
            StudentHomeNav()
        
        # Data Analyst Role Pages
        if st.session_state["role"] == "data_analyst":
            DataAnalystHomeNav()
        
        # Advisor Role Pages
        if st.session_state["role"] == "advisor":
            AdvisorHomeNav()
        
        # Admin Role Pages
        if st.session_state["role"] == "administrator":
            AdminPageNav()

    # Always show
    HomeNav()
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")
