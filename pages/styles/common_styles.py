from dash import html, Input, Output

PAGE_STYLE = {
    "padding": "1rem 2rem",
}

def get_flex_style(width):
    return {
        'display': 'flex',
        'width': width
    }

def PageDiv(children):
    return html.Div(children, id="main-content", style=PAGE_STYLE)

def FlexDiv(children, width="100%"):
    return html.Div(children, style=get_flex_style(width))
