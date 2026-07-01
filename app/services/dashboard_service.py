from app.database.repository import Repository
from app.database.queries import dashboard


class DashboardService:

    def __init__(self):

        self.repository = Repository()

    def get_total_revenue(self):

        return self.repository.fetch_scalar(
            dashboard.TOTAL_REVENUE
        )

    def get_total_orders(self):

        return self.repository.fetch_scalar(
            dashboard.TOTAL_ORDERS
        )

    def get_total_customers(self):

        return self.repository.fetch_scalar(
            dashboard.TOTAL_CUSTOMERS
        )

    def get_total_products(self):

        return self.repository.fetch_scalar(
            dashboard.TOTAL_PRODUCTS
        )

    def get_total_sellers(self):

        return self.repository.fetch_scalar(
            dashboard.TOTAL_SELLERS
        )

    def get_average_order_value(self):

        return self.repository.fetch_scalar(
            dashboard.AVERAGE_ORDER_VALUE
        )

    def get_monthly_revenue(self):

        return self.repository.fetch_dataframe(
            dashboard.MONTHLY_REVENUE
        )

    def get_top_categories(self):

        return self.repository.fetch_dataframe(
            dashboard.TOP_CATEGORIES
        )

    def get_revenue_by_state(self):

        return self.repository.fetch_dataframe(
            dashboard.REVENUE_BY_STATE
        )

    def get_payment_distribution(self):

        return self.repository.fetch_dataframe(
            dashboard.PAYMENT_DISTRIBUTION
        )

    def get_recent_orders(self):

        return self.repository.fetch_dataframe(
            dashboard.RECENT_ORDERS
        )