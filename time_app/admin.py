from django.contrib import admin
from .models import Profil, Localisation

# Register your models here.
class ProfilAdmin(admin.ModelAdmin):
    list_display=("user",)
    list_filter=("user",)
    search_fields=("user",)

class LocalisationAdmin(admin.ModelAdmin):
    list_display=("continent", "city")
    list_filter=("continent", "city")
    search_fields=("continent", "city")

admin.site.register(Profil, ProfilAdmin)
admin.site.register(Localisation, LocalisationAdmin)