from pages.subroutes_page import subroutes_page, sub_routes as sb1
from pages.home_page import home_page
from pages.graph_page import graph_page
from pages.forms_page import get_forms_page
from dash import dcc

def get_routes(app):
    return {
        '/': home_page,
        '/subrouting_examples': subroutes_page,
        '/graph_examples': graph_page,
        '/form_examples': get_forms_page(app)
    }

sub_routes = { **sb1 }
