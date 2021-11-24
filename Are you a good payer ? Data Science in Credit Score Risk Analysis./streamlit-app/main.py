
# Libs
import streamlit as st

from modules import intro

# Set page title and favicon
st.set_page_config(page_title = 'Credit Scoring Project', page_icon = "", layout="wide")


def main():
    
    # Dashboard
    abstract_text = st.markdown(get_file_content_as_string("markdowns/abstract/abstract_p0.md"))

    # Add an app mode in the sidebar.
    st.sidebar.title("Explore Around")

    app_mode = st.sidebar.selectbox("Choose an app mode",
                                    [   
                                        "An Intro",
                                        "Dashboard",
                                        "My Credit Score",
                                        "Pipeline",
                                        "About"
                                    ])
    
    if app_mode == "An Intro":
        abstract_text.empty()
        intro.run_app()


def get_file_content_as_string(path):
    with open(path, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    return text


if __name__ == '__main__':
    main()