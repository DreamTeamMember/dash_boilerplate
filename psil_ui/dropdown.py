import dash_bootstrap_components as dbc
from dash import html, dcc

def create_dropdown(id, label, placeholder, options, style={}):
    default_style = { 'width': '200px' }
    dropdown_style = { **default_style, **style }
    return html.Div(
        [
            dbc.Label(label, html_for=id),
            dcc.Dropdown(id=id, options=options, placeholder=placeholder,),
        ],
        className="mb-3",
        style=dropdown_style
    )