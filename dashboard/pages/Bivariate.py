import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd 
from dash import Dash, dcc, html, Input, Output , State , callback , dash_table
import dash_bootstrap_components as dbc
import dash 
import plotly.graph_objects as go
import numpy as np

dash.register_page(__name__)


######## import cleaned dataset ######
df = pd.read_csv('data/data_cleaned.csv')
df_rows = df.shape[0]
################################################

############################ plotly graphs ###############################

########################### Gender ####################

#####status_gender#######
df_status_gender_group = df.groupby(by=["CustomerStatus",'Gender']).size().reset_index(name="counts")
status_gender_fig = px.bar(df_status_gender_group
                           , x="CustomerStatus"
                           , y="counts"
                           , color="Gender"
                           , barmode="group"
                           , category_orders = {"Gender": ["Male", "Female"]}
                           , title='Who leaves the company more, women or men?')

####### Dependents_Gender #####
Dependents_gender_fig = px.histogram(df
                           , x="NumberofDependents"
                           , color="Gender"
                           , barmode="group"
                           , category_orders = {"Gender": ["Male", "Female"]}
                           , title='Who have more Dependents, women or men?')
#####contract_gender#######
df_contract_gender_group = df.groupby(by=["Contract",'Gender']).size().reset_index(name="counts")
contract_gender_fig = px.bar(df_contract_gender_group
                           , x="Contract"
                           , y="counts"
                           , color="Gender"
                           , barmode="group"
                           , category_orders = {"Gender": ["Male", "Female"]}
                           , title='Contracts that are preferred by women and men')
#####PaymentMethod_gender#######
df_PaymentMethod_gender_group = df.groupby(by=["PaymentMethod",'Gender']).size().reset_index(name="counts")
PaymentMethod_gender_fig = px.bar(df_PaymentMethod_gender_group
                           , x="PaymentMethod"
                           , y="counts"
                           , color="Gender"
                           , barmode="group"
                           , category_orders = {"Gender": ["Male", "Female"]}
                           , title='What is the preferred Payment Method for both men and women ?')
######### PhoneService_Gender ######
PhoneService_Gender_pie = px.pie(df[df['PhoneService']=='Yes']
                          , values='TotalRevenue'
                          , names='Gender'
                          , title='Who subscribes more to the phone service, women or men?')
######### InternetService_Gender ######
InternetService_Gender_pie = px.pie(df[df['InternetService']=='Yes']
                          , values='TotalRevenue'
                          , names='Gender'
                          , title='Who subscribes more to the internet service, women or men?')
#####InternetType_gender#######
df_InternetType_gender_group = df.groupby(by=["InternetType",'Gender']).size().reset_index(name="counts")
InternetType_gender_fig = px.bar(df_InternetType_gender_group
                           , x="InternetType"
                           , y="counts"
                           , color="Gender"
                           , barmode="group"
                           , category_orders = {"Gender": ["Male", "Female"]}
                           , title='What is the preferred Internet Type for both men and women ?')
######### Revenue_Gender#########
# df_Revenue_Gender_group = df.groupby(by=['Gender'])['TotalRevenue'].sum().reset_index(name="Revenue")
# Revenue_Gender_fig = dash_table.DataTable(df_Revenue_Gender_group.to_dict('records'), [{"name": i, "id": i} for i in df_Revenue_Gender_group.columns])
# Revenue_Gender_fig = go.Figure(data=[go.Table(header=dict(values=['Gender','Revenue']),
#                                cells=dict(values=[df_Revenue_Gender_group['Gender'],df_Revenue_Gender_group['Revenue']]))])

###################################### NumberofDependents ############################
####### Married_NumberofDependents #####
Married_NumberofDependents_fig = px.histogram(df
                           , x="NumberofDependents"
                           , color="Married"
                           , barmode="group"
                           , category_orders = {"Married": ["Yes", "No"]}
                           , title='Does the marriage affect the number of Dependents?')
############TotalRevenue_NumberofDependents
TotalRevenue_NumberofDependents_fig = px.scatter(df
                                                 , y='NumberofDependents' 
                                                 , x='TotalRevenue'
                                                 , title='Are profits affected by an increase in the number of dependents?'
                                                 )
############AvgMonthlyGBDownload_NumberofDependents
AvgMonthlyGBDownload_NumberofDependents_fig = px.scatter(df
                                                 , y='NumberofDependents' 
                                                 , x='AvgMonthlyGBDownload'
                                                 , title='Is the gigabyte affected by an increase in the number of dependents?'
                                                 )
############MonthlyCharge_NumberofDependents
MonthlyCharge_NumberofDependents_fig = px.scatter(df
                                                 , y='NumberofDependents' 
                                                 , x='MonthlyCharge'
                                                 , title='Is the average monthly charges affected by an increase in the number of dependents?'
                                                 )
############Age_NumberofDependents
Age_NumberofDependents_fig = px.scatter(df
                                                 , y='NumberofDependents' 
                                                 , x='Age'
                                                 , title='Is the number of Dependents affected by age?'
                                                 )
####### status_NumberofDependents #####
status_NumberofDependents_fig = px.histogram(df
                           , x="NumberofDependents"
                           , color="CustomerStatus"
                           , barmode="group"
                           , category_orders = {"CustomerStatus": ["Stayed", "Churned"]}
                           , title='Does the number of Dependents affect the client’s status?')
############################################### CustomerStatus###################################
######Contract_CustomerStatus
df_Contract_CustomerStatus_group = df.groupby(by=["CustomerStatus",'Contract']).size().reset_index(name="counts")
Contract_CustomerStatus_fig = px.bar(df_Contract_CustomerStatus_group
                           , x="Contract"
                           , y="counts"
                           , color="CustomerStatus"
                           , barmode="group"
                           , category_orders = {"CustomerStatus": ["Stayed", "Churned"]}
                           , title='The most popular contract type for staying customers and churning customers')
######PaymentMethod_CustomerStatus
df_PaymentMethod_CustomerStatus_group = df.groupby(by=["CustomerStatus",'PaymentMethod']).size().reset_index(name="counts")
PaymentMethod_CustomerStatus_fig = px.bar(df_PaymentMethod_CustomerStatus_group
                           , x="PaymentMethod"
                           , y="counts"
                           , color="CustomerStatus"
                           , barmode="group"
                           , category_orders = {"CustomerStatus": ["Stayed", "Churned"]}
                           , title='The most popular payment method for staying customers and churning customers')
######PhoneService_CustomerStatus
df_PhoneService_CustomerStatus_group = df.groupby(by=["CustomerStatus",'PhoneService']).size().reset_index(name="counts")
PhoneService_CustomerStatus_fig = px.bar(df_PhoneService_CustomerStatus_group
                           , x="PhoneService"
                           , y="counts"
                           , color="CustomerStatus"
                           , barmode="group"
                           , category_orders = {"CustomerStatus": ["Stayed", "Churned"]}
                           , title='Do people who subscribe to phone service leave the company?')
######InternetService_CustomerStatus
df_InternetService_CustomerStatus_group = df.groupby(by=["CustomerStatus",'InternetService']).size().reset_index(name="counts")
InternetService_CustomerStatus_fig = px.bar(df_InternetService_CustomerStatus_group
                           , x="InternetService"
                           , y="counts"
                           , color="CustomerStatus"
                           , barmode="group"
                           , category_orders = {"CustomerStatus": ["Stayed", "Churned"]}
                           , title='Do people who subscribe to internet service leave the company?')
######InternetType_CustomerStatus
df_InternetType_CustomerStatus_group = df.groupby(by=["CustomerStatus",'InternetType']).size().reset_index(name="counts")
InternetType_CustomerStatus_fig = px.bar(df_InternetType_CustomerStatus_group
                           , x="InternetType"
                           , y="counts"
                           , color="CustomerStatus"
                           , barmode="group"
                           , category_orders = {"CustomerStatus": ["Stayed", "Churned"]}
                           , title='What is the type of Internet used by users who will churn?')

############TotalRevenue_NumberofDependents
TotalRevenue_NumberofDependents_fig = px.scatter(df
                                                 , y='NumberofDependents' 
                                                 , x='TotalRevenue'
                                                 , title='Are profits affected by an increase in the number of dependents?'
                                                 )
############# Age_CustomerStatus
Age_Stayed_data = df[df['CustomerStatus'] == 'Stayed']['Age'].tolist()
Age_Churned_data = df[df['CustomerStatus'] == 'Churned']['Age'].tolist()
Customer_Status = ['Stayed','Churned']
Age_CustomerStatus_fig = ff.create_distplot([Age_Stayed_data,Age_Churned_data]
                                            , Customer_Status
                                            ,show_hist=False)
Age_CustomerStatus_fig.update_layout(title_text='Age distribution of stayed and churned people')
############# TotalRevenue_CustomerStatus
TotalRevenue_Stayed_data = df[df['CustomerStatus'] == 'Stayed']['TotalRevenue'].tolist()
TotalRevenue_Churned_data = df[df['CustomerStatus'] == 'Churned']['TotalRevenue'].tolist()
Customer_Status = ['Stayed','Churned']
TotalRevenue_CustomerStatus_fig = ff.create_distplot([TotalRevenue_Stayed_data,TotalRevenue_Churned_data]
                                            , Customer_Status
                                            ,show_hist=False)
TotalRevenue_CustomerStatus_fig.update_layout(title_text='Total Revenue distribution of stayed and churned people')

############# NumberofReferrals_CustomerStatus
NumberofReferrals_Stayed_data = df[df['CustomerStatus'] == 'Stayed']['NumberofReferrals'].tolist()
NumberofReferrals_Churned_data = df[df['CustomerStatus'] == 'Churned']['NumberofReferrals'].tolist()
Customer_Status = ['Stayed','Churned']
NumberofReferrals_CustomerStatus_fig = ff.create_distplot([NumberofReferrals_Stayed_data,NumberofReferrals_Churned_data]
                                            , Customer_Status
                                            ,show_hist=False)
NumberofReferrals_CustomerStatus_fig.update_layout(title_text='Number of Referrals distribution of stayed and churned people')

############# TenureinMonths_CustomerStatus
TenureinMonths_Stayed_data = df[df['CustomerStatus'] == 'Stayed']['TenureinMonths'].tolist()
TenureinMonths_Churned_data = df[df['CustomerStatus'] == 'Churned']['TenureinMonths'].tolist()
Customer_Status = ['Stayed','Churned']
TenureinMonths_CustomerStatus_fig = ff.create_distplot([TenureinMonths_Stayed_data,TenureinMonths_Churned_data]
                                            , Customer_Status
                                            ,show_hist=False)
TenureinMonths_CustomerStatus_fig.update_layout(title_text='Tenure in Months distribution of stayed and churned people')
############# MonthlyCharge_CustomerStatus
MonthlyCharge_Stayed_data = df[df['CustomerStatus'] == 'Stayed']['MonthlyCharge'].tolist()
MonthlyCharge_Churned_data = df[df['CustomerStatus'] == 'Churned']['MonthlyCharge'].tolist()
Customer_Status = ['Stayed','Churned']
MonthlyCharge_CustomerStatus_fig = ff.create_distplot([MonthlyCharge_Stayed_data,MonthlyCharge_Churned_data]
                                            , Customer_Status
                                            ,show_hist=False)
MonthlyCharge_CustomerStatus_fig.update_layout(title_text='Monthly Charge distribution of stayed and churned people')
############TotalRevenue_AvgMonthlyGBDownload
TotalRevenue_AvgMonthlyGBDownload_fig = px.scatter(df
                                                 , x='AvgMonthlyGBDownload' 
                                                 , y='TotalRevenue'
                                                 , title='Are profits affected by an increase in the Avg Monthly GB Download?'
                                                 )
############################################### MonthlyCharge ###################################
######### Contract_MonthlyCharge
Contract_MonthlyCharge_group = df.groupby(by=["Contract"])['MonthlyCharge'].sum().reset_index(name="MonthlyCharge")
Contract_MonthlyCharge_fig = px.bar(data_frame=Contract_MonthlyCharge_group
                                    , x="Contract"
                                    , y="MonthlyCharge"
                                    , color = 'MonthlyCharge'
                                    ,title='Which contract has the highest monthly charge?')
######### offer_MonthlyCharge
offer_MonthlyCharge_group = df.groupby(by=["Offer"])['MonthlyCharge'].sum().reset_index(name="MonthlyCharge")
offer_MonthlyCharge_fig = px.bar(data_frame=offer_MonthlyCharge_group
                                    , x="Offer"
                                    , y="MonthlyCharge"
                                    , color = 'MonthlyCharge'
                                    ,title='Which offer has the highest monthly charge?')
######### AvgMonthlyGBDownload_MonthlyCharge
AvgMonthlyGBDownload_MonthlyCharge_fig = px.scatter(df
                                                 , x='AvgMonthlyGBDownload' 
                                                 , y='MonthlyCharge'
                                                 , title='Are monthly charge affected by an increase in the Avg Monthly GB Download?'
                                                 )#,trendline="ols"
######### InternetType_MonthlyCharge
InternetType_MonthlyCharge_group = df.groupby(by=["InternetType"])['MonthlyCharge'].sum().reset_index(name="MonthlyCharge")
InternetType_MonthlyCharge_fig = px.bar(data_frame=InternetType_MonthlyCharge_group
                                    , x="InternetType"
                                    , y="MonthlyCharge"
                                    , color = 'MonthlyCharge'
                                    ,title='Which Internet Type has the highest monthly charge?')
######### MultipleLines_MonthlyCharge
MultipleLines_MonthlyCharge_group = df.groupby(by=["MultipleLines"])['MonthlyCharge'].sum().reset_index(name="MonthlyCharge")
MultipleLines_MonthlyCharge_fig = px.bar(MultipleLines_MonthlyCharge_group
                                                 , x='MultipleLines' 
                                                 , y='MonthlyCharge'
                                                 , color='MonthlyCharge'
                                                 , title='Are monthly charge affected by an increase in the Multiple Lines?'
                                                 )

########### heatmap_corr
heatmap_corr_figure = px.imshow(df[['Age', 'NumberofDependents', 'NumberofReferrals', 'TenureinMonths',
       'AvgMonthlyGBDownload', 'MonthlyCharge', 'TotalRevenue']].corr(), text_auto=True)
############# dash component ###########
######## collapse ######
def collapse(title,id_names,graphs,WD):
    collapse = html.Div(
        [
            dbc.Button(
                title,
                id="collapse-button",
                style={'width':'100%','background-color':'black','border':'none','text-align':'left'},
                n_clicks=0
            ),
            dbc.Collapse(
                dbc.Card(children = [
                    # dbc.Row([
                    #     dbc.Col(dbc.CardBody(children=[Revenue_Gender_fig]),sm=12,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'})
                    # ]),
                    dbc.Row([
                        # dbc.Col(dbc.CardBody(children=[Revenue_Gender_fig]),lg=4,sm=12,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) , 
                        dbc.Col(dbc.CardBody(dcc.Graph(id=item,figure=graphs[idx])), lg=WD[idx],sm=12,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) 
                        for idx,item in enumerate(id_names) 
                    ])
               ]),
                id="collapse",
                is_open=True,
            ),
        ]
    )
    return collapse
############ layout ###########
layout = html.Div([
    dbc.Row([
        dbc.Col(html.H1(children="Bivariate analysis") ,sm=12,style={'padding-bottom':'20px'}) , 
        dbc.Col(
            collapse('Gender'
                     ,['PhoneService_Gender_pie','Dependents_gender_fig','InternetService_Gender_pie','InternetType_gender_fig','contract_gender_fig','PaymentMethod_gender_fig','status_gender_fig']
                     ,[PhoneService_Gender_pie,Dependents_gender_fig,InternetService_Gender_pie,InternetType_gender_fig,contract_gender_fig,PaymentMethod_gender_fig,status_gender_fig]
                     ,[5,7,5,7,5,7,12]
                     ), lg=12,md=12,sm=12,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}
            ),
        dbc.Col(
            collapse('Number of Dependents'
                     ,['Married_NumberofDependents_fig','TotalRevenue_NumberofDependents_fig','AvgMonthlyGBDownload_NumberofDependents_fig','MonthlyCharge_NumberofDependents_fig','Age_NumberofDependents_fig','status_NumberofDependents_fig']
                     ,[Married_NumberofDependents_fig,TotalRevenue_NumberofDependents_fig,AvgMonthlyGBDownload_NumberofDependents_fig,MonthlyCharge_NumberofDependents_fig,Age_NumberofDependents_fig,status_NumberofDependents_fig]
                     ,[5,7,5,7,5,7]
                     ), lg=12,md=12,sm=12,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}
            ),
        dbc.Col(
            collapse('Customer Status'
                     ,['Contract_CustomerStatus_fig','PaymentMethod_CustomerStatus_fig','PhoneService_CustomerStatus_fig','InternetService_CustomerStatus_fig','InternetType_CustomerStatus_fig','Age_CustomerStatus_fig','NumberofReferrals_CustomerStatus_fig','TotalRevenue_CustomerStatus_fig','TenureinMonths_CustomerStatus_fig','MonthlyCharge_CustomerStatus_fig','TotalRevenue_AvgMonthlyGBDownload_fig']
                     ,[Contract_CustomerStatus_fig,PaymentMethod_CustomerStatus_fig,PhoneService_CustomerStatus_fig,InternetService_CustomerStatus_fig,InternetType_CustomerStatus_fig,Age_CustomerStatus_fig,NumberofReferrals_CustomerStatus_fig,TotalRevenue_CustomerStatus_fig,TenureinMonths_CustomerStatus_fig,MonthlyCharge_CustomerStatus_fig,TotalRevenue_AvgMonthlyGBDownload_fig]
                     ,[12,12,12,12,12,12,12,12,12,12,12]
                     ), lg=12,md=12,sm=12,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}
            ),
        dbc.Col(
            collapse('Monthly Charge'
                     ,['Contract_MonthlyCharge_fig','offer_MonthlyCharge_fig','AvgMonthlyGBDownload_MonthlyCharge_fig','InternetType_MonthlyCharge_fig','MultipleLines_MonthlyCharge_fig','heatmap_corr_figure']
                     ,[Contract_MonthlyCharge_fig,offer_MonthlyCharge_fig,AvgMonthlyGBDownload_MonthlyCharge_fig,InternetType_MonthlyCharge_fig,MultipleLines_MonthlyCharge_fig,heatmap_corr_figure]
                     ,[12,12,12,12,12,12]
                     ), lg=12,md=12,sm=12,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}
            ),

    ],className="mb-2")  ,
],style={'padding':'20px 20px 20px 20px'})

##############
@callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open