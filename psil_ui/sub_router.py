from dash import html
from dash.dependencies import Input, Output
from dash import dcc

def init_sub_router(app, sub_routes, base_url):
    @app.callback(
        Output("subrouter-content", "children"),
        [Input("url", "pathname")]
    )
    def render_page_content(pathname):
        return sub_routes.get(pathname.replace(base_url, '')) or "couldn't find route"
