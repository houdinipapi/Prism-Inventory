from django.urls import path
from . import views


urlpatterns = [
    path('', views.wine_list, name='wine_list'),
    path('wine/<int:pk>/', views.wine_detail, name='wine_detail'),
    path('wine/new/', views.wine_create, name='wine_create'),
    path('wine/<int:pk>/edit/', views.wine_update, name='wine_update'),
    path('wine/<int:pk>/delete/', views.wine_delete, name='wine_delete'),
]
