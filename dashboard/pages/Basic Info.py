import plotly.express as px
import pandas as pd 
from dash import Dash, dcc, html, Input, Output 
import dash_bootstrap_components as dbc
import dash 

dash.register_page(__name__, path='/')


######## import cleaned dataset ######
df = pd.read_csv('data/data_cleaned.csv')

####################### plotly Graphs ####################################
################ map ##################
df_map_group = df.groupby(by=['City','Latitude','Longitude']).size().reset_index(name="counts")
map_fig = px.scatter_mapbox(df_map_group, lat="Latitude", lon="Longitude", hover_name="City",size='counts') #,color='TotalRevenue'
map_fig.update_layout(mapbox_style="open-street-map")
map_fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
############### dash component ####################
########## create an card ############
def create_card(header,body,bk_color,txt_color):
    return dbc.Card(
    [
        # dbc.CardImg(src=img_src, top=True),
        dbc.CardBody(
            [
                html.H4(header, className="card-title" , style={'text-align': 'center'}),
                html.P(
                    body,
                    className="card-text",
                    style={'text-align': 'center' }
                )
            ]
        ),
    ],style={'background-color':bk_color,'color':txt_color}
)
####### layout ########

layout = html.Div([
    html.H1(children="Telecom Customer Churn Prediction") , 
    html.Ul(children = [
        html.Li(children=['The Customer Churn table contains information on all 7,043 customers from a Telecommunications company' ]),
        html.Li(children=['and contains details about their demographics, location, tenure, subscription services, status for the quarter stayed, or churned, and more!' ]),
    ]) , 
    html.Br(),
    dbc.Row([
    dbc.Col(create_card(df.shape[0],'Total number of customers ','black','white'), md=6,sm=1,style={'margin-bottom':'10px'}),
    dbc.Col(create_card(df.shape[1],'Total number of Features','black','white'), md=6,sm=1,style={'margin-bottom':'10px'})
    ],align="center") , 
    html.Br(),
    dbc.Row([
        dbc.Col(html.H6(children='in California in Q2 2022 ( '+ str(df["City"].nunique()) +' Total number of customers cities )'), md=4,sm=1,style={'margin-bottom':'10px'}),
        dbc.Col(dcc.Graph(id="map_fig",figure=map_fig ), md=8,sm=1,style={'margin-bottom':'10px'}),
    ],align="center"),
    html.Br(),
    html.Hr(),
    dbc.Row([
    dbc.Col(html.H4(children='The Summary of Q2 2022'), lg=12 , md=12,sm=1,style={'margin-bottom':'15px'}), 
    dbc.Col(create_card(df[df['Offer'] != 'No Offer']['Offer'].nunique(),"Total number of offers ",'white','black'), lg=4, md=6,sm=1,style={'margin-bottom':'10px'}),
    dbc.Col(create_card(df['InternetType'].nunique(),'Total number of internet type','white','black'), lg=4 , md=6,sm=1,style={'margin-bottom':'10px'}),
    dbc.Col(create_card(df['Contract'].nunique(),'Total number of contract types','white','black') , lg=4 , md=6,sm=1,style={'margin-bottom':'10px'}),
    dbc.Col(create_card("{:,}".format(df['TotalRevenue'].sum()),'Total Revenue ','black','white') , lg=12 , md=6,sm=1,style={'margin-bottom':'10px'}),
    dbc.Col(create_card(df[df['CustomerStatus'] == 'Stayed'].shape[0],'Total number of customer stayed ','rgba(0,255,0,0.5)','black'), lg=6 , md=6,sm=1,style={'margin-bottom':'10px'}),
    dbc.Col(create_card(df[df['CustomerStatus'] != 'Stayed'].shape[0],'Total number of customer churned ','rgba(187, 37, 37,0.5)','black'), lg=6 , md=6,sm=1,style={'margin-bottom':'10px'}),
    ],align="center")

],style={'padding':'20px 20px 20px 20px'})