from django.urls import path
from .views import Products, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', Products.as_view()),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Ссылка на детали товара
    path('add/', ProductCreateView.as_view(), name='product_create'),  # Ссылка на создание товара
    path('<int:pk>/edit', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
]