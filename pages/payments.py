from dash import register_page 
import dash_bootstrap_components as dbc

register_page(__name__, path="/payments", name="Payments")

layout = dbc.Container(
    children=[
        "Payments Page"
    ]
)