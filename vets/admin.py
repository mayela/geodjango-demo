from django.contrib import admin

from vets.models import Vet


@admin.register(Vet)
class VetAdmin(admin.ModelAdmin):
    readonly_fields = ('certification',)
    pass
