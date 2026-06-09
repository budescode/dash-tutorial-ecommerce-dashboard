import dash_bootstrap_components as dbc
from dash import html

vertical_nav =     dbc.Nav(
                                [
                                    dbc.NavItem(
                                        dbc.NavLink(
                                            html.Div(
                                                children=[
                                                    html.I(className="bi bi-speedometer2 me-2"),
                                                    html.Span("Dashboard")
                                                ], className="navlink"
                                            ),href="/",  active="exact"
                                        )),
                                    dbc.NavItem(dbc.NavLink(
                                        html.Div(
                                            children=[
                                                html.I(className="bi bi-people me-2"),
                                                html.Span("Users")
                                            ], className="navlink"
                                        ),href="/users",  active="exact")),
                                  
                                    dbc.NavItem(dbc.NavLink(
                                        html.Div(
                                            children=[
                                                html.I(className="bi bi-box me-2"),
                                                html.Span("Products")
                                            ], className="navlink"
                                        ),href="/products",  active="exact")),
                                  
                                    dbc.NavItem(dbc.NavLink(
                                        html.Div(
                                            children=[
                                                html.I(className="bi bi-gift me-2"),
                                                html.Span("Orders")
                                            ], className="navlink"
                                        ),href="/orders",  active="exact")),
                                  
                                    dbc.NavItem(dbc.NavLink(
                                        html.Div(
                                            children=[
                                                html.I(className="bi bi-ui-checks me-2"),
                                                html.Span("Sellers")
                                            ], className="navlink"
                                        ),href="/sellers",  active="exact")),
                                  
                                    dbc.NavItem(dbc.NavLink(
                                        html.Div(
                                            children=[
                                                html.I(className="bi bi-file-earmark-x me-2"),
                                                html.Span("Review")
                                            ], className="navlink"
                                        ),href="/reviews",  active="exact"
                                        
                                        )),
                                  
                                    dbc.NavItem(dbc.NavLink(
                                        html.Div(
                                            children=[
                                                html.I(className="bi bi-file-earmark-diff me-2"),
                                                html.Span("Payments")
                                            ], className="navlink"
                                        ),href="/payments",  active="exact")),
                                    html.H6("ADMIN", className="ms-2 text-muted mt-4"),
                                    dbc.NavItem(dbc.NavLink(
                                        html.Div(
                                            children=[
                                                html.I(className="bi bi-gear me-2"),
                                                html.Span("Settings")
                                            ], className="navlink"
                                        ),href="/settings",  active="exact")),
                                  
                                    dbc.NavItem(dbc.NavLink(
                                        html.Div(
                                            children=[
                                                html.I(className="bi bi-shield-check me-2"),
                                                html.Span("Security")
                                            ], className="navlink"
                                        ),href="/security",  active="exact")),
                                  
                                    dbc.NavItem(dbc.NavLink(
                                        html.Div(
                                            children=[
                                                html.I(className="bi bi-question-circle me-2"),
                                                html.Span("Help & Support")
                                            ], className="navlink"
                                        ),href="/help",  active="exact")),
                                  
                                ],
                                vertical=True,
                                className="p-4",
                                style={
                                    "height": "100vh",
                                    "boxShadow":"2px 0 5px rgba(0,0,0,0.1)"
                                }
                            )
                        