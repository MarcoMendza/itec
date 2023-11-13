from reactpy import html
from inventory_view import InventoryView

def Content():
    return html.main(role="main", className="col-md-9 ml-sm-auto col-lg-10 px-4",
        children=[
            InventoryView()
        ]
    )
