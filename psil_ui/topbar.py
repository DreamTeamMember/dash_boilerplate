from dash import html
import dash_bootstrap_components as dbc

TOPBAR_STYLE = {
    "width": "100%",
    "padding": "1rem 1rem",
    "backgroundColor": "#f8f9fa",
}

def create_top_bar(links, id='page-name'):
    return html.Div([
        dbc.Nav(
            links,
            vertical=False,
            pills=True,
        )],
        id= f"topbar-nav-{id}",
        style=TOPBAR_STYLE
    )
