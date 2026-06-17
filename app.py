from dash import Dash, page_container, Input, Output, callback
import dash_bootstrap_components as dbc
from pages.nav.nav_v import vertical_nav
from pages.nav.nav_h import horizontal_nav


app = Dash(
    external_stylesheets=[
        dbc.themes.BOOTSTRAP, 
        "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.13.1/font/bootstrap-icons.min.css"
    ],
    use_pages=True,
    pages_folder="pages",
    suppress_callback_exceptions=True
)

search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button("Search", color="primary", className="ms-2", n_clicks=0),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

app.layout = [
    dbc.Container(
        fluid=True,
        children = [
            dbc.Row( 
                children=[
                    dbc.Col(
                        children=[
                            horizontal_nav
                        ],
                        md=12, 
                    )
                ],
              
            ),
            dbc.Row( 
                children = [
                    dbc.Col(
                        md=2,
                        id="sidebar",
                        style = {"height":"100vh"},
                        children=[
                        
                            vertical_nav

                        ]
                    ),
                    dbc.Col(
                        md=10,
                        id="main-content",
                        children=[
                            page_container
                        ]
                    )
                ]
            )

        ], className="p-0 m-0"
    )
]

@callback(
    Output("sidebar", "style"),
    Output("sidebar", "md"),
    Output("main-content", "md"),
    Input("navbar-toggler", "n_clicks"),
)
def toggle_sidebar(n):
    click = n % 2
    if click == 0:
        return {"display":"block", "height":"100vh"}, 2, 10
    else:
        return {"display":"none", "height":"100vh"}, 0, 12

if __name__ == '__main__':
    app.run(debug=True, port=9010)
