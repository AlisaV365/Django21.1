from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, \
    IndexView, ProductListView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, toggle_activity

app_name = CatalogConfig.name



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('product/<int:pk>/', ProductListView.as_view(), name='product'),
    path('product/detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('activity/<int:pk>', toggle_activity, name='toggle_activity'),
]
