from app.database.repository import Repository
from app.database.queries import sellers


class SellerService:

    def __init__(self):

        self.repository = Repository()

    def total_sellers(self):

        return self.repository.fetch_scalar(
            sellers.TOTAL_SELLERS
        )

    def sellers_by_state(self):

        return self.repository.fetch_dataframe(
            sellers.SELLERS_BY_STATE
        )

    def seller_revenue(self):

        return self.repository.fetch_dataframe(
            sellers.SELLER_REVENUE
        )

    def seller_orders(self):

        return self.repository.fetch_dataframe(
            sellers.SELLER_ORDERS
        )

    def top_states(self):

        return self.repository.fetch_dataframe(
            sellers.TOP_SELLER_STATES
        )