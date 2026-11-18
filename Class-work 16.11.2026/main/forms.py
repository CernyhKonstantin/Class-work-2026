from django import forms
from .models import Card
class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ["title", "description", "tags"]
        widgets = {"title": forms.TextInput(attrs={"class":"form-control","placeholder":"Enter a card title"}), "description": forms.Textarea(attrs={"class":"form-control","rows":5}), "tags": forms.CheckboxSelectMultiple()}
