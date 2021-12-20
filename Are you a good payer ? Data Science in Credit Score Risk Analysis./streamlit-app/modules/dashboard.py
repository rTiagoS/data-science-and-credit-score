import streamlit as st
import plotly.graph_objects as go


from modules import mysql

def get_html_card(card):

    if card == 'html_card_header1':
        html_card_header1=  """
                            <div class="card">
                                <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ACC9C4; padding-top: 5px; width: 350px;height: 70px;">
                                    <h4 class="card-title" style="background-color:#ACC9C4; color:#008080; font-family:Sans serif; text-align: center; padding: 0px 0;">Teste</h4>
                                </div>
                            </div>
                            """
        return html_card_header1

    elif card == 'html_card_footer1':
        html_card_footer1=  """
                            <div class="card">
                                <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #ACC9C4; padding-top: 1rem;; width: 350px;height: 50px;">
                                    <p class="card-title" style="background-color:#ACC9C4; color:#008080; font-family:Sans serif; text-align: center; padding: 0px 0;">Teste 46%</p>
                                </div>
                            </div>
                            """
        return html_card_footer1

def run_app():
    st.markdown("# Credit Score")
    st.markdown("### Dashboard")
    st.markdown("---")


    html_card_header1="""
                    <div class="card">
                    <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ACC9C4; padding-top: 5px; width: 350px;
                    height: 70px;">
                        <h4 class="card-title" style="background-color:#ACC9C4; color:#008080; font-family:Sans serif; text-align: center; padding: 0px 0;">Teste</h4>
                    </div>
                    </div>
                    """
from modules import mysql

    
    with st.container():
        col1, col2, col3, col4, col5, col6, col7 = st.columns([1,15,1,15,1,15,1])

        with col1:
            st.write("")

        with col2:
            st.markdown(html_card_header1, unsafe_allow_html=True)

            fig_c1 = go.Figure(go.Indicator(
                mode="number+delta",
                value=35,
                number={'suffix': "%", "font": {"size": 40, 'color': "#008080", 'family': "Arial"}},
                delta={'position': "bottom", 'reference': 46, 'relative': False},
                domain={'x': [0, 1], 'y': [0, 1]}))
            fig_c1.update_layout(autosize=False,
                                width=350, height=90, margin=dict(l=20, r=20, b=20, t=30),
                                paper_bgcolor="#E4FDF6", font={'size': 20})
            st.plotly_chart(fig_c1)
            st.markdown(html_card_footer1, unsafe_allow_html=True)

    mysql_client = mysql.MyDB()

    query = 'SELECT * FROM src_loan_data_2007_2014'

    result = mysql_client.mysql_execute_query(query)

    #st.write(f"Resultado: {result}")