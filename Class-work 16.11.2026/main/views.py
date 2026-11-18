from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CardForm
from .models import Card, Tag

def home(request):
    return render(request, "main/home.html", {"cards": Card.objects.prefetch_related("tags").all()})

def card_detail(request, pk):
    card = get_object_or_404(Card.objects.prefetch_related("tags"), pk=pk)
    return render(request, "main/card_detail.html", {"card": card})

def card_create(request):
    form = CardForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        card = form.save()
        messages.success(request, "Card created successfully.")
        return redirect("card_detail", pk=card.pk)
    return render(request, "main/card_form.html", {"form": form, "page_title": "Create card"})

def card_update(request, pk):
    card = get_object_or_404(Card, pk=pk)
    form = CardForm(request.POST or None, instance=card)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Card updated successfully.")
        return redirect("card_detail", pk=card.pk)
    return render(request, "main/card_form.html", {"form": form, "page_title": "Edit card", "card": card})

def card_delete(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == "POST":
        card.delete()
        messages.success(request, "Card deleted.")
        return redirect("home")
    return render(request, "main/card_confirm_delete.html", {"card": card})

def tag_list(request):
    return render(request, "main/tag_list.html", {"tags": Tag.objects.prefetch_related("cards").all()})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag.objects.prefetch_related("cards__tags"), slug=slug)
    return render(request, "main/tag_detail.html", {"tag": tag})
