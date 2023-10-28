import dash 
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],use_pages=True)
server = app.server 

################# dash component ###############
############# NavBar #############
navbar = dbc.NavbarSimple(
    children=[
        # dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        # dbc.NavItem(dbc.NavLink("Page 2", href="#")),
        dbc.NavItem(dbc.NavLink(page['name'], href=page['path'],style={'color':'white'}))
        for page in dash.page_registry.values()
    ],
    brand="Telecom Customer Dashboard",
    brand_href="#",
    color="dark",
    dark=True,
    style={'position':'fixed','width':'100%','margin-bottom':'20px','z-index':'99'}
)
#######3 main page ###########
app.layout = html.Div([
    navbar , 
    html.Br() , 
    html.Br() ,
    html.Br() ,
    dash.page_container
],style={'overflow-x':'hidden','background-color':'rgba(239, 239, 240,0.1)'})

if __name__ == '__main__':
    app.run_server(debug=False, port=8051)