from app.database.repository import Repository
from app.database.queries import customers


class CustomerService:

    def __init__(self):

        self.repository = Repository()

    def total_customers(self):

        return self.repository.fetch_scalar(
            customers.TOTAL_CUSTOMERS
        )

    def customers_by_state(self):

        return self.repository.fetch_dataframe(
            customers.CUSTOMERS_BY_STATE
        )

    def customers_by_city(self):

        return self.repository.fetch_dataframe(
            customers.CUSTOMERS_BY_CITY
        )

    def customer_revenue(self):

        return self.repository.fetch_dataframe(
            customers.CUSTOMER_REVENUE
        )

    def monthly_customers(self):

        return self.repository.fetch_dataframe(
            customers.NEW_CUSTOMERS_MONTHLY
        )