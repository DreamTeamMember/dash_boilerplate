import dash_bootstrap_components as dbc
from dash import Input, Output, html, State
from dash.exceptions import PreventUpdate
import re

styles = {
    'width': '300px',
    'marginRight': '10px',
}

submit_button = dbc.Button("Submit", color="primary", className="me-1", id="submit-button")

email_input = html.Div([
    dbc.Label("Email"),
    dbc.Input(id="email-input", type="email", value=""),
    dbc.FormFeedback("Good job ! you've entered a correct email :-)", type="valid"),
    dbc.FormFeedback(
        "You should enter a valid email in order to get a smiley.",
        type="invalid")
    ],
    style=styles
)

password_input = html.Div([
    dbc.Label("Password"),
    dbc.Input(id="password-input", type="password", value=""),
    dbc.FormFeedback("Password is required",type="invalid"),
    ],
    style=styles
)

form_with_submit = html.Div([
    html.H4("Example with submit"),
    html.Div([
        html.Div(email_input),
        html.Div(password_input),
        html.Div(submit_button, style={ 'alignSelf': 'center', 'marginBottom': '15px' }),
    ], style={ 'display': 'flex' , 'marginBottom': '20px', 'height': '117px', 'alignItems': 'flex-start' }),
    html.Div(id="form-output")
])

def get_form_with_submit(app):
    # on click handler for the submit button - currently when valid we only display the form values instead of an api call
    app.clientside_callback(
        """
        function(clickNumber, passwordValid, emailValid, passwordTouched, emailTouched, email, password) {
            if (!passwordValid || !emailValid || !passwordTouched || !emailTouched || !clickNumber) return [""];
            const postObject = { email, password };
            return [`submitting object: ${JSON.stringify(postObject, null, 2)}`];
        }
        """,
        [Output("form-output", "children")],
        [
         Input("submit-button", 'n_clicks'),
         State("password-input", "valid"),
         State("email-input", "valid"),
         State("password-input", "touched"),
         State("email-input", "touched"),
         State("email-input", "value"),
         State("password-input", "value"),
        ]
    )
    # check form validation - should separate this since each change in password input also triggers the validation of the email field
    app.clientside_callback(
        """
        function(email, password, passwordTouched, emailTouched, clickSubmitAmount) {
            const validEmailRegex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            const email_validity = email.match(validEmailRegex);
            const touchedEmail = !!email || emailTouched || !!clickSubmitAmount;
            const touchedPassword = !!password || passwordTouched || !!clickSubmitAmount;
            return [
                email_validity && touchedEmail,
                !email_validity && touchedEmail,
                !password && touchedPassword,
                !!password && touchedPassword,
                touchedEmail ? "true" : "",
                touchedPassword ? "true" : "",
                (touchedEmail && !email_validity) || (touchedPassword && !password)
            ];
        }
        """,
        [
            Output("email-input", "valid"),
            Output("email-input", "invalid"),
            Output("password-input", "invalid"),
            Output("password-input", "valid"),
            Output("email-input", "touched"),
            Output("password-input", "touched"),
            Output("submit-button", "disabled")
        ],
        [
            Input("email-input", "value"),
            Input("password-input", "value"),
            Input("password-input", "touched"),
            Input("email-input", "touched"),
            Input("submit-button", 'n_clicks')
        ]
    )
    return form_with_submit
