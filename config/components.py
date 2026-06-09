import dash_bootstrap_components as dbc
from dash import html
def card_metrics(title, value, description, icon_class):
    return  dbc.Card(
                    dbc.CardBody(
                        html.Div(
                            children=[
                                
                            html.Div(children=[
                                html.H6(title, className="text-muted"),
                                html.H3(value, className="text-dark"),
                                html.Span(description, className="text-success")
                            ]),

                            html.I(className=icon_class)
                            ],
                            className="d-flex justify-content-between"
                        )
                    )
                )