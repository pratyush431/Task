class LimitOrderAgent(PriceListener):
    
    def __init__(self, execution_client: ExecutionClient) -> None:
        super().__init__()
        self.execution_client = execution_client
        self.orders = []

    def add_order(self, buy: bool, product_id: str, amount: int, limit: float):
        """Add an order to be executed when the price reaches the limit."""
        self.orders.append({"buy": buy, "product_id": product_id, "amount": amount, "limit": limit})

    def on_price_tick(self, product_id: str, price: float):
        """Handle price tick and execute orders if price meets conditions."""
        for order in self.orders[:]:
            if order["product_id"] == product_id:
                if (order["buy"] and price <= order["limit"]) or (not order["buy"] and price >= order["limit"]):
                    try:
                        if order["buy"]:
                            self.execution_client.buy(product_id, order["amount"])
                        else:
                            self.execution_client.sell(product_id, order["amount"])
                        self.orders.remove(order)
                    except ExecutionException:
                        print(f"Failed to execute {'buy' if order['buy'] else 'sell'} order for {product_id}")

