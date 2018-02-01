from django.contrib import admin

from hospitals.models import Hospital


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    readonly_fields = ('license',)
    pass
