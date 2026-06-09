from dash import register_page 
import dash_bootstrap_components as dbc

register_page(__name__, path="/security", name="Security")

layout = dbc.Container(
    children=[
        "Security Page"
    ]
)