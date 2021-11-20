from dash import Dash
import dash_bootstrap_components as dbc
from app import init_app

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], title="Boilerplate", suppress_callback_exceptions=True)
init_app(app)

if __name__ == '__main__':
    app.run_server(debug=True)