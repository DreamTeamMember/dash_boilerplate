from dash import html
import dash_bootstrap_components as dbc
from utils.basepath import BASE_PATH
from psil_ui.topbar import create_top_bar
from pages.styles.common_styles import PageDiv

top_nav_links = [
    dbc.NavLink("Route 1", href=f"{BASE_PATH}/subrouting_examples", active="exact"),
    dbc.NavLink("Route 2", href=f"{BASE_PATH}/subrouting_examples/route2", active="exact"),
    dbc.NavLink("Route 3", href=f"{BASE_PATH}/subrouting_examples/route3", active="exact"),
]

topbar = create_top_bar(top_nav_links, id='subrouting_page')

subroutes_page = html.Div([
    topbar,
    PageDiv([html.Div(id='subrouter-content')])
])

def get_subroutes_page():
    return subroutes_page

def get_subroutes():
    return {
        '/subrouting_examples': html.H4("Main route 🤴🏽"),
        '/subrouting_examples/route2': html.H4("Sub route 2 👩🏽‍🌾"),
        '/subrouting_examples/route3': html.H4("Sub route 3 🤶🏽")
    }
