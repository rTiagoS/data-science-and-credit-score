
# Libs
import streamlit as st

from modules import intro, dashboard


# TO DO:
# 1. Put options into a "PAGES" variable. 

# Set page title and favicon
st.set_page_config(page_title = 'Credit Scoring Project', page_icon = "", layout="wide", initial_sidebar_state="expanded")

PAGES = [
    "About the Project",
    "Credit Score Intro",
    "Credit Score Dashboard",
    "Credit Score Model",
    "Credit Score Pipeline",
    "About me"
    
]

def main():
    
    # Dashboard
    abstract_text = st.markdown(get_file_content_as_string("markdowns/abstract/abstract_p0.md"))

    # Add an app mode in the sidebar.
    st.sidebar.title("Explore Around")

    app_mode = st.sidebar.radio('Navigation', PAGES)
    
    if app_mode == "Credit Score Intro":
        abstract_text.empty()
        intro.run_app()
    
    elif app_mode == 'Credit Score Dashboard':
        abstract_text.empty()
        dashboard.run_app()
    
    elif app_mode == 'About the Project':
        abstract_text.empty()
        st.markdown(get_file_content_as_string("markdowns/About the Project.md"))

    elif app_mode == 'Credit Score Model':
        abstract_text.empty()
        st.markdown(get_file_content_as_string("markdowns/Credit Score Model.md"))
    
    elif app_mode == 'Credit Score Pipeline':
        abstract_text.empty()
        st.markdown(get_file_content_as_string("markdowns/Credit Score Pipeline.md"))

    elif app_mode == 'About me':
        abstract_text.empty()
        st.markdown(get_file_content_as_string("markdowns/About me.md"))

        


def get_file_content_as_string(path):
    with open(path, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    return text


if __name__ == '__main__':
    main()