from reactpy import html
from sidebar import Sidebar
from content import Content

def App():
    return html.div(className="container-fluid",
        children=[
            html.div(className="row",
                children=[
                    Sidebar(),
                    Content()
                ]
            )
        ]
    )
