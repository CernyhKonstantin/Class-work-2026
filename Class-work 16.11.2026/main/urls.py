from django.urls import path
from . import views
urlpatterns = [
 path("", views.home, name="home"),
 path("cards/create/", views.card_create, name="card_create"),
 path("cards/<int:pk>/", views.card_detail, name="card_detail"),
 path("cards/<int:pk>/edit/", views.card_update, name="card_update"),
 path("cards/<int:pk>/delete/", views.card_delete, name="card_delete"),
 path("tags/", views.tag_list, name="tag_list"),
 path("tags/<slug:slug>/", views.tag_detail, name="tag_detail"),
]
