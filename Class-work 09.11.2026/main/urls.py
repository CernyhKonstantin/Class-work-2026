from django.urls import path
from . import views
urlpatterns = [path('', views.home, name='home'), path('registration/', views.registration_page, name='registration'), path('api/register/', views.register_api, name='register_api')]
