from dash import register_page, html, callback, Input, Output, ctx 
import dash_bootstrap_components as dbc

register_page(__name__, path="/settings", name="Settings")

layout = dbc.Container(
    
    children=[
        dbc.Row(
            children = [
                    dbc.Card(
                        dbc.CardBody(
                            children=[
                                dbc.Col(
                                    md=12,
                                    children=[
                                        html.Div(
                                            children=[
                                                html.Div(children=[
                                                    html.H6("Settings", className="text-dark fw-bold"),
                                                    html.P("Manage your application preferences and configuration", className="text-muted")

                                                ]),
                                                html.Div(
                                                    children = [
                                                        dbc.Button(
                                                            children=[
                                                                html.I(className="bi bi-arrow-counterclockwise me-2"),
                                                                "Reset to Defaults"
                                                            ],
                                                            color="warning",
                                                            className="me-2"
                                                            
                                                        ),
                                                        dbc.Button(
                                                            children=[
                                                                html.I(className="bi bi-check2 me-2"),
                                                                "Save Changes"
                                                            ],
                                                            color="primary"
                                                        ),
                                                    ]
                                                ),
                                            ],
                                            className="d-flex justify-content-between align-items-center"
                                        )
                                    ]
                                )
                            ]
                        )
                    ),


            ],
            className="mt-3 mb-3"
        ),
        dbc.Row(
            children=[
                dbc.Col(md=3,
                        children=[
                            dbc.Nav(
                                children=[
                                    dbc.NavLink(
                                        children=[
                                           html.I(className="bi bi-gear me-3"), 
                                           "General"
                                        ],
                                        active=True,
                                        className="mb-1 text-start text-dark",
                                        id="nav-general",
                                        n_clicks=0,
                                        href="#"
                                    ),
                                    dbc.NavLink(
                                        children=[
                                           html.I(className="bi bi-palette me-3"), 
                                           "Appearance"
                                        ],
                                        className="text-dark text-start mb-1",
                                        id="nav-appearance",
                                        n_clicks=0,
                                        href="#"
                                        
                                        
                                        
                                    ),
                                    dbc.NavLink(
                                        children=[
                                           html.I(className="bi bi-bell me-3"), 
                                           "Notifications"
                                        ],
                                        className="mb-1 text-start text-dark",
                                        id="nav-notifications",
                                        n_clicks=0,
                                        href="#"
                                        
                                        

                                    ),
                                    dbc.NavLink(
                                        children=[
                                           html.I(className="bi bi-shield-lock me-3"), 
                                           "Privacy"
                                        ],
                                        className="text-dark text-start mb-1",
                                        id="nav-privacy",
                                        n_clicks=0,
                                        href="#"
                                        
                                        
                                    ),
                                    dbc.NavLink(
                                        children=[
                                           html.I(className="bi bi-hdd me-3"), 
                                           "Storage"
                                        ],
                                        className="text-dark text-start mb-1",
                                        id="nav-storage",
                                        n_clicks=0,
                                        href="#"
                                        
                                        
                                    ),
                                ],
                                vertical=True,
                                pills=True,
                                
                            )
                        ]),
                dbc.Col(md=9,
                        children=[
                            dbc.Card(
                                dbc.CardBody(
                                    children=[],
                                    id="settings-content"
                                )
                            )
                        ]
                ),
            ]
        )
    ],
)

@callback(
Output("settings-content", "children"),

Output("nav-general", "active"),
Output("nav-appearance", "active"),
Output("nav-notifications", "active"),
Output("nav-privacy", "active"),
Output("nav-storage", "active"),

Input("nav-general", "n_clicks"),
Input("nav-appearance", "n_clicks"),
Input("nav-notifications", "n_clicks"),
Input("nav-privacy", "n_clicks"),
Input("nav-storage", "n_clicks"),

)
def update_nav(general, appearance, notifications, privacy, storage):
    ctx_id = ctx.triggered_id
    if ctx_id == "nav-general" or ctx_id == None:
        return html.Div(children=[
            html.H5("General Settings", className="fw-bold"),
            html.P("Configure basic application preferences and behavior", className="text-muted"),

            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Div(
                                children=[
                                    html.Span("Application Language", className="fw-bold"),
                                    html.Small("Choose your preferred language for the interface", className="text-muted")
                                ]
                            ),
                            html.Div(
                                dbc.Select(
                                    options=[
                                        {"label":"English", "value":"en"},
                                        {"label":"Spanish", "value":"es"},
                                    ],
                                    value="es",
                                )
                            )
                        ],
                        className="d-flex justify-content-between align-items-center"
                    ),

                ], className="mb-3"
            ),
       
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Div(
                                children=[
                                    html.Span("Timezone", className="fw-bold"),
                                    html.Small("Set your local timezone for accurate timestamps", className="text-muted")
                                ]
                            ),
                            html.Div(
                                dbc.Select(
                                    options=[
                                        {"label":"Eastern Time (ET)", "value":"ET"},
                                        
                                    ],
                                    value="ET",
                                )
                            )
                        ],
                        className="d-flex justify-content-between align-items-center"
                    ),

                ], className="mb-3"
            ),     

            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Div(
                                children=[
                                    html.Span("Date Format", className="fw-bold"),
                                    html.Small("Choose how dates are displayed throughout the application", className="text-muted")
                                ]
                            ),
                            html.Div(
                                dbc.Select(
                                    options=[
                                        {"label":"MM/DD/YYYY (US)", "value":"US"},
                                        
                                    ],
                                    value="US",
                                )
                            )
                        ],
                        className="d-flex justify-content-between align-items-center"
                    ),

                ], className="mb-3"
            ),   
            html.Hr(), 
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Div(
                                children=[
                                    html.Span("Auto-save", className="fw-bold"),
                                    html.Small("Automatically save changes as you work", className="text-muted")
                                ]
                            ),
                            html.Div(
                                dbc.Switch(value=True, className="fs-4")
                            )
                        ],
                        className="d-flex justify-content-between align-items-center"
                    ),

                ], className="mb-3"
            ),  


        ]), True, False, False, False, False
    if ctx_id == "nav-appearance":
        return html.Div("Appearance"), False, True, False, False, False
    if ctx_id == "nav-notifications":
        return html.Div("Notifications"), False, False, True, False, False
    if ctx_id == "nav-privacy":
        return html.Div("Privacy"), False, False, False, True, False
    if ctx_id == "nav-storage":
        return html.Div("Storage"), False, False, False, False, True
    
