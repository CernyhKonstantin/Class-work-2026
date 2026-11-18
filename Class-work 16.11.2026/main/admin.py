from django.contrib import admin
from .models import Card, Tag
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")
    search_fields = ("title",)
    filter_horizontal = ("tags",)
