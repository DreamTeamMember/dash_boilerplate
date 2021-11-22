import dash_bootstrap_components as dbc
from dash import Input, Output, html
from pages.styles.common_styles import FlexDiv
dbc.Textarea(className="mb-3", placeholder="A Textarea"),

DIV_STYLE = { 'width' : '30%' }

def FormDiv(children):
    return html.Div(children, style={ 'width': '30%' })

radioitems = FormDiv(
    [
        dbc.Label("Radio Buttons"),
        dbc.RadioItems(
            options=[
                {"label": "Option 1", "value": 1},
                {"label": "Option 2", "value": 2},
                {"label": "Disabled Option", "value": 3, "disabled": True},
            ],
            value=1,
            id="radioitems-input",
        ),
    ]
)

checklist = FormDiv(
    [
        dbc.Label("Check list"),
        dbc.Checklist(
            options=[
                {"label": "Option 1", "value": 1},
                {"label": "Option 2", "value": 2},
                {"label": "Disabled Option", "value": 3, "disabled": True},
            ],
            value=[1],
            id="checklist-input",
        ),
    ]
)

switches = FormDiv(
    [
        dbc.Label("Switches"),
        dbc.Checklist(
            options=[
                {"label": "Option 1", "value": 1},
                {"label": "Option 2", "value": 2},
                {"label": "Disabled Option", "value": 3, "disabled": True},
            ],
            value=[1],
            id="switches-input",
            switch=True,
        ),
    ]
)

additional_inputs = html.Div(
    [
        html.H4("Additional Input components"),
        dbc.Textarea(className="mb-3", placeholder="A Textarea"),
        dbc.Form([FlexDiv([radioitems, checklist, switches])]),
        html.P(id="radioitems-checklist-output"),
    ]
)

def get_additional_inputs(app):
    app.clientside_callback(
        """
        function(radio_items_value, checklist_value, switches_value) {
            const RadioButtonOutput = `Selected Radio ${radio_items_value}`;
            const ChecklistOutput = checklist_value.length ? `CheckList Items '${checklist_value.join(",")}'`: "no checklists selected";
            const SwitchOutput = switches_value.length ? `Selected Switches '${switches_value.join(",")}'`: "no switches selected";
            return [RadioButtonOutput,ChecklistOutput,SwitchOutput].join(". ");
        }
        """,
        Output("radioitems-checklist-output", "children"),
        [
            Input("radioitems-input", "value"),
            Input("checklist-input", "value"),
            Input("switches-input", "value"),
        ]
    )

    return additional_inputs