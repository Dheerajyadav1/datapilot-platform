from app.database.repository import Repository
from app.database.queries import products


class ProductService:

    def __init__(self):

        self.repository = Repository()

    def total_products(self):

        return self.repository.fetch_scalar(
            products.TOTAL_PRODUCTS
        )

    def products_by_category(self):

        return self.repository.fetch_dataframe(
            products.PRODUCTS_BY_CATEGORY
        )

    def category_revenue(self):

        return self.repository.fetch_dataframe(
            products.CATEGORY_REVENUE
        )

    def average_price(self):

        return self.repository.fetch_scalar(
            products.AVERAGE_PRODUCT_PRICE
        )

    def product_weight(self):

        return self.repository.fetch_dataframe(
            products.PRODUCT_WEIGHT
        )

    def dimensions(self):

        return self.repository.fetch_dataframe(
            products.PRODUCT_DIMENSIONS
        )