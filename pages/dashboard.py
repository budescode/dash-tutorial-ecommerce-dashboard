from dash import register_page, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from config.data_loader import DataLoader, DataCategory
from config.components import card_metrics
register_page(__name__, path="/", name="Dashboard")


customers_df = DataLoader(data_category=DataCategory.CUSTOMERS).load_data()
orders_df = DataLoader(data_category=DataCategory.ORDERS).load_data()
sellers_df = DataLoader(data_category=DataCategory.SELLERS).load_data()
payments_df = DataLoader(data_category=DataCategory.ORDER_PAYMENTS).load_data()
geo_df = DataLoader(data_category=DataCategory.GEO_LOCATION).load_data()

geo_grouped = geo_df.groupby("geolocation_zip_code_prefix").first().reset_index()
customers_geo = customers_df.merge(
    geo_grouped,
    how = "left",
    left_on="customer_zip_code_prefix",
    right_on="geolocation_zip_code_prefix"
)


layout = dbc.Container(
    children=[
        html.H5("Dashboard"),
        html.P("Welcome back! Here's what's happening!"),

        dbc.Row(
            children=[
                dbc.Col(card_metrics("Total Users", f"{len(customers_df):,}", "All time users", "bi bi-people-fill fs-4 text-primary"),),
                dbc.Col(card_metrics("Total Orders", f"{len(orders_df):,}", "All time orders", "bi bi-gift fs-4 text-primary"),),
                dbc.Col(card_metrics("Total Sellers", f"{len(sellers_df):,}", "All time sellers", "bi bi-people-shop fs-4 text-primary"),),
                dbc.Col(card_metrics("Total Payment", f"{len(payments_df):,}", "All time payments", "bi bi-bank fs-4 text-primary"),),

            ]
        ),
        dbc.Row(
            dbc.Col(
                md=12,
                children=[
                    dcc.Graph(
                        figure=px.scatter_mapbox(
                            customers_geo,
                            lat="geolocation_lat",
                            lon="geolocation_lng",
                            hover_name = "customer_id",
                            zoom=3,
                            height=700,
                            color="geolocation_state",
                            title = "Customers distribution across Brazil",
                            mapbox_style="open-street-map"

                        )
                    )
                ]
             )   
        )

    ],
    class_name="py-4"
)