from dash import register_page 
import dash_bootstrap_components as dbc

register_page(__name__, path="/help", name="Help & Support")

layout = dbc.Container(
    children=[
        "Help & Support Page"
    ]
)