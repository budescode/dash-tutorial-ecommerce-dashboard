from dash import register_page, dcc, html, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
from config.data_loader import DataCategory, DataLoader
import dash_ag_grid as dag
register_page(__name__, path="/users", name="Users")

customers_df = DataLoader(data_category=DataCategory.CUSTOMERS).load_data()
state_options = sorted(customers_df["customer_state"].unique())
city_options = sorted(customers_df["customer_city"].unique())


layout = dbc.Container(
    children=[

        # ============================================filter======================================
        dbc.Row(
            children=[
                dbc.Col(
                    dcc.Dropdown(
                        multi=True,
                        id="state-filter",
                        options=state_options,
                        placeholder="Select State",
                        clearable=True
                    ),
                    md=3,
                ),
                dbc.Col(
                    dcc.Dropdown(
                        multi=True,
                        id="city-filter",
                        options=city_options,
                        placeholder="Select City",
                        clearable=True
                    ),
                    md=3,
                 )
            ],
            className="mb-4 mt-3"
        ),
        # ============================================end filter======================================
        
        # ============================================cards======================================
        dbc.Row(
            children=[
                # first card
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                           children = [
                                html.Div(
                                    children=[
                                        html.Div(
                                            children=[
                                                html.H6("Total Users", className="text-muted"),
                                                html.H3("", className="text-dark", id="total-users-kpi"),
                                                html.Span("All time users", className="text-success"),
                                            ]
                                        ),

                                        html.I(className="bi bi-people-fill fs-1 text-primary"),
                                    

                                    ],
                                    className="d-flex justify-content-between align-items-center"
                                )
                            ]
                        )
                    ),
                    md=6
                ),
                # second card
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                           children = [
                                html.Div(
                                    children=[
                                        html.Div(
                                            children=[
                                                html.H6("Active Users", className="text-muted"),
                                                html.H3("", className="text-dark", id="active-users-kpi"),
                                                html.Span("Users active", className="text-success"),
                                            ]
                                        ),

                                        html.I(className="bi bi-people-fill fs-1 text-primary"),
                                    

                                    ],
                                    className="d-flex justify-content-between align-items-center"
                                )
                            ]
                        )
                    ),
                    md=6
                ),

            ]
        ),
        # ============================================end cards======================================


        # ============================================plots======================================
        dbc.Row(
            children=[
                dbc.Col(
                    children=[
                        dbc.Card(
                            dbc.CardBody(
                                children=[
                                    # radio items
                                    html.Div(
                                        children=[
                                            html.H6("User Growth Over Time"),

                                            dbc.RadioItems(
                                                id="radios",
                                                className="btn-group",
                                                inputClassName="btn-check",
                                                labelClassName="btn btn-outline-primary",
                                                labelCheckedClassName="active",
                                                options=[
                                                    {"label": "7D", "value": "7D"},
                                                    {"label": "30D", "value": "30D"},
                                                    {"label": "90D", "value": "90D"},
                                                ],
                                                value=1,
                                            ),

                                        ],
                                        className="d-flex justify-content-between align-items-center"
                                    ),

                                    # bar chart
                                    html.Div(
                                        dcc.Graph(
                                            id="customers-state-graph",
                                            config={"displayModeBar": True}
                                        )
                                     )

                                ]
                            )
                        )
                    ],
                    md=9
                ),
                dbc.Col(
                    children=[
                        dbc.Card(
                            dbc.CardBody(
                                children=[
                                    html.H6("Users by State"),
                                    dag.AgGrid(
                                        id="users-by-state-grid",
                                        defaultColDef={"resizable":True, "flex":1},
                                        columnDefs = [
                                            {"headerName":"State", "field":"customer_state", "filter":True},
                                            {"headerName":"Total Count", "field":"count", "sortable":True}
                                        ]
                                        
                                    )
                                ]
                            )
                        )
                    ],
                    md=3,

                )
            ], className="mt-4"
         )

    ]
)

@callback(
    Output("total-users-kpi", "children"),
    Output("active-users-kpi", "children"),
    Output("customers-state-graph", "figure"),
    Output("users-by-state-grid", "rowData"),

    Input("state-filter", "value"),
    Input("city-filter", "value")

)
def update_dashboard(state_filter, city_filter):
    customer_df_copy = customers_df.copy()
    if state_filter:
        customer_df_copy = customer_df_copy[  customer_df_copy["customer_state"].isin(state_filter)  ]  

    if city_filter:
        customer_df_copy = customer_df_copy[  customer_df_copy["customer_city"].isin(city_filter)  ]  

    total_customers = f"{len(customer_df_copy):,}"
    active_customers =  len(customer_df_copy[  customer_df_copy["customer_zip_code_prefix"].notna() ])
    active_customers_fmt = f"{active_customers:,}"

    customers_state_df = customer_df_copy["customer_state"].value_counts().reset_index()


    figure = px.bar(
       customers_state_df,
       x =  "customer_state",
       y = "count",
       title = "Customers by State",
       labels={"count":"Total Count", "customer_state":"State"}
    )

    rowData = customers_state_df.to_dict("records")

    return total_customers, active_customers_fmt, figure, rowData
