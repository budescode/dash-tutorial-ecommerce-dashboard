import dash_bootstrap_components as dbc
from dash import html, callback, Output, Input, State
from config.colors import Colors
horizontal_nav =  dbc.Navbar(

                                color="light",
                                class_name="border-bottom sticky-top shadow-sm",
                                children=[
                                    html.Div(
                                        children=[
                                            html.Div(
                                                children=[
                                                    html.H5("Budescode", style={"color":Colors.BLUE}, className="m-0 p-0 fw-bold"),
                                                    dbc.Button(
                                                        html.I(className="bi bi-list"),
                                                        color="light",
                                                        className="border",
                                                        id="navbar-toggler",
                                                        n_clicks=0,
                                                     )
                                    
                                                ],
                                                className="d-flex align-items-center gap-2 flex-grow-1"
                                            ),
                                            html.Div(
                                                dbc.InputGroup(
                                                        [
                                                            
                                                            dbc.Input(id="input-group-button-input", placeholder="Search... (Ctrl + K)",),
                                                            dbc.Button(
                                                                html.I(className="bi bi-search", style={"color":Colors.BLACK}), 
                                                                id="input-group-button", 
                                                                className="bg-transparent border"
                                                            ),
                                                        ],
                                                        className="w-66"
                                                    ),
                                                    className="d-flex flex-grow-1"

                                            ),

                                            html.Div(children=[
                                                html.I(className="bi bi-person-circle fs-4"),
                                                html.Span("John Doe")
                                            ], className="d-flex flex-grow-1 justify-content-end gap-2 align-items-center")

                                        ],
                                        className="d-flex justify-content-between w-100 align-items-center px-3 "
                                    )
                                ],
                                className="p-0 m-0"

                                
                            )

