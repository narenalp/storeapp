from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:item_code>/", views.detail, name="detail" ),
    path("<int:item_code>/price/", views.price, name="price" ),
    path("<int:item_code>/unit/", views.unit, name="unit" ),
]