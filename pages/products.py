from dash import register_page, html
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
from config.data_loader import DataCategory, DataLoader

register_page(__name__, path="/products", name="Products")


products_df = DataLoader(data_category=DataCategory.PRODUCTS).load_data()
total_products = f"{len(products_df):,}"
products_categories = products_df["product_category_name"].nunique()
products_categories_fmt = f"{products_categories:,}"
total_quantity = int(products_df["product_photos_qty"].sum())
total_quantity_fmt = f"{total_quantity:,}"
table_columns = [ {"headerName":x, "field":x, "sortable":True, "filter":True} for x in  products_df.columns.to_list()]


layout = dbc.Container(
    children=[
        # ==================================card row====================================
        dbc.Row(
            children = [
            dbc.Col(
                md=4,
                children = [
                    dbc.Card( 
                        dbc.CardBody(
                            children = [
                                html.Div( 
                                    [
                                        html.Div([
                                            html.H6("Total Products", className="text-muted"),
                                            html.H3(total_products, className="text-dark"),
                                            html.Span("All time product", className="text-success")
                                        ]),
                                        html.I(className="bi bi-file fs-1 text-primary")
                                    ],
                                    className="d-flex justify-content-between align-items-center"
                                )
                            ]
                        )
                    )
                ]
            ),

            dbc.Col(
                md=4,
                children = [
                    dbc.Card( 
                        dbc.CardBody(
                            children = [
                                html.Div( 
                                    [
                                        html.Div([
                                            html.H6("Total Categories", className="text-muted"),
                                            html.H3(products_categories_fmt, className="text-dark"),
                                            html.Span("All Categories", className="text-success")
                                        ]),
                                        html.I(className="bi bi-list fs-1 text-primary")
                                    ],
                                    className="d-flex justify-content-between align-items-center"
                                )
                            ]
                        )
                    )
                ]
            ),

            dbc.Col(
                md=4,
                children = [
                    dbc.Card( 
                        dbc.CardBody(
                            children = [
                                html.Div( 
                                    [
                                        html.Div([
                                            html.H6("Total Quantity", className="text-muted"),
                                            html.H3(total_quantity_fmt, className="text-dark"),
                                            html.Span("All time quantities", className="text-success")
                                        ]),
                                        html.I(className="bi bi-handbag fs-1 text-primary")
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
        # ==================================end card row====================================

        # ==================================Table Row====================================
        dbc.Row(
            children=[
                dbc.Col(
                    md=12,
                    children=[
                        dbc.Card(
                            dbc.CardBody(
                                children=[
                                    html.H5("Products", className="card-title mb-3"),
                                    dag.AgGrid(
                                        columnDefs=table_columns,
                                        rowData=products_df.to_dict("records"),
                                        style={"height":"500px"}

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