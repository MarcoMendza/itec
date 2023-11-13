from react import html

def Content():
    return html.main(role="main", className="col-md-9 ml-sm-auto col-lg-10 px-4",
        children=[
            html.div(id="main-content", children="Main Content Here")
        ]
    )
