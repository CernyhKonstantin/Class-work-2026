from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from .utils import get_current_timestamp
import random

class Product:
    name: str
    def __init__(self, name):
        self.id = get_current_timestamp() + random.randint(1,10)
        self.name = name
    
    def __str__(self):
        return f"""
        <h3>ProductID: {self.id}</h3>
        <h3>Name: {self.name}</h3>
    """

products = [
    Product("product1"),
    Product("product2"),
    Product("product3"),
    Product("product4"),
    Product("product5"),
    Product("product6"),
]

def get_product(request: HttpRequest, id:int):
    if len(products) <=0:
        return HttpResponse("<h1> Product list is empty</h1>")
    
    for product in products:
        if product.id == id:
            return HttpResponse(product)
    
    return HttpResponseNotFound(content='<h1 style="color: red;">Product not found</h1>')
    

def get_products(request):
    result = "<ul>"
    for product in products:
        result+=f"<li>{product}</li>"
    result+="</ul>"
    return HttpResponse(result)

def index(request:HttpRequest):
    return HttpResponse("""
<h1> Hello from Django </h1>
""")

def get_person(request: HttpRequest, name, surname):
    return HttpResponse(f"""
<h1> Name: {name} Suranme: {surname} </h1>
""")