from django.urls import path

from catalog.apps import CatalogConfig

from .views import (ContactsView,
                    HomeView,
                    ProductCreateView,
                    ProductDeleteView,
                    ProductDetailView,
                    ProductsListView,
                    ProductUpdateView,
                    ProductUnpublishView, ProductByCategoryView, CategoryListView)

app_name = CatalogConfig.name
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("products_list/", ProductsListView.as_view(), name="products_list"),
    path("product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path("product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("product_confirm_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_confirm_delete"),
    path("product_unpublish/<int:pk>/", ProductUnpublishView.as_view(), name="product_unpublish"),
    path('catalog/category_list', CategoryListView.as_view(), name='categories_list'),
    path("category/products_by_category/<int:category_id>/", ProductByCategoryView.as_view(), name="products_by_category"),

]
