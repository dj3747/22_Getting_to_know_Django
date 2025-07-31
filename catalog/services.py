from catalog.models import Product
from django.core.cache import cache

class ProductService:
    @staticmethod
    def get_products_by_category(category_id):
        key = f"products_in_category_{category_id}"
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(category_id=category_id).prefetch_related('category')
            cache.set(key, list(products), 60 * 15)
        return products
