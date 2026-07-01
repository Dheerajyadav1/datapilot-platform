from app.database.repository import Repository
from app.database.queries import sales


class SalesService:

    def __init__(self):

        self.repository = Repository()

    def daily_revenue(self):

        return self.repository.fetch_dataframe(
            sales.DAILY_REVENUE
        )

    def monthly_orders(self):

        return self.repository.fetch_dataframe(
            sales.MONTHLY_ORDERS
        )

    def top_categories(self):

        return self.repository.fetch_dataframe(
            sales.TOP_PRODUCT_CATEGORIES
        )

    def payment_distribution(self):

        return self.repository.fetch_dataframe(
            sales.PAYMENT_TYPES
        )

    def order_status(self):

        return self.repository.fetch_dataframe(
            sales.ORDER_STATUS
        )

    def top_states(self):

        return self.repository.fetch_dataframe(
            sales.TOP_STATES
        )