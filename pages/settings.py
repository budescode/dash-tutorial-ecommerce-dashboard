from dash import register_page 
import dash_bootstrap_components as dbc

register_page(__name__, path="/settings", name="Settings")

layout = dbc.Container(
    children=[
        "Settings Page"
    ]
)