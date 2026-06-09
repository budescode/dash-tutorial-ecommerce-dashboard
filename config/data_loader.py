from enum import Enum, auto 
import pandas as pd

class DataCategory(Enum):
    CUSTOMERS = auto()
    GEO_LOCATION = auto()
    ORDER_ITEMS = auto()
    ORDER_PAYMENTS = auto()
    ORDER_REVIEWS = auto()
    ORDERS = auto()
    PRODUCT_CATEGORY_TRANSLATIONS = auto()
    PRODUCTS = auto()
    SELLERS = auto()

class DataLoader:
    def __init__(self, data_category: DataCategory):
        self.data_category = data_category

    def load_data(self):
        if self.data_category == DataCategory.CUSTOMERS:
            return pd.read_csv("data/customers.csv")
        elif self.data_category == DataCategory.GEO_LOCATION:
            return pd.read_csv("data/geolocation.csv")
        elif self.data_category == DataCategory.ORDER_ITEMS:
            return pd.read_csv("data/order_items.csv")
        elif self.data_category == DataCategory.ORDER_PAYMENTS:
            return pd.read_csv("data/order_payments.csv")
        elif self.data_category == DataCategory.ORDER_REVIEWS:
            return pd.read_csv("data/order_reviews.csv")
        elif self.data_category == DataCategory.ORDERS:
            return pd.read_csv("data/orders.csv")
        elif self.data_category == DataCategory.PRODUCT_CATEGORY_TRANSLATIONS:
            return pd.read_csv("data/product_category_name_translation.csv")
        elif self.data_category == DataCategory.PRODUCTS:
            return pd.read_csv("data/products.csv")
        elif self.data_category == DataCategory.SELLERS:
            return pd.read_csv("data/sellers.csv")
        else:
            raise ValueError("Invalid data category")