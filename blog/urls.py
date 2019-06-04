from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('poat/<int:pk>/', views.poat_detail, name='poat_detail'),
    path('poat/new', views.poat_new, name='poat_new'),
]