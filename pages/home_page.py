from dash import html
from pages.styles.common_styles import PageDiv

home_page = PageDiv([
    html.H4("Welcome to the boilerplate example"),
])

def get_home_page():
    return home_page
