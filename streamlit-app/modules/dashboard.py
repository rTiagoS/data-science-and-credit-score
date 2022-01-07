import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime
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
        
        col8, col9, col10 = st.columns([10,2,10])
        with col8:
            st.plotly_chart(bar_chart_by_grade())
        with col9:
            st.write("")
        
        with col10:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.pyplot(hist_chart_by_annual_inc())

        st.write("")
        
        # col11, col12, col13 = st.columns([10,2,10])

        # with col11:
        #     st.plotly_chart(geomap_chart())

        # with col12:
        #     st.write("")

        # with col13:
        #     st.plotly_chart(bar_chart_by_emp_length())
    
        st.plotly_chart(geomap_chart())

        st.write("")

        st.plotly_chart(bar_line_chart())


        

    

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
                         name = '<b>Good Payers</b>',
                         marker_color = 'rgb(0,100,0)' #darkblue
                         ))
    fig.add_trace(go.Bar(x = grade,
                         y = bad_payers,
                         name = '<b>Bad Payers</b>',
                         marker_color = 'rgb(139,0,0)' #darkred
                         ))
    fig.update_layout(
        title_text = '<b>Distribution of Bad Payers and Good Payers by Grade</b>',
        title_x = 0.5,
        title_y = 0.87,
        xaxis = dict(
                    title = '<b>Grade</b>',
                    titlefont_size = 16,
                    tickfont_size = 14
                    ),
        yaxis = dict(
                    title = '<b>Amount (%)</b>',
                    titlefont_size = 16,
                    tickfont_size = 14
                    ),
        font={
            "family": "Sans serif"},
        legend = dict(
                    x = 0.7, 
                    y = 1.0, 
                    bgcolor = 'rgba(255, 255, 255, 0)', 
                    bordercolor = 'rgba(255, 255, 255, 0)'
                    ),
        barmode = 'group',
        bargap = 0.15,
        bargroupgap = 0.1,

        width=750, height=510
        
        )
        
    return fig


def hist_chart_by_annual_inc():

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
    annual_inc  = []
    label_ = []

    for res in query_results:
        annual_inc.append(float(res[0]))
        label_.append(res[1])

    loan_data = pd.DataFrame(dict(annual_income = annual_inc, label = label_))
    with sns.axes_style(rc= {'axes.facecolor': '#ACC9C4',
                            'axes.edgecolor': '#008080',
                            'axes.grid': True,
                            'axes.axisbelow': 'line',
                            'axes.labelcolor': 'black',
                            'figure.facecolor': '#E4FDF6',
                            'grid.color': 'FFFFFF'
                            }):

        fig = plt.figure(figsize=(13, 8))
        plt.title('Annual Income Histogram by Payer Label', fontweight = 'bold', fontsize = 20)
        plt.xlabel('Annual Income ($)', fontsize = 18, fontweight = 'bold')
        plt.ylabel("Frequency (%)", fontsize = 18, fontweight = 'bold')
        sns.histplot(data = loan_data[loan_data['annual_income'] < 200000], x = 'annual_income', hue = 'label',
        element = "step", stat = 'percent', common_norm = True, alpha = 0.5, kde = True, bins = 40, palette={"Good Payers": "#006400", "Bad Payers": "darkred"})

    
    return fig

def geomap_chart():

    query = """
    SELECT
        addr_state,
        COUNT(loan_status) AS count_loan_status
    FROM
        `src_loan_data_2007_2014`

    WHERE
        loan_status IN ('Charged Off', 'Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)')
        
    GROUP BY
        addr_state
            """

    mysql_client = mysql.MyDB()

    query_results = mysql_client.mysql_execute_query(query)

    # Histogram Data 
    count_loan_status  = []
    addr_state = []

    for res in query_results:
        addr_state.append(res[0])
        count_loan_status.append(res[1])

    df = pd.DataFrame(dict(states = addr_state, nr_of_bad_payers = count_loan_status))
    
    fig = go.Figure(
                    data=go.Choropleth(
                                        locations = df['states'], # spatial coordinates
                                        z = df['nr_of_bad_payers'],
                                        locationmode = 'USA-states', # set of locations match entries in 'locations',
                                        colorscale = 'Reds',
                                        colorbar_title = "<b>Defaulters amount scale</b>",
                                        showscale = True
                                        )
                    )

    fig.update_layout(
                        geo=dict(bgcolor= 'rgba(0,0,0,0)'),
                        geo_scope='usa', # limite map scope to USA
                        title_text = '<b>Defaulters amount per state in USA</b>',
                        title_x = 0.5,
                        title_y = 0.98,
                        font={"family": "Sans serif"},
                        width=1300,
                        height=500,
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        
                )
    # fig.update_layout(coloraxis_colorbar_x=0.1)

    # fig.update_yaxes(automargin=True)
    # fig.update_xaxes(automargin=True)

    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return fig


def bar_chart_by_isse_d():

    query = """
            SELECT
                emp_length,
                'bad payer' AS payer_status

            FROM
                `src_loan_data_2007_2014`
            WHERE
                loan_status IN ('Charged Off', 'Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)')

            UNION ALL

            SELECT
                emp_length,
                'good payer' AS payer_status

            FROM
                `src_loan_data_2007_2014`
            WHERE
                loan_status NOT IN ('Charged Off', 'Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)')

            """

    mysql_client = mysql.MyDB()

    query_results = mysql_client.mysql_execute_query(query)

    emp_length  = []
    payer_status = []

    for res in query_results:
        emp_length.append(res[0])
        payer_status.append(res[1])

    df = pd.DataFrame(dict(Employe_Length = emp_length, Payer_Status = payer_status))

    fig = go.Figure()

    teste_1 = df[df['Payer_Status'] == 'good payer'].groupby(['Employe_Length'])['Payer_Status'].count().reset_index()

    # st.dataframe(teste_1)
    
    teste_2 = df[df['Payer_Status'] == 'bad payer'].groupby(['Employe_Length'])['Payer_Status'].count().reset_index()

    fig.add_trace(go.Bar(x = teste_1['Employe_Length'],
                         name = 'Good Payers',
                         y = teste_1['Payer_Status']/teste_1['Payer_Status'].sum(),
                         marker_color = 'rgb(55, 83, 109)'
                         ))
    fig.add_trace(go.Bar(x = teste_2['Employe_Length'],
                         name = 'Bad Payers',
                        y = teste_2['Payer_Status']/teste_2['Payer_Status'].sum(),
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
    
# @st.cache
def bar_line_chart():

    query = """
            
            SELECT
                issue_d,
                'bad payer' AS payer_status

            FROM
                `src_loan_data_2007_2014`
            WHERE
                loan_status IN ('Charged Off', 'Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)')

            UNION ALL

            SELECT
                issue_d,
                'good payer' AS payer_status

            FROM
                `src_loan_data_2007_2014`
            WHERE
                loan_status NOT IN ('Charged Off', 'Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)')

            """

    mysql_client = mysql.MyDB()

    query_results = mysql_client.mysql_execute_query(query)

    issue_d = []
    payer_status = []

    for res in query_results:
        issue_d.append(res[0])
        payer_status.append(res[1])

    df = pd.DataFrame(dict(issue_date=issue_d, payer_label = payer_status))

    df['issue_date'] = pd.to_datetime(df['issue_date'], format = "%b-%y")
    df['month'] = df.issue_date.dt.strftime('%b')
    df['year'] = df.issue_date.dt.strftime('%Y')

    months = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()

    
    df_1 = df.groupby(['month', 'year'])['payer_label'].count().reset_index().sort_values(by=['year'], ascending = True)

    df_2 = df.groupby(['month', 'year', 'payer_label']).count().reset_index().sort_values(by=['year'], ascending = True)

    df_2['month'] =  pd.Categorical(df_2['month'], categories = months, ordered = True)
    df_2 = df_2.sort_values(by=['year', 'month'], ascending = True)
    d = df_2[df_2['payer_label'] == 'bad payer'].reset_index(drop = True)
    l = df_2[df_2['payer_label'] == 'good payer'].reset_index(drop=True)
    d.drop(['month', 'year','payer_label'], axis = 1, inplace = True)
    l.drop(['month', 'year','payer_label'], axis = 1, inplace = True)
    d.columns = ['bad_payer_issue']
    l.columns = ['good_payer_issue']


    c = pd.concat([l,d], axis=1)

    df_1['month'] = pd.Categorical(df_1['month'], categories = months, ordered = True)
    df_1 = df_1.reset_index(drop=True)
    df_1 = df_1.sort_values(by=['year', 'month'], ascending = True)

    df_1 = pd.concat([df_1, c], axis = 1)

    years = list(df_1.year.unique())
    
    col1, col2, col3, col4, col5 = st.columns([1,6,6,3,3])

    with col1:
        st.write("")
    with col2:
        year_chosen = st.selectbox('Select the year:', years)
    with col3:
        st.write("")
    with col4:
        st.write("")
    with col5:
        st.write("")
   

    fig = go.Figure()

    
    fig.add_trace(
                    go.Bar(
                            x = df_1[df_1['year'] == year_chosen]['month'],
                            y = df_1[(df_1['year'] == year_chosen)]['good_payer_issue'],
                            name = 'Good Payers Issues Amount',
                            marker_color = 'rgb(0,100,0)'
                        )   
                )
    fig.add_trace(
                     go.Bar(
                                x = df_1[df_1['year'] == year_chosen]['month'],
                                y = df_1[(df_1['year'] == year_chosen)]['bad_payer_issue'],
                                name = 'Bad Payers Issues Amount',
                                marker_color = 'rgb(139,0,0)' 
                            )
            )

    fig.add_trace(
                     go.Scatter(
                                x = df_1[df_1['year'] == year_chosen]['month'],
                                y = df_1[(df_1['year'] == year_chosen)]['good_payer_issue'],
                                name = 'Good Payers Issues Amount Trend',
                                marker_color = 'rgb(0,100,0)'
                            )
            )

    fig.add_trace(
                     go.Scatter(
                                x = df_1[df_1['year'] == year_chosen]['month'],
                                y = df_1[(df_1['year'] == year_chosen)]['bad_payer_issue'],
                                name = 'Bad Payers Issues Amount Trend',
                                marker_color = 'rgb(139,0,0)' 
                            )
            )

    fig.update_layout(
        title_text = '<b>Distribution of issues amount per month</b>',
        title_x = 0.5,
        title_y = 0.9,
        xaxis_tickfont_size = 14,
        xaxis = dict(
                    title = '<b>Issues Date (months)</b>',
                    titlefont_size = 16,
                    tickfont_size = 14
                    ),
        yaxis = dict(
                    title = '<b>Amount (%)</b>',
                    titlefont_size = 16,
                    tickfont_size = 14
                    ),
        font={
            "family": "Sans serif"},
        legend = dict(
                    x = 0.5, 
                    y = 1.0, 
                    bgcolor = 'rgba(255, 255, 255, 0)', 
                    bordercolor = 'rgba(255, 255, 255, 0)'
                    ),
        barmode = 'group',
        bargap = 0.15,
        bargroupgap = 0.1,

        width=1200, height=680
    )

    
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