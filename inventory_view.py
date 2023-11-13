from reactpy import html

def InventoryView():
    return html.div(
        className="inventory-view p-4",
        children=[
            html.h1(className="h2", children="Inventario"),
            html.p(className="text-muted", children="Lista y detalles de productos"),
            html.div(
                className="table-responsive",
                children=[
                    html.table(
                        className="table table-striped table-sm",
                        children=[
                            html.thead(
                                className="thead-light",
                                children=html.tr(
                                    children=[
                                        html.th(children="CÓDIGO"),
                                        html.th(children="DESCRIPCIÓN"),
                                        html.th(children="EXISTENCIAS MES ANTERIOR"),
                                        html.th(children="ENTRADAS"),
                                        html.th(children="SALIDAS"),
                                        html.th(children="STOCK"),
                                    ]
                                )
                            ),
                            html.tbody(
                                children=[
                                    html.tr(
                                        children=[
                                            html.td(children="001"),
                                            html.td(children="Harina de arroz"),
                                            html.td(children="100"),
                                            html.td(children="70"),
                                            html.td(children="30"),
                                            html.td(children="140"),
                                        ]
                                    ),
                                ]
                            )
                        ]
                    )
                ]
            ),
            html.p(className="text-muted", children="Nota: Aquí se podrá determinar qué acciones puedes tener como admin, agregar, editar, eliminar."),
            html.p(className="text-muted", children="Nota: Considerar filtros de búsqueda."),
        ]
    )
