from dash import register_page, html, dcc
import dash_bootstrap_components as dbc
from config.data_loader import DataLoader, DataCategory 
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
register_page(__name__, path="/reviews", name="Reviews")


reviews_df = DataLoader(data_category=DataCategory.ORDER_REVIEWS).load_data()
reviews_df["review_creation_date"] = pd.to_datetime(reviews_df["review_creation_date"])

monthly_scores = reviews_df.set_index("review_creation_date").resample("ME")["review_score"].mean().reset_index()


one_star =  len(reviews_df[ reviews_df["review_score"] == 1 ])
one_star_fmt = f"{one_star:,}"
two_star = len(reviews_df[ reviews_df["review_score"] == 2 ])
two_star_fmt = f"{two_star:,}"
three_star = len(reviews_df[ reviews_df["review_score"] == 3 ])
three_star_fmt = f"{three_star:,}"
four_star = len(reviews_df[ reviews_df["review_score"] == 4 ])
four_star_fmt = f"{four_star:,}"
five_star = len(reviews_df[ reviews_df["review_score"] == 5 ])
five_star_fmt = f"{five_star:,}"
all_stars = one_star + two_star + three_star + four_star + five_star
all_stars_fmt = f"{all_stars:,}"

score_counts = reviews_df["review_score"].value_counts().reset_index()




def stars_cards(title, star_number):
    return dbc.Col(
        md=2,
        children=[
            dbc.Card(
                dbc.CardBody(
                    html.Div(
                        children=[
                            html.Div(
                                children=[
                                    html.H6(title, className="text-muted fs-6"),
                                    html.H4(star_number, className="text-dark")
                                ]
                            ),
                            html.I(className="bi bi-star-fill fs-4 text-primary")
                        ],
                        className="d-flex justify-content-between align-items-center"
                    )
                )
            )
        ]
    )


layout = dbc.Container(
    children=[
        dbc.Row(
            children=[
                stars_cards("All Stars", all_stars_fmt),
                stars_cards("One Star", one_star_fmt),
                stars_cards("Two Stars", two_star_fmt),
                stars_cards("Three Stars", three_star_fmt),
                stars_cards("Four Stars", four_star_fmt),
                stars_cards("Five Stars", five_star_fmt),

            ],
            className="mt-3 mb-3"
        ),
        dbc.Row(
            dbc.Col(
                md=12,
                children=[
                    dbc.Card(
                        dbc.CardBody(
                            dcc.Graph(
                                figure = px.bar(
                                    score_counts,
                                    x="review_score",
                                    y="count",
                                    title="Reviews by Score",
                                    color="review_score",
                                    labels={"count":"Total Count", "review_score":"Score"}
                                )   
                            )
                        )
                    )
                ]
            ),
            className="mb-3"
        ),

        dbc.Row(
            children=[
                dbc.Col(
                    md=12,
                    children = [
                        dbc.Card(
                            dbc.CardBody(
                                dcc.Graph(
                                    figure = px.line(
                                        monthly_scores,
                                        x="review_creation_date",
                                        y="review_score",
                                        markers=True,
                                        labels={"review_score":"Average Score", "review_creation_date":"Date"}
                                    )
                                )
                            )
                        )
                    ]
                )   
            ],
            className="mb-3"
        ),
        dbc.Row(
            children=[
                dbc.Col(
                    md=12,
                    children = [
                        dbc.Card(
                            dbc.CardBody(
                                children=[
                                    html.H5("Reviews", className="card-title mb-3"),
                                    dag.AgGrid(
                                        columnDefs=[ {"headerName":x.replace("_", " ").title(), "field":x, "sortable":True, "filter":True} for x in reviews_df.columns ],
                                        rowData=reviews_df.to_dict("records"),
                                        style={"height":"500px"},
                                        
                                    )

                                ]
                            )
                        )
                    ]
                )
            ]
        )

    ]
)