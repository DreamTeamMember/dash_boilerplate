from dash import html, Input, Output, State
from pages.styles.common_styles import PageDiv
from psil_ui.dropdown import create_dropdown
from pages.forms_page.form_with_submit import get_form_with_submit
from pages.forms_page.additional_inputs import get_additional_inputs

metrics = [
    {'label': "DAU", 'value': "Related metrics: ARPDAU / PPU / Spinners"},
    {'label': "Revenue", 'value': "Related metrics: ARPDAU / ARPPU"},
    {'label': "Depositors", 'value': "Related metrics: ARPPU / PPU / FTD's"},
    {'label': "ARPDAU", 'value': "Related metrics: Revenue / DAU"},
    {'label': "ARPPU", 'value': "Related metrics: Revenue / Depositors"},
    {'label': "PPU", 'value': "Related metrics: Depositors / DAU"},
    {'label': "ftd", 'value': "Related metrics: Depositors"},
    {'label': "Spinners", 'value': "Related metrics: DAU"}
]


metrics_dropdown = create_dropdown("metrics-dropdown", "Metric", "Choose a Metric...", metrics)
dimensions_dropdown = create_dropdown("dimension-dropdown", "Dimensions", "Choose a Dimension...", [], { 'marginLeft': '15px'})
filters_dropdown = create_dropdown("filters-dropdown", "Filters", "Choose a Filter...", [], { 'marginLeft': '15px'})

mock_filters = {}
for metric in metrics:
    mock_filters[metric['value']] = [{ 'label': f"filter for {metric['label']}", 'value': metric['value'] }]

def get_forms_page(app):

    forms_page = PageDiv([
        html.H5("Dropdowns with relations"),
        html.Form([
            metrics_dropdown,
            dimensions_dropdown,
            filters_dropdown
        ], style={ 'display': 'flex' }),
        html.Br(),
        get_additional_inputs(app),
        html.Br(),
        get_form_with_submit(app)
    ])

    #--- Callbacks --- #

    @app.callback(
        Output("dimension-dropdown", "options"),
        Output("dimension-dropdown", "disabled"),
        Output("dimension-dropdown", "value"),
        Input("metrics-dropdown", "value"),
    )
    def update_dimension_dropdown(value):
        if not value: return [], True, ""
        return [{ 'label': value.replace("Related metrics: ", ""), 'value': value }], False, ""

    @app.callback(
        Output("filters-dropdown", "options"),
        Output("filters-dropdown", "disabled"),
        Output("filters-dropdown", "value"),
        Input("dimension-dropdown", "value"),
    )
    def update_filter_dropdown(value):
        if not value: return [], True, ""
        return mock_filters[value], False, ""

    #--- Callbacks End ---#
    
    return forms_page
