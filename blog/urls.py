from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = "blog"

urlpatterns = [
    path("", BlogListView.as_view(), name="blogpost_list"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blogpost_detail"),
    path("create/", BlogCreateView.as_view(), name="blogpost_create"),
    path("<int:pk>/update/", BlogUpdateView.as_view(), name="blogpost_update"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="blogpost_delete"),
]