from dash import register_page, html, dcc 
import dash_bootstrap_components as dbc
import plotly.express as px
from config.data_loader import DataCategory, DataLoader

register_page(__name__, path="/payments", name="Payments")
payments_df = DataLoader(data_category=DataCategory.ORDER_PAYMENTS).load_data()
total_payments = f"{len(payments_df):,}" 
payment_value = payments_df["payment_value"].sum()
payment_value_fmt = f"{payment_value:,.2f}"
payment_type_counts = payments_df["payment_type"].value_counts().reset_index()
layout = dbc.Container(
    children=[
        # =====================================cards row============================================================
        dbc.Row(
            children=[
                dbc.Col(
                    md=6,
                    children = [
                        dbc.Card(
                            dbc.CardBody(
                                children=[
                                    html.Div(
                                        children=[
                                            html.Div(children=[
                                                html.H6("Total Payments", className="text-muted"),
                                                html.H3(total_payments, className="text-dark"),
                                                html.Span("All time payments", className="text-success")

                                            ]),
                                            html.I(className="bi bi-cash fs-1 text-primary")
                                        ],
                                        className="d-flex justify-content-between align-items-center"
                                    )
                                ]
                            )
                        )
                    ]
                ),
                dbc.Col(
                    md=6,
                    children = [
                        dbc.Card(
                            dbc.CardBody(
                                children=[
                                    html.Div(
                                        children=[
                                            html.Div(children=[
                                                html.H6("Total Payment Value", className="text-muted"),
                                                html.H3(payment_value_fmt, className="text-dark"),
                                                html.Span("All time payment values", className="text-success")

                                            ]),
                                            html.I(className="bi bi-bank fs-1 text-primary")
                                        ],
                                        className="d-flex justify-content-between align-items-center"
                                    )
                                ]
                            )
                        )
                    ]
                ),
            ],
            className="mt-3 mb-3"
        ),
        # =====================================end cards row============================================================

        # =====================================plots row================================================================

        dbc.Row(
            children=[
                dbc.Col(
                    md=8,
                    children=[
                        dbc.Card(
                            dbc.CardBody(
                                children=[
                                    dcc.Graph(
                                        figure =  px.histogram(
                                            payments_df,
                                            x = "payment_installments",
                                            title = "Installment Distribution (How many months?)",
                                            text_auto=True,
                                            labels={"payment_installments":"Payment Installments"}   
                                        )  
                                    )
                                ]
                            )
                        )
                    ]
                ),
                dbc.Col(
                    md=4,
                    children=[
                        dbc.Card(
                            dbc.CardBody(
                                children=[
                                    dcc.Graph(
                                        figure = px.pie(
                                            payment_type_counts,
                                            values="count",
                                            names="payment_type",
                                            title="Payment Type Distribution",
                                            hole=0.5,
                                            color_discrete_sequence=px.colors.qualitative.Alphabet_r
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                ),
            ],
            className="mb-3"
        ),

        # =====================================end plots row============================================================

        # =====================================box plot row=============================================================

        dbc.Row(
            children=[
                dbc.Col(
                    md=12,
                    children=[
                        dbc.Card(
                            dbc.CardBody(
                                children=[
                                    dcc.Graph(
                                        figure=px.box(
                                            payments_df,
                                            x="payment_type",
                                            y="payment_value",
                                            title = "Transaction Valye By Payment Method",
                                            points=False,
                                            labels={"payment_value":"Payment Value", "payment_type":"Payment Type"}
                                        
                                        )
                                    )
                                ]

                            )
                        )
                    ]
                )
            ]
        )

        # =====================================endbox plot row==========================================================
    ]
)