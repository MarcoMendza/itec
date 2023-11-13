from reactpy import html

def SalesSummary(sales_summary_data):
    return html.div(
        className="sales-summary mb-4",
        children=[
            html.h2(className="h3", children="Resumen de ventas"),
            html.div(className="row",
                     children=[
                         html.div(className="col-md-4",
                                  children=html.div(className="card",
                                                    children=[
                                                        html.div(className="card-body",
                                                                 children=[
                                                                     html.h5(className="card-title", children="Total vendido"),
                                                                     html.p(className="card-text", children=sales_summary_data['total_sales'])
                                                                 ])
                                                    ])),
                     ])
        ]
    )
