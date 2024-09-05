import unittest

class LimitOrderAgentTest(unittest.TestCase):

    # Example test case:
    def test_limit_order_agent():
        class MockExecutionClient:
            def __init__(self):
                self.orders_executed = []

            def buy(self, product_id: str, amount: int):
                self.orders_executed.append(("buy", product_id, amount))

            def sell(self, product_id: str, amount: int):
                self.orders_executed.append(("sell", product_id, amount))

        mock_client = MockExecutionClient()
        agent = LimitOrderAgent(mock_client)
    
        agent.add_order(True, "IBM", 1000, 100.0)  
        agent.on_price_tick("IBM", 99.0)  
    
        assert mock_client.orders_executed == [("buy", "IBM", 1000)], "Test failed: Order not executed as expected"

    test_limit_order_agent()

