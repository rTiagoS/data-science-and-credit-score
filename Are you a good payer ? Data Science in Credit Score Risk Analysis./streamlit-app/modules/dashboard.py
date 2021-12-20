import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



from modules import mysql


def run_app():
    # TO DO
    # Insert github logo and link.
    st.markdown("# Credit Score")
    st.markdown("### Dashboard")
    st.markdown("---")

    html_card_header1 = get_html_card('html_card_header1')
    html_card_header2 = get_html_card('html_card_header2')
    html_card_header3 = get_html_card('html_card_header3')

    html_card_footer1 = get_html_card('html_card_footer1')
    html_card_footer2 = get_html_card('html_card_footer2')
    html_card_footer3 = get_html_card('html_card_footer3')

    

    

    with st.container():
        col1, col2, col3, col4, col5, col6, col7 = st.columns([1,15,1,15,1,15,1])

        with col1:
            st.write("")

        with col2:
            st.markdown(html_card_header1, unsafe_allow_html=True)
            st.plotly_chart(kpi_up_left())
            st.markdown(html_card_footer1, unsafe_allow_html=True)

        with col3:
            st.write("")
        with col4:
            st.markdown(html_card_header2, unsafe_allow_html=True)
            
            st.plotly_chart(kpi_up_middle())
            st.markdown(html_card_footer2, unsafe_allow_html=True)
        with col5:
            st.write("")
        with col6:
            st.markdown(html_card_header3, unsafe_allow_html=True)
            fig_c3 = go.Figure(go.Indicator(
                mode="number+delta",
                value=1.085,
                number={"font": {"size": 40, 'color': "#008080", 'family': "Arial"}},
                delta={'position': "bottom", 'reference': 1, 'relative': False},
                domain={'x': [0, 1], 'y': [0, 1]}))
            fig_c3.update_layout(autosize=False,
                                width=350, height=90, margin=dict(l=20, r=20, b=20, t=30),
                                paper_bgcolor="#E4FDF6", font={'size': 20})
            fig_c3.update_traces(delta_decreasing_color="#3D9970",
                                delta_increasing_color="#FF4136",
                                delta_valueformat='.3f',
                                selector=dict(type='indicator'))
            st.plotly_chart(fig_c3)
            st.markdown(html_card_footer3, unsafe_allow_html=True)
        with col7:
            st.write("")

        st.write("")

        st.plotly_chart(bar_chart_by_grade())

        st.write("")
        
        #st.plotly_chart(hist_chart_by_loan_status())
        
        st.pyplot(hist_plot_3())

    

    #st.write(f"Resultado: {result}")


def kpi_up_left():

    mysql_client = mysql.MyDB()

    query = """
            SELECT
                COUNT(DISTINCT(member_id)) AS count_members
            FROM
                `LendingClub`.`src_loan_data_2007_2014`;
            """

    nr_members = int(mysql_client.mysql_execute_query(query)[0][0])

    fig_c1 = go.Figure(go.Indicator(
                mode="number+delta",
                value=nr_members,
                number={'suffix': "", "font": {"size": 40, 'color': "#008080", 'family': "Arial"}},
                delta={'position': "bottom", 'reference': 400000, 'relative': True},
                domain={'x': [0, 1], 'y': [0, 1]}))
    fig_c1.update_layout(autosize=False,
                         width=350, height=90, margin=dict(l=20, r=20, b=20, t=30),
                         paper_bgcolor="#E4FDF6", font={'size': 20})
    return fig_c1

def kpi_up_middle():

    mysql_client = mysql.MyDB()

    query = """
            SELECT
                COUNT(*)
            FROM
                `LendingClub`.`src_loan_data_2007_2014` t1
            WHERE
                t1.loan_status IN(
                    SELECT
                        loan_status
                    FROM
                        `LendingClub`.`src_loan_data_2007_2014`
                    WHERE
                        loan_status IN ('Charged Off', 'Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)')
                )
            """
    nr_bad_payers = int(mysql_client.mysql_execute_query(query)[0][0])

    fig_c2 = go.Figure(go.Indicator(
                mode="number+delta",
                value=nr_bad_payers,
                number={'suffix': "", "font": {"size": 40, 'color': "#008080", 'family': "Arial"}, 'valueformat': ',f'},
                delta={'position': "bottom", 'reference': 10000},
                domain={'x': [0, 1], 'y': [0, 1]}))
    fig_c2.update_layout(autosize=False,
                                width=350, height=90, margin=dict(l=20, r=20, b=20, t=30),
                                paper_bgcolor="#E4FDF6", font={'size': 20})
    fig_c2.update_traces(delta_decreasing_color="#3D9970",
                                delta_increasing_color="#FF4136",
                                delta_valueformat='f',
                                selector=dict(type='indicator'))


    return fig_c2

def kpi_up_right():
    pass

def bar_chart_by_grade():
    
    mysql_client = mysql.MyDB()

    query = """
            
            SELECT
                t1_0.grade,
                nr_bad_clients,
                nr_good_clients
            FROM(
            (SELECT
                COUNT(DISTINCT(member_id)) AS nr_bad_clients,
                grade
            FROM
                `LendingClub`.`src_loan_data_2007_2014` t1
            WHERE
                t1.loan_status IN ('Charged Off', 'Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)')
            GROUP BY
                grade) t1_0

            LEFT JOIN

            (SELECT
                COUNT(DISTINCT(member_id)) AS nr_good_clients,
                grade
            FROM
                `LendingClub`.`src_loan_data_2007_2014` t2
            WHERE
                t2.loan_status NOT IN ('Charged Off', 'Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)')
            GROUP BY
                grade) t2_0
            ON
                t1_0.grade = t2_0.grade
            )
            
            """
    query_results = mysql_client.mysql_execute_query(query)

    grade       = []
    good_payers = []
    bad_payers  = []

    for res in query_results:
        grade.append(res[0])
        bad_payers.append(res[1])
        good_payers.append(res[2])

    good_payers = [round(100*x/sum(good_payers)) for x in good_payers]
    bad_payers  = [round(100*x/sum(bad_payers)) for  x in bad_payers]

    fig = go.Figure()

    fig.add_trace(go.Bar(x = grade,
                         y = good_payers,
                         name = 'Good Payers',
                         marker_color = 'rgb(55, 83, 109)'
                         ))
    fig.add_trace(go.Bar(x = grade,
                         y = bad_payers,
                         name = 'Bad Payers',
                         marker_color = 'rgb(26, 118, 255)'
                         ))
    fig.update_layout(
        title = 'Distribution of Bad Payers and Good Payers over Grade',
        xaxis_tickfont_size = 14,
        yaxis = dict(
                    title = 'Amount',
                    titlefont_size = 16,
                    tickfont_size = 14
                    ),
        legend = dict(x = 0.8, y = 1.0, bgcolor = 'rgba(255, 255, 255, 0)', bordercolor = 'rgba(255, 255, 255, 0)'),
        barmode = 'group',
        bargap = 0.15,
        bargroupgap = 0.1
    )

    

    return fig

def hist_chart_by_loan_status():

    

    query_good_payers = """
                        SELECT
                            loan_amnt AS good_payers_loan_amnt
                        FROM
                            `LendingClub`.`src_loan_data_2007_2014` t2
                        WHERE
                            t2.loan_status NOT IN ('Charged Off', 'Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)')
                        LIMIT 100	
                        """
    query_bad_payers ="""
                        SELECT
                            loan_amnt AS bad_payers_loan_amnt
                        FROM
                            `LendingClub`.`src_loan_data_2007_2014` t2
                        WHERE
                            t2.loan_status IN ('Charged Off', 'Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)')
                        LIMIT 100
                      """
    mysql_client = mysql.MyDB()
    query_results_gp = mysql_client.mysql_execute_query(query_good_payers)

    query_results_bd = mysql_client.mysql_execute_query(query_bad_payers)
    
    # Histogram Data 
    good_payers_loan_amnt = []
    bad_payers_loan_amnt  = []

    for res in query_results_gp:
        good_payers_loan_amnt.append(int(res[0]))

    for res in query_results_bd:
        bad_payers_loan_amnt.append(int(res[0]))

    # Group data together
    hist_data = [good_payers_loan_amnt, bad_payers_loan_amnt]

    group_labels = ['Good Payers', 'Bad Payers']

    # Create displot
    fig = ff.create_distplot(hist_data, group_labels, bin_size = 5)

    return fig

def hist_2():
        

    query_good_payers = """
                        SELECT
                            loan_amnt AS good_payers_loan_amnt
                        FROM
                            `LendingClub`.`src_loan_data_2007_2014` t2
                        WHERE
                            t2.loan_status NOT IN ('Charged Off', 'Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)')
                        LIMIT 2000	
                        """
    query_bad_payers ="""
                        SELECT
                            loan_amnt AS bad_payers_loan_amnt
                        FROM
                            `LendingClub`.`src_loan_data_2007_2014` t2
                        WHERE
                            t2.loan_status IN ('Charged Off', 'Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)')
                        LIMIT 2000
                      """
    mysql_client = mysql.MyDB()
    query_results_gp = mysql_client.mysql_execute_query(query_good_payers)

    query_results_bd = mysql_client.mysql_execute_query(query_bad_payers)
    
    # Histogram Data 
    good_payers_loan_amnt = []
    bad_payers_loan_amnt  = []

    for res in query_results_gp:
        good_payers_loan_amnt.append(int(res[0]))

    for res in query_results_bd:
        bad_payers_loan_amnt.append(int(res[0]))

    # penguins = sns.load_dataset("penguins")

    # fig = sns.pairplot(penguins, hue = "species")

    fig = plt.figure(figsize=(10, 4))

    sns.histplot(data = pd.DataFrame(good_payers_loan_amnt, columns = ['gp_dist']), element = "step", stat = 'density', common_norm = True, alpha = 0.2, palette = 'bright', kde = True, bins = 25)

    return fig

def hist_plot_3():

    query="""
            SELECT
                *
            FROM(

            SELECT
                annual_inc,
                'Good Payers' AS label
            FROM
                `LendingClub`.`src_loan_data_2007_2014` t2
            WHERE
                t2.loan_status NOT IN ('Charged Off', 'Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)')
            ORDER BY
                RAND()
            LIMIT 10000
            ) AS A

            UNION ALL

            SELECT
                *
            FROM(
            SELECT
                annual_inc,
                'Bad Payers' AS label
            FROM
                `LendingClub`.`src_loan_data_2007_2014` t1
            WHERE
                t1.loan_status IN ('Charged Off', 'Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)')
            ORDER BY
                RAND()
            LIMIT 10000
            ) AS B
            """
    mysql_client = mysql.MyDB()
    query_results = mysql_client.mysql_execute_query(query)
    
    # Histogram Data 
    loan_amnt_  = []
    label_ = []

    for res in query_results:
        loan_amnt_.append(float(res[0]))
        label_.append(res[1])

    loan_data = pd.DataFrame(dict(loan_amnt = loan_amnt_, label = label_))

    fig = plt.figure(figsize=(10, 4))




    sns.histplot(data = loan_data[loan_data['loan_amnt'] < 200000], x = 'loan_amnt', hue = 'label',
     element = "step", stat = 'density', common_norm = True, alpha = 0.2, palette = 'bright', kde = True, bins = 50)

    return fig

def get_html_card(card):

    if card == 'html_card_header1':
        return """
                <div class="card">
                    <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ACC9C4; padding-top: 5px; width: 350px;height: 70px;">
                        <h4 class="card-title" style="background-color:#ACC9C4; color:#008080; font-family:Sans serif; text-align: center; padding: 0px 0;">Total Clients</h4>
                    </div>
                </div>
                """
         

    elif card == 'html_card_footer1':
        return """
                <div class="card">
                    <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #ACC9C4; padding-top: 1rem;; width: 350px;height: 50px;">
                            <p class="card-title" style="background-color:#ACC9C4; color:#008080; font-family:Sans serif; text-align: center; padding: 0px 0;">Baseline 400k</p>
                    </div>
                </div>
                """
        
    
    elif card == 'html_card_header2':
        return """
                <div class="card">
                    <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ACC9C4; padding-top: 5px; width: 350px;height: 70px;">
                        <h4 class="card-title" style="background-color:#ACC9C4; color:#008080; font-family:Sans serif; text-align: center; padding: 0px 0;">% Tot. Bad Payers</h4>
                    </div>
                </div>
                """
    
    elif card == 'html_card_footer2':
        return """
                <div class="card">
                    <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #ACC9C4; padding-top: 1rem;; width: 350px;height: 50px;">
                            <p class="card-title" style="background-color:#ACC9C4; color:#008080; font-family:Sans serif; text-align: center; padding: 0px 0;">Teste 46%</p>
                    </div>
                </div>
                """
    
    elif card == 'html_card_header3':
        return """
                <div class="card">
                    <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ACC9C4; padding-top: 5px; width: 350px;height: 70px;">
                        <h4 class="card-title" style="background-color:#ACC9C4; color:#008080; font-family:Sans serif; text-align: center; padding: 0px 0;">Total Losses $</h4>
                    </div>
                </div>
                """
    elif card == 'html_card_footer3':
        return """
                <div class="card">
                    <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #ACC9C4; padding-top: 1rem;; width: 350px;height: 50px;">
                            <p class="card-title" style="background-color:#ACC9C4; color:#008080; font-family:Sans serif; text-align: center; padding: 0px 0;">Teste 46%</p>
                    </div>
                </div>
                """