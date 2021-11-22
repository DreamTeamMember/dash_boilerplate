from dash import html
from dash.dependencies import Input, Output
from dash import dcc

def init_router(app, routes, base_url):
    @app.callback(
        Output("page-content", "children"),
        [Input("url", "pathname")]
    )
    def render_page_content(pathname):
        fallbackPage = html.Div([
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
        ])
        path_without_base = pathname.replace(base_url, '')
        page = routes.get(path_without_base)
        if not page:
            subPathIndex = path_without_base.find('/', 1)
            if subPathIndex != -1 :
                page = routes.get(path_without_base[0 : subPathIndex])

        return page or fallbackPage
