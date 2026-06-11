from dash import register_page, dcc, html, callback, Output, Input 
import dash_bootstrap_components as dbc
import plotly.express as px
from config.data_loader import DataCategory, DataLoader

register_page(__name__, path="/sellers", name="Sellers")

sellers_df = DataLoader(data_category=DataCategory.SELLERS).load_data()
geolocation_df = DataLoader(data_category=DataCategory.GEO_LOCATION).load_data()
geo_grouped = geolocation_df.groupby("geolocation_zip_code_prefix").first().reset_index()
sellers_with_geo = sellers_df.merge(
    geolocation_df,
    how="left",
    left_on="seller_zip_code_prefix",
    right_on="geolocation_zip_code_prefix"
)
seller_city = sellers_with_geo["seller_city"].unique()
seller_state = sellers_with_geo["seller_state"].unique()
total_seller_city = f"{len(seller_city):,}"
total_seller_state = f"{len(seller_state):,}"
total_sellers = f"{len(sellers_with_geo):,}"
seller_state_count = sellers_with_geo["seller_state"].value_counts().reset_index()

layout = dbc.Container(
    children=[
        #  ==============================================filter row======================================
       dbc.Row(
           children=[
               dbc.Col(
                   md=4,
                   children=[
                       dcc.Dropdown(
                           multi=True,
                           id="seller-state",
                           options=seller_state,
                           placeholder="Select State",
                           clearable=True   

                       )
                   ]
               ),
               dbc.Col(
                   md=4,
                   children=[
                       dcc.Dropdown(
                           multi=True,
                           id="seller-city",
                           options=seller_city,
                           placeholder="Select City",
                           clearable=True   

                       )
                   ]
               ),
           ],
           className="mt-3 mb-3"
       ),
       #  ==============================================end filter row======================================

        #  ==============================================cards row=========================================
       dbc.Row(
           children=[
               dbc.Col(
                   md=4,
                   children=[
                       dbc.Card(
                           dbc.CardBody(
                               [
                                    html.Div(
                                        children=[
                                            html.Div(
                                                children=[
                                                    html.H6("Total Sellers", className="text-muted"),
                                                    html.H3(total_sellers, id="total-sellers", className="text-dark"),
                                                    html.Span("All time sellers", className="text-success")
                                                ]
                                            ),
                                            html.I(className="bi bi-people-fill fs-1 text-primary")
                                        ],
                                        className="d-flex justify-content-between align-items-center"
                                    )   
                               ]
                           )
                       ),
                   ]
               ),
               dbc.Col(
                   md=4,
                   children=[
                        dbc.Card(
                           dbc.CardBody(
                               [
                                    html.Div(
                                        children=[
                                            html.Div(
                                                children=[
                                                    html.H6("Total States", className="text-muted"),
                                                    html.H3(total_seller_state, id="sellers-total-states", className="text-dark"),
                                                    html.Span("All time states", className="text-success")
                                                ]
                                            ),
                                            html.I(className="bi bi-globe fs-1 text-primary")
                                        ],
                                        className="d-flex justify-content-between align-items-center"
                                    )   
                               ]
                           )
                       ),
                   ]
               ),
               dbc.Col(
                   md=4,
                   children=[
                       dbc.Card(
                           dbc.CardBody(
                               [
                                    html.Div(
                                        children=[
                                            html.Div(
                                                children=[
                                                    html.H6("Total Cities", className="text-muted"),
                                                    html.H3(total_seller_city, id="sellers-total-city", className="text-dark"),
                                                    html.Span("All time cities", className="text-success")
                                                ]
                                            ),
                                            html.I(className="bi bi-globe2 fs-1 text-primary")
                                        ],
                                        className="d-flex justify-content-between align-items-center"
                                    )   
                               ]
                           )
                       ),
                   ]
               )

           ]
       ),
       #  ==============================================end cards row======================================

       #  ==============================================map row============================================

       dbc.Row(
           children=[
               dbc.Col(
                   md=12,
                   children=[
                       dbc.Card(
                           dbc.CardBody(
                               children=[
                                    dcc.Graph(
                                        id="sellers-map",
                                        figure = px.scatter_mapbox(
                                            sellers_with_geo,
                                            lat="geolocation_lat",
                                            lon="geolocation_lng",
                                            hover_name="seller_id",
                                            zoom=3,
                                            height=700,
                                            color="seller_state",
                                            title = "Sellers distribution across Brazil",
                                            mapbox_style="open-street-map"
                                        )
                                )
                               ]
                           )
                       ),

                   ]
               )
           ],
           className="mb-3 mt-3"
       ),
       #  ==============================================end map row============================================
       dbc.Row(
           children=[
               dbc.Card(
                dbc.CardBody(
                    children = [
                        dcc.Graph(
                            id="sellers-state-graph",
                            figure=px.bar(
                                seller_state_count,
                                x="seller_state",
                                y="count",
                                title="Sellers by State",
                                labels={"count":"Total Count", "seller_state":"State"}
                            )
                        )
                    ]
                )      
               ),

           ]
       )

    ]
)

@callback(
    Output("total-sellers", "children"),
    Output("sellers-total-states", "children"),
    Output("sellers-total-city", "children"),
    Output("sellers-map", "figure"),
    Output("sellers-state-graph", "figure"),
    Input("seller-state", "value"),
    Input("seller-city", "value")

)

def update_dashboard(seller_state, seller_city):
    sellers_df_copy = sellers_with_geo.copy()

    if seller_state:
        sellers_df_copy = sellers_df_copy[ sellers_df_copy["seller_state"].isin(seller_state) ]

    if seller_city:
        sellers_df_copy = sellers_df_copy[ sellers_df_copy["seller_city"].isin(seller_city) ]

    total_sellers = f"{len(sellers_df_copy):,}"
    total_seller_state = f"{len(sellers_df_copy['seller_state'].unique()):,}"
    total_seller_city = f"{len(sellers_df_copy['seller_city'].unique()):,}"
    seller_state_count = sellers_df_copy["seller_state"].value_counts().reset_index()

    sellers_map_figure = px.scatter_mapbox(
        sellers_df_copy,
        lat="geolocation_lat",
        lon="geolocation_lng",
        hover_name="seller_id",
        zoom=3,
        height=700,
        color="seller_state",
        title = "Sellers distribution across Brazil",
        mapbox_style="open-street-map"
    )    
    sellers_bar_figure =px.bar(
        seller_state_count,
        x="seller_state",
        y="count",
        title="Sellers by State",
        labels={"count":"Total Count", "seller_state":"State"}
    )
    return total_sellers, total_seller_state, total_seller_city, sellers_map_figure, sellers_bar_figure