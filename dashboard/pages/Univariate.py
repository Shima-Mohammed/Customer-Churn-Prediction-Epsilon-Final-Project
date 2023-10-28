import plotly.express as px
import pandas as pd 
from dash import Dash, dcc, html, Input, Output 
import dash_bootstrap_components as dbc
import dash 

dash.register_page(__name__)


######## import cleaned dataset ######
df = pd.read_csv('data/data_cleaned.csv')
######################################

############### plotly Graphs ####################
########## Gender ##############
df_Gender_group = df.groupby(by=["Gender"]).size().reset_index(name="counts")
gender_pie = px.pie(df_Gender_group, values='counts', names='Gender', title='gender')
########## married ###########
df_Married_group = df.groupby(by=["Married"]).size().reset_index(name="counts")
married_pie = px.pie(df_Married_group, values='counts', names='Married', title='Married')
########## NumberofDependents ############
df_NumberofDependents_group = df.groupby(by=["NumberofDependents"]).size().reset_index(name="counts")
NumberofDependents_pie = px.pie(df_NumberofDependents_group, values='counts', names='NumberofDependents', title='Number of Dependents')
######### NumberofReferrals ##########
NumberofReferrals_hist = px.histogram(df, x="NumberofReferrals",title='Number of Referrals')
######### Age ##############
age_hist = px.histogram(df, x="Age", title='Age')
####### TenureinMonths ######
TenureinMonths_hist = px.histogram(df, x="TenureinMonths",title='Tenure in Months')
###### offers#############
df_Offer_group = df.groupby(by=["Offer"]).size().reset_index(name="counts")
offer_pie = px.pie(df_Offer_group, values='counts', names='Offer', title='Offer')
########## PhoneService ########
df_PhoneService_group = df.groupby(by=["PhoneService"]).size().reset_index(name="counts")
PhoneService_pie = px.pie(df_PhoneService_group, values='counts', names='PhoneService', title='Phone Service')
########## MultipleLines ######
df_MultipleLines_group = df.groupby(by=["MultipleLines"]).size().reset_index(name="counts")
MultipleLines_pie = px.pie(df_MultipleLines_group, values='counts', names='MultipleLines', title='Multiple Lines')
########### internet service #########
df_InternetService_group = df.groupby(by=["InternetService"]).size().reset_index(name="counts")
InternetService_bar = px.bar(data_frame=df_InternetService_group, x="InternetService", y="counts",color='counts' , title='Internet Service')
####### internet type ##########
df_InternetType_group = df.groupby(by=["InternetType"]).size().reset_index(name="counts")
InternetType_bar = px.bar(data_frame=df_InternetType_group, x="InternetType", y="counts",color='counts',title='Internet Type')
###### online secuirty #######
df_OnlineSecurity_group = df.groupby(by=["OnlineSecurity"]).size().reset_index(name="counts")
OnlineSecurity_pie = px.pie(df_OnlineSecurity_group, values='counts', names='OnlineSecurity', title='Online Security')
######## onlineBackup ###########
df_OnlineBackup_group = df.groupby(by=["OnlineBackup"]).size().reset_index(name="counts")
OnlineBackup_pie = px.pie(df_OnlineBackup_group, values='counts', names='OnlineBackup', title='Online Backup')
####### DeviceProtectionPlan ########
df_DeviceProtectionPlan_group = df.groupby(by=["DeviceProtectionPlan"]).size().reset_index(name="counts")
DeviceProtectionPlan_pie = px.pie(df_DeviceProtectionPlan_group, values='counts', names='DeviceProtectionPlan', title='Device Protection Plan')
####### PremiumTechSupport #########
df_PremiumTechSupport_group = df.groupby(by=["PremiumTechSupport"]).size().reset_index(name="counts")
PremiumTechSupport_pie = px.pie(df_PremiumTechSupport_group, values='counts', names='PremiumTechSupport', title='Premium Tech Support')
##### StreamingMovies #########
df_StreamingMovies_group = df.groupby(by=["StreamingMovies"]).size().reset_index(name="counts")
StreamingMovies_pie = px.pie(df_StreamingMovies_group, values='counts', names='StreamingMovies', title='Streaming Movies')
######### StreamingTV ##########
df_StreamingTV_group = df.groupby(by=["StreamingTV"]).size().reset_index(name="counts")
StreamingTV_pie = px.pie(df_StreamingTV_group, values='counts', names='StreamingTV', title='Streaming TV')
######### StreamingMusic #######
df_StreamingMusic_group = df.groupby(by=["StreamingMusic"]).size().reset_index(name="counts")
StreamingMusic_pie = px.pie(df_StreamingMusic_group, values='counts', names='StreamingMusic', title='Streaming Music')
######## UnlimitedData ########
df_UnlimitedData_group = df.groupby(by=["UnlimitedData"]).size().reset_index(name="counts")
UnlimitedData_pie = px.pie(df_UnlimitedData_group, values='counts', names='UnlimitedData', title='Unlimited Data')
######## Contract ##########
df_Contract_group = df.groupby(by=["Contract"]).size().reset_index(name="counts")
Contract_bar = px.bar(data_frame=df_Contract_group, x="Contract", y="counts",color='counts',title='Contract')
######### PaperlessBilling ###########
df_PaperlessBilling_group = df.groupby(by=["PaperlessBilling"]).size().reset_index(name="counts")
PaperlessBilling_bar = px.bar(data_frame=df_PaperlessBilling_group, x="PaperlessBilling", y="counts",color='counts',title='Paperless Billing')
######### PaymentMethod ##########
df_PaymentMethod_group = df.groupby(by=["PaymentMethod"]).size().reset_index(name="counts")
PaymentMethod_bar = px.bar(data_frame=df_PaymentMethod_group, x="PaymentMethod", y="counts",color='counts',title='Payment Method')
####### TotalRevenue #########
TotalRevenue_hist = px.histogram(df, x="TotalRevenue",title='Total Revenue')
######### MonthlyCharge ############
MonthlyCharge_hist = px.histogram(df, x="MonthlyCharge",title='Monthly Charge')
######### AvgMonthlyGBDownload #########
AvgMonthlyGBDownload_hist = px.histogram(df, x="AvgMonthlyGBDownload")
######## CustomerStatus #########
df_CustomerStatus_group = df.groupby(by=["CustomerStatus"]).size().reset_index(name="counts")
CustomerStatus_pie = px.pie(df_CustomerStatus_group, values='counts', names='CustomerStatus', title='Customer Status')
####### ChurnCategory #########
df_customer_churned = df[df['CustomerStatus']=='Churned']
df_customer_churned_group = df_customer_churned.groupby(by=['ChurnCategory']).size().reset_index(name="counts")
ChurnCategory_bar = px.bar(data_frame=df_customer_churned_group, x='ChurnCategory', y="counts",color='counts',title='Churn Category')


#################dash component ########################
layout = html.Div([
    dbc.Row([
        dbc.Col(html.H1(children="Univariate analysis") ,sm=12,style={'padding-bottom':'20px'}) , 
        dbc.Col(dcc.Graph(id="gender_pie" ,figure= gender_pie ), lg=4,md=6,sm=12,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}),
        dbc.Col(dcc.Graph(id='NumberofReferrals_hist',figure=NumberofReferrals_hist), lg=8,md=6,sm=12,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) ,
        dbc.Col(dcc.Graph(id="NumberofDependents_pie" ,figure= NumberofDependents_pie ),lg=4,md=6,sm=12,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'} ) ,
        dbc.Col(dcc.Graph(id='married_pie',figure=married_pie),lg=4,md=6,sm=12,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) ,
        dbc.Col(dcc.Graph(id='offer_pie',figure=offer_pie), lg=4,md=6,sm=12,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) ,
        dbc.Col(dcc.Graph(id='TenureinMonths_hist',figure=TenureinMonths_hist), lg=8,md=6,sm=12,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}),
        dbc.Col(dcc.Graph(id='age_hist',figure=age_hist), lg=4,md=6,sm=12,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) , 
        dbc.Col(dcc.Graph(id='MonthlyCharge_hist',figure=MonthlyCharge_hist), lg=12,md=12,sm=1,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) ,
        dbc.Col(dcc.Graph(id='AvgMonthlyGBDownload_hist',figure=AvgMonthlyGBDownload_hist), lg=12,md=12,sm=12,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) ,
        dbc.Col(dcc.Graph(id='PhoneService_pie',figure=PhoneService_pie), lg=4,md=6,sm=1,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) ,
        dbc.Col(dcc.Graph(id='MultipleLines_pie',figure=MultipleLines_pie), lg=3,md=6,sm=1,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) ,
        dbc.Col(dcc.Graph(id='InternetService_bar',figure=InternetService_bar), lg=5,md=6,sm=1,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}), 
        dbc.Col(dcc.Graph(id='InternetType_bar',figure=InternetType_bar), lg=5,md=6,sm=1,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) ,
        dbc.Col(dcc.Graph(id='OnlineSecurity_pie',figure=OnlineSecurity_pie), lg=4,md=6,sm=1,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}),
        dbc.Col(dcc.Graph(id='OnlineBackup_pie',figure=OnlineBackup_pie), lg=3,md=6,sm=1,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) ,
        dbc.Col(dcc.Graph(id='DeviceProtectionPlan_pie',figure=DeviceProtectionPlan_pie), lg=4,md=6,sm=1,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}),
        dbc.Col(dcc.Graph(id='PremiumTechSupport_pie',figure=PremiumTechSupport_pie), lg=4,md=6,sm=1,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) ,
        dbc.Col(dcc.Graph(id='StreamingTV_pie',figure=StreamingTV_pie), lg=4,md=6,sm=1,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) ,
        dbc.Col(dcc.Graph(id='StreamingMovies_pie',figure=StreamingMovies_pie), lg=4,md=6,sm=1,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) , 
        dbc.Col(dcc.Graph(id='StreamingMusic_pie',figure=StreamingMusic_pie), lg=4,md=6,sm=1,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) ,
        dbc.Col(dcc.Graph(id='UnlimitedData_pie',figure=UnlimitedData_pie), lg=4,md=6,sm=1,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) , 
        dbc.Col(dcc.Graph(id='Contract_bar',figure=Contract_bar), lg=6,md=6,sm=1,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) , 
        dbc.Col(dcc.Graph(id='PaperlessBilling_bar',figure=PaperlessBilling_bar), lg=6,md=6,sm=1,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) ,
        dbc.Col(dcc.Graph(id='PaymentMethod_bar',figure=PaymentMethod_bar), lg=8,md=6,sm=1,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) , 
        dbc.Col(dcc.Graph(id='CustomerStatus_pie',figure=CustomerStatus_pie), lg=4,md=6,sm=1,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) ,
        dbc.Col(dcc.Graph(id='TotalRevenue_hist',figure=TotalRevenue_hist), lg=12,md=6,sm=1,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) , 
        dbc.Col(dcc.Graph(id='ChurnCategory_bar',figure=ChurnCategory_bar),  lg=12,md=6,sm=1,style={'margin-bottom':'15px','box-shadow':'2px 2px 5px rgba(239, 239, 240,0.8)'}) , 
    ],className="mb-2")  ,
],style={'padding':'20px 20px 20px 20px'})