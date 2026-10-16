from django.urls import path

from . import views

"""
<type:prop_name> # example
<int:prop_name>
# по дефолту використовується рядок
<str:prop_name> 
<slug:prop_name>
<uuid: prop_name>
<path:prop_name> /url

"""

urlpatterns = [
    path('', views.index, name="start_page"),
    path('person/', views.get_person, kwargs={"name":"Joe", "surname":"Due"}, name="get_person"),
    path('products/',views.get_products, name="get_products"),
    path('product/<int:id>', views.get_product, name="product_by_id")
]