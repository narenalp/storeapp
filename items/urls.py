from django.urls import path

from . import views

app_name = "items"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add" ),
    path("<int:item_code>/edit/", views.edit, name="edit" ),
    path("<int:item_code>/disp/", views.disp, name="disp" ),
]