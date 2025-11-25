from django.urls import path

from product.views import CategoryListAPIView, ProductDetailAPIView, ProductListAPIView


urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
]
