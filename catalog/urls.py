from django.urls import path

from catalog.apps import CatalogConfig

from .views import (ContactsView,
                    HomeView,
                    ProductCreateView,
                    ProductDeleteView,
                    ProductDetailView,
                    ProductsListView,
                    ProductUpdateView,
                    ProductUnpublishView)

app_name = CatalogConfig.name
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("catalog/contacts/", ContactsView.as_view(), name="contacts"),
    path("catalog/products_list/", ProductsListView.as_view(), name="products_list"),
    path("catalog/product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("catalog/product_create/", ProductCreateView.as_view(), name="product_create"),
    path("catalog/product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("catalog/product_confirm_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_confirm_delete"),
    path("catalog/product_unpublish/<int:pk>/", ProductUnpublishView.as_view(), name="product_unpublish")
]
