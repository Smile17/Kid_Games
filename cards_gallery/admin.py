from django.contrib import admin
from .models import *


class CardAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Card._meta.fields
    ]  # all fields for the model


admin.site.register(Card, CardAdmin)


class CardItemAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in CardItem._meta.fields
    ]  # all fields for the model


admin.site.register(CardItem, CardItemAdmin)
