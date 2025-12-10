from django.urls import path
from .views import (
    CategoryListCreateView, CategoryDetailView,
    SubCategoryListCreateView, SubCategoryDetailView,
    ProductListCreateView, ProductDetailView
)

urlpatterns = [
    #category urls
    path('categories/', CategoryListCreateView.as_view(), name='category_list_create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),

    #subCategory urls
    path('subcategories/', SubCategoryListCreateView.as_view(), name='subcategory_list_create'),
    path('subcategories/<int:pk>/', SubCategoryDetailView.as_view(), name='subcategory_detail'),

    #products urls
    path('', ProductListCreateView.as_view(), name='product_list_create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
