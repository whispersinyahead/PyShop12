from django.contrib import admin
from django.db.models import Model
from django.urls import path

from .class_views import *
from .views import *


urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('<str:slug>/', ProductListView.as_view(), name='list'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='detail'),
    path('product/create/', ProductCreateView.as_view(), name='create-product'),
    path('product/update/<int:id>/', ProductUpdateView.as_view(), name='update_product'),
    path('product/delete/<int:id>/', ProductDeleteView.as_view(), name='delete_product')
]
