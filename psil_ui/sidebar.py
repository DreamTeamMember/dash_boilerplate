from dash import html
import dash_bootstrap_components as dbc

SIDE_BAR_WIDTH = "16rem"

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": SIDE_BAR_WIDTH,
    "padding": "2rem 1rem",
    "backgroundColor": "#f8f9fa",
}

def create_sidebar(links, header="", sub_header=""):
    return html.Div(
        [
            header and html.H5(header, className="h5"),
            header and html.Hr(),
            sub_header and html.P(
                sub_header, className="h6"
            ),
            dbc.Nav(
                links,
                vertical=True,
                pills=True,
            ),
        ],
        style=SIDEBAR_STYLE,
    )

CONTENT_STYLE = {
    "width": f"calc(100% - {SIDE_BAR_WIDTH})",
    "marginLeft": SIDE_BAR_WIDTH,
    "height": "100vh"
}

TOPBAR_STYLE = {
    "marginLeft": "18rem",
    "marginRight": "2rem",
}

contentDiv = html.Div(id="page-content", style=CONTENT_STYLE)
