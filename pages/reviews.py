from dash import register_page 
import dash_bootstrap_components as dbc

register_page(__name__, path="/reviews", name="Reviews")

layout = dbc.Container(
    children=[
        "Reviews Page"
    ]
)