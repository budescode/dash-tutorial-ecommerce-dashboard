from dash import register_page 
import dash_bootstrap_components as dbc

register_page(__name__, path="/products", name="Products")

layout = dbc.Container(
    children=[
        "Products Page"
    ]
)