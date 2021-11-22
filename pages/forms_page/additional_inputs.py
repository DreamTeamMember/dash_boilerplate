import dash_bootstrap_components as dbc
import dash_core_components as dcc
from datetime import date
from dash import Input, Output, html
from pages.styles.common_styles import FlexDiv

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

standalone_toggles = html.Div(
    [
        FlexDiv(
            [
                FormDiv(dbc.Checkbox(
                    id="standalone-checkbox",
                    label="This is a checkbox",
                    value=False,
                )),
                FormDiv(dbc.Switch(
                    id="standalone-switch",
                    label="This is a toggle switch",
                    value=False,
                )),
                FormDiv(dbc.RadioButton(
                    id="standalone-radio",
                    label="This is a radio button",
                    value=False,
                )),
            ]
        ),
        html.P(id="standalone-radio-check-output"),
    ]
)

date_pickers = html.Div (
    FlexDiv([
        FormDiv(dcc.DatePickerSingle(
            date='2017-06-21',
            display_format='X'
        )),
        FormDiv(dcc.DatePickerSingle(
            month_format='MMMM Y',
            placeholder='MMMM Y',
            date=date(2020, 2, 29)
        )),
        FormDiv(dcc.DatePickerRange(
            end_date=date(2017, 6, 21),
            display_format='MMMM Y, DD',
            start_date_placeholder_text='MMMM Y, DD'
        )),
    ])
)

additional_inputs = html.Div(
    [
        html.H5("Additional input components"),
        html.H6("Date pickers"),
        date_pickers,
        html.Br(),
        html.H6("Standalone toggles"),
        standalone_toggles,
        html.H6("Toggle lists"),
        dbc.Form([FlexDiv([radioitems, checklist, switches])]),
        html.P(id="radioitems-checklist-output"),
        html.H6("Text inputs"),
        FormDiv(dbc.Textarea(className="mb-3", placeholder="A Textarea")),
    ], style={ 'maxWidth': '1000px' }
)

def get_additional_inputs(app):
    app.clientside_callback(
        """
        function(radio_items_value, checklist_value, switches_value) {
            const RadioButtonOutput = `Selected Radio ${radio_items_value}`;
            const ChecklistOutput = checklist_value.length ? `CheckList Items '${checklist_value.join(",")}'`: "no checks selected";
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