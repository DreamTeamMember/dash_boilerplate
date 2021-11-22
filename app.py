from dash import dcc, html
from utils.basepath import BASE_PATH
from psil_ui.router import init_router
from psil_ui.sub_router import init_sub_router
from psil_ui.sidebar import contentDiv
from layout.sidebar import sidebar
from routes import get_routes, get_sub_routes
from dash import dcc
from dash import html

def init_app(app):
    app.layout = html.Div([dcc.Location(id="url", refresh=False), sidebar, contentDiv])

    init_router(app, get_routes(app), base_url=BASE_PATH)

    init_sub_router(app, get_sub_routes(app), BASE_PATH)
    return app
