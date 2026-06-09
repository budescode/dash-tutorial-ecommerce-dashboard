from dash import register_page 
import dash_bootstrap_components as dbc

register_page(__name__, path="/sellers", name="Sellers")

layout = dbc.Container(
    children=[
        "Sellers Page"
    ]
)