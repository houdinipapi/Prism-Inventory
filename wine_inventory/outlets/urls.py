from django.urls import path
from . import views

urlpatterns = [
    path("", views.outlet_list, name="outlet_list"),
    path("outlet/<int:pk>/", views.outlet_detail, name="outlet_detail"),
    path("outlet/new/", views.outlet_create, name="outlet_create"),
    path("outlet/<int:pk>/edit/", views.outlet_update, name="outlet_update"),
    path("outlet/<int:pk>/delete/", views.outlet_delete, name="outlet_delete"),
    path(
        "outlet/<int:outlet_pk>/wine/new/",
        views.outlet_wine_create,
        name="outlet_wine_create",
    ),
    path(
        "outlet/<int:outlet_pk>/wine/<int:pk>/edit/",
        views.outlet_wine_update,
        name="outlet_wine_update",
    ),
    path(
        "outlet/<int:outlet_pk>/wine/<int:pk>/delete/",
        views.outlet_wine_delete,
        name="outlet_wine_delete",
    ),
]
