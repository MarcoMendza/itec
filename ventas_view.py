def VentasView():
    return html.div(
        className="ventas-view",
        children=[
            SalesSummary(sales_summary_data),
            ProductDetails(product_details_data),
            SalesHistory(sales_history_data),
            PaymentMethods(payment_methods_data),
        ]
    )
