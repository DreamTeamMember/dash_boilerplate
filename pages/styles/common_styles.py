from dash import html, Input, Output

PAGE_STYLE = {
    "padding": "1rem 2rem",
}

def PageDiv(children):
    return html.Div(children, id="main-content", style=PAGE_STYLE)
