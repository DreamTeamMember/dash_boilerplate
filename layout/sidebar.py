import dash_bootstrap_components as dbc
from psil_ui.sidebar import create_sidebar
from utils.basepath import BASE_PATH

links = [
    dbc.NavLink("Home Page", href=f"{BASE_PATH}/", active="exact"),
    dbc.NavLink("Subrouting Example", href=f"{BASE_PATH}/subrouting_examples", active="partial"),
    dbc.NavLink("Example Graphs", href=f"{BASE_PATH}/graph_examples", active="exact"),
    dbc.NavLink("Example Forms", href=f"{BASE_PATH}/form_examples", active="exact"),
]

sidebar = create_sidebar(links, "👨🏽‍🏫 Examples")