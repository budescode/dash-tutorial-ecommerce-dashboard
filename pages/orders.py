from dash import register_page, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import dash_ag_grid as dag

from config.data_loader import DataCategory, DataLoader

register_page(__name__, path="/orders", name="Orders")

orders_df = DataLoader(data_category=DataCategory.ORDERS).load_data()
total_orders = f"{len(orders_df):,}"

processing_orders = len(orders_df[ orders_df["order_status"] == "processing" ])
processing_orders_fmt = f"{processing_orders:,}"

delivered_orders = len(orders_df[ orders_df["order_status"] == "delivered" ])
delivered_orders_fmt = f"{delivered_orders:,}"

cancelled_orders = len(orders_df[ orders_df["order_status"] == "cancelled" ])
cancelled_orders_fmt = f"{cancelled_orders:,}"

order_status = orders_df["order_status"].unique()

min_date = orders_df["order_purchase_timestamp"].min()
max_date = orders_df["order_purchase_timestamp"].max()


layout = dbc.Container(
    children=[
        # ==================================card row====================================
       dbc.Row(
           children=[
               
               dbc.Col(
                   md=3, 
                   children=[
                       dbc.Card(
                           dbc.CardBody(
                               [
                                   html.Div(
                                       [
                                           html.Div(
                                               [
                                                   html.H6("Total Orders", className="text-muted"),
                                                   html.H3(total_orders, className="text-dark"),
                                                   html.Span("All time orders", className="text-success")
                                               ]
                                           ),
                                           html.I(className="bi bi-gift fs-1 text-primary")
                                       ],
                                       className="d-flex justify-content-between align-items-center"
                                   )
                               ]
                           )
                       )
                   ]
               ),

               dbc.Col(
                   md=3, 
                   children=[
                       dbc.Card(
                           dbc.CardBody(
                               [
                                   html.Div(
                                       [
                                           html.Div(
                                               [
                                                   html.H6("Processing Orders", className="text-muted"),
                                                   html.H3(processing_orders_fmt, className="text-dark"),
                                                   html.Span("Total Processing Orders", className="text-success")
                                               ]
                                           ),
                                           html.I(className="bi bi-gift fs-1 text-primary")
                                       ],
                                       className="d-flex justify-content-between align-items-center"
                                   )
                               ]
                           )
                       )
                   ]
               ),

               dbc.Col(
                   md=3, 
                   children=[
                       dbc.Card(
                           dbc.CardBody(
                               [
                                   html.Div(
                                       [
                                           html.Div(
                                               [
                                                   html.H6("Delivered Orders", className="text-muted"),
                                                   html.H3(delivered_orders_fmt, className="text-dark"),
                                                   html.Span("Total Delivered Orders", className="text-success")
                                               ]
                                           ),
                                           html.I(className="bi bi-gift fs-1 text-primary")
                                       ],
                                       className="d-flex justify-content-between align-items-center"
                                   )
                               ]
                           )
                       )
                   ]
               ),

               dbc.Col(
                   md=3, 
                   children=[
                       dbc.Card(
                           dbc.CardBody(
                               [
                                   html.Div(
                                       [
                                           html.Div(
                                               [
                                                   html.H6("Cancelled Orders", className="text-muted"),
                                                   html.H3(cancelled_orders_fmt, className="text-dark"),
                                                   html.Span("Total Cancelled Orders", className="text-success")
                                               ]
                                           ),
                                           html.I(className="bi bi-gift fs-1 text-primary")
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


       # ==================================filter row====================================
        dbc.Row(
            children=[

                dbc.Col(
                    md=4,
                    children=[
                        dcc.Dropdown(
                            multi=True,
                            id="order-status",
                            options=order_status,
                            placeholder="Select Order Status",
                            clearable=True
                        )
                    ]
                ),
                dbc.Col(
                    md=4,
                    children=[
                        dcc.DatePickerRange(
                            id="order-date-range",
                            min_date_allowed=min_date,
                            max_date_allowed=max_date,
                            start_date=min_date,
                            end_date=max_date
                        )
                    ]
                )
            ],
            className="mb-3"
        ),

       # ==================================end filter row====================================

       # ==================================table row=========================================

        dbc.Row(
            children=[
                dbc.Col(
                    md=12,
                    children = [
                        dbc.Card(
                            dbc.CardBody(
                                children=[
                                    html.H6("Order Records"),
                                    dag.AgGrid(
                                        id="order-table",
                                        columnDefs=[ {"headerName":x, "field":x, "filter":True, "sortable":True } for x in orders_df.columns ],
                                        style={"height":"500px"},
                                        rowData=orders_df.to_dict("records"),
                                    )

                                ]
                            )
                        )
                    ]
                )
            ]
        )

       # ==================================end table row=========================================


    ]
)

@callback(
    Output("order-table", "rowData"),
    Input("order-status", "value"),
    Input("order-date-range", "start_date"),
    Input("order-date-range", "end_date"),

)

def update_order_table(order_status, start_date, end_date):
    filtered_orders =  orders_df.copy() 
    if order_status:
        filtered_orders = filtered_orders[ filtered_orders["order_status"].isin(order_status) ]
    
    if start_date:
        filtered_orders = filtered_orders[ filtered_orders["order_purchase_timestamp"] >= start_date ]
        
    if end_date:
        filtered_orders = filtered_orders[ filtered_orders["order_purchase_timestamp"] <= end_date ]
    
    return filtered_orders.to_dict("records")

    
