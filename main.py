
# Libs
import streamlit as st

from modules import intro, dashboard


# TO DO:
# 1. Put options into a "PAGES" variable. 

# Set page title and favicon
st.set_page_config(page_title = 'Credit Scoring Project', page_icon = "", layout="wide", initial_sidebar_state="expanded")

PAGES = [
    "An Intro",
    "Dashboard",
    "My Credit Score",
    "Pipeline",
    "About"
]

def main():
    
    # Dashboard
    abstract_text = st.markdown(get_file_content_as_string("markdowns/abstract/abstract_p0.md"))

    # Add an app mode in the sidebar.
    st.sidebar.title("Explore Around")

    app_mode = st.sidebar.radio('Navigation', PAGES)
    
    if app_mode == "An Intro":
        abstract_text.empty()
        intro.run_app()
    
    elif app_mode == 'Dashboard':
        abstract_text.empty()
        dashboard.run_app()
        


def get_file_content_as_string(path):
    with open(path, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    return text


if __name__ == '__main__':
    main()