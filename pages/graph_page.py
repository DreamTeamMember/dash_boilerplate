from dash import dcc
from dash import html
from pages.styles.common_styles import PageDiv
from pages.graphs.first_graph import exampleGraph

graph_page = PageDiv([
    html.H4("Graph Examples"),
    html.Div(dcc.Graph(figure=exampleGraph))
])

def get_graph_page():
    return graph_page
