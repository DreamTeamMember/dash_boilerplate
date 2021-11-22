from pages.subroutes_page import get_subroutes_page, get_subroutes as get_sb1
from pages.home_page import get_home_page
from pages.graph_page import get_graph_page
from pages.forms_page.forms_page import get_forms_page
from dash import dcc

def get_routes(app):
    return {
        '/': get_home_page(),
        '/subrouting_examples': get_subroutes_page(),
        '/graph_examples': get_graph_page(),
        '/form_examples': get_forms_page(app)
    }

def get_sub_routes(app):
    return { **get_sb1() }
