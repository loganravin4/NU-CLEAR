# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home")


def AboutPageNav():
    st.sidebar.page_link("pages/About.py", label="About")


#### ------------------------ Employer Role ------------------------
def EmployerHomeNav():
    st.sidebar.page_link("pages/00_Employer_Home.py", label="Employer Home")

    st.sidebar.page_link("pages/00_My_Company.py", label="My Company")

    st.sidebar.page_link("pages/00_Compare_Company.py", label="Other Companies")

    st.sidebar.page_link("pages/00_Summary_Review.py", label="Overall Reviews")


#### ------------------------ Data Analyst Role ------------------------
def DataAnalystHomeNav():
    st.sidebar.page_link("pages/01_Data_Analyst_Home.py", label="Data Analyst Home")

    st.sidebar.page_link("pages/01_Summary_Report.py", label="Add Summary Report")

    st.sidebar.page_link("pages/01_Coop_Review_by_Demographic.py", label = "Coop Reviews by Demographics")

    st.sidebar.page_link("pages/01_Add_Visualizations.py", label = "Add Visualizations")


#### ------------------------ Student Role ------------------------
def StudentHomeNav():
    st.sidebar.page_link("pages/02_Student_Home.py", label="Student Home")

    st.sidebar.page_link("pages/02_Coop_Reviews.py", label="View Co-op Reviews")
 
    st.sidebar.page_link("pages/02_Create_Review.py", label="Create a Review")

    st.sidebar.page_link("pages/02_User_Reviews.py", label="User Reviews")

    st.sidebar.page_link("pages/02_Favorited_Jobs.py", label="Favorited Jobs")

 
#### ------------------------ Advisor Role ------------------------
def AdvisorHomeNav():
    st.sidebar.page_link("pages/03_Advisor_Home.py", label="Advisor Home")


    st.sidebar.page_link("pages/03_Advisor_Student_Dashboard.py", label="Student Dashboard")

    st.sidebar.page_link("pages/02_Coop_Reviews.py", label="Co-op Reviews")

    st.sidebar.page_link("pages/03_Student_Recs.py", label="Recommend Co-ops")

    st.sidebar.page_link("pages/03_Make_and_Delete_Announcements.py", label="Delete Announcements")
 
#### ------------------------ System Admin Role ------------------------
def AdminPageNav():
    st.sidebar.page_link("pages/04_Admin_Home.py", label="System Admin")

    st.sidebar.page_link("pages/04_User_Management.py", label="Manage User Permissions")

    st.sidebar.page_link("pages/04_Module_Management.py", label="Manage Modules") 

    st.sidebar.page_link("pages/04_Add_Coop_Listing.py", label="Publish a Co-op listing")
    
# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width=200)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    # Always show
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
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")