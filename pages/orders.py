from dash import register_page 
import dash_bootstrap_components as dbc

register_page(__name__, path="/orders", name="Orders")

layout = dbc.Container(
    children=[
        "Orders Page"
    ]
)