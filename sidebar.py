from react import html

def Sidebar():
    return html.div(
        {
            'className': 'd-flex flex-column flex-shrink-0 p-3 bg-light',
            'style': {'width': '280px'}
        },
        html.a(
            {'href': '#', 'className': 'd-flex align-items-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none'},
            html.span({'className': 'fs-4'}, 'ITEC ADMIN')
        ),
        html.hr(),
        html.ul(
            {'className': 'nav nav-pills flex-column mb-auto'},
            html.li({'className': 'nav-item'},
                    html.a({'href': '#inventario', 'className': 'nav-link active', 'aria-current': 'page'}, 'Inventario')),
            html.li({'className': 'nav-item'},
                    html.a({'href': '#ventas', 'className': 'nav-link'}, 'Ventas')),
            html.li({'className': 'nav-item'},
                    html.a({'href': '#compras', 'className': 'nav-link'}, 'Compras')),
            html.li({'className': 'nav-item'},
                    html.a({'href': '#logistica', 'className': 'nav-link'}, 'Logística')),
            html.li({'className': 'nav-item'},
                    html.a({'href': '#ajustes', 'className': 'nav-link'}, 'Ajustes'))
        )
    )
