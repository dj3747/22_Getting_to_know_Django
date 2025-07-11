from django.urls import reverse_lazy

from .models import Product
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class HomeView(TemplateView):
    template_name = 'catalog/home.html'


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductsListView(ListView):
    model = Product
    template_name = "catalog/products_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    fields = ["name", "description","image"]
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:products_list")

class ProductUpdateView(UpdateView):
    model = Product
    fields = ["name", "price", "category", "image"]
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:products_list")

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:products_list")
