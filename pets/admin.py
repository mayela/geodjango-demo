from django.contrib import admin

from pets.models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass
