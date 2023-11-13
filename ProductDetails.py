def ProductDetails(product_details_data):
    return html.div(
        className="product-details mb-4",
        children=[
            html.h2(className="h3", children="Detalles por producto"),
                        
            html.div(className="row",
                     children=[
                         html.div(className="col-md-6",
                                  children=html.div(className="card",
                                                    children=[
                                                        html.div(className="card-body",
                                                                 children=[
                                                                     html.h5(className="card-title", children="Producto 1"),
                                                                     html.p(className="card-text", children=product_details_data['product_1']['sales']),
                                                                 ])
                                                    ])),
                     ])
        ]
    )
