import streamlit as st

def run_app():

    topic_chosen = st.sidebar.selectbox("Select a topic",
                                        ["Summary",
                                         "Concepts",
                                         "Reasons",
                                         "Modeling"])

    if topic_chosen == "Summary":
        st.empty()
        run_intro_screen()

    elif topic_chosen == "Concepts":
        st.empty()
        run_topic_1_screen()

    elif topic_chosen == "Reasons":
        st.empty()
        run_topic_2_screen()
    
    elif topic_chosen == "Modeling":
        st.empty()
        run_topic_3_screen()

    return None    

def run_intro_screen():

    intro_p0 = st.markdown(get_file_content_as_string("markdowns/intro/intro_p0.md"), unsafe_allow_html=True)

    _, col2, _ = st.columns(3)

    col2.image("figures/intro/credit_score.jpg", caption = "Illustrative picture. (Font: Flickr)", width = 600)

    intro_p1 = st.markdown(get_file_content_as_string("markdowns/intro/intro_p1.md"))

def run_topic_1_screen():
    
    # Topic 1 - Part 0 
    st.markdown(get_file_content_as_string("markdowns/intro/t1_p0.md"))

    _, col2, _ = st.columns(3)

    col2.image("figures/intro/BorrowerVsLender.png", width = 500, caption = 'Basic lending illustration. (Icons from Noun Project)')

    
    # Topic 1 - Part 1 
    st.markdown(get_file_content_as_string("markdowns/intro/t1_p1.md"))

    col1, col2, _, _ = st.columns(4)
    col2.image("figures/intro/debt.png", width = 700, caption = "Illustrative picture. Central ideia: Money being sucked in by borrowing fees. (Font: Flickr)")
    
    # Topic 1 - Part 2 
    st.markdown(get_file_content_as_string("markdowns/intro/t1_p2.md"))


    col1, col2, _, _ = st.columns(4)
    col2.image("figures/intro/numbers.jpg", width = 700, caption = "Illustrative picture. (Font: Flickr)")

    # Topic 1 - Part 3
    st.markdown(get_file_content_as_string("markdowns/intro/t1_p3.md"))

    return None

def run_topic_2_screen():

    st.markdown(get_file_content_as_string("markdowns/intro/t2_p0.md"))

    col1, col2, _, _ = st.columns(4)
    col2.image("figures/intro/2008.jpg", width = 600, caption = "2008 Financial Crisis - Consequences. (Font: The Balance)")

    st.markdown(get_file_content_as_string("markdowns/intro/t2_p1.md"))

def run_topic_3_screen():

    st.markdown(get_file_content_as_string("markdowns/intro/t3_p0.md"))

    # st.image("figures/intro/2008.jpg")

    st.markdown(get_file_content_as_string("markdowns/intro/t3_p1.md"))

    # st.image("figures/intro/2008.jpg")

    st.markdown(get_file_content_as_string("markdowns/intro/t3_p2.md"))


def get_file_content_as_string(path):
    with open(path, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    return text

    