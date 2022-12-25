from django.contrib import admin

from .models import Trajet, Vol, Compagnie


# Register your models here.

class AdminTrajet(admin.ModelAdmin):
    list_display = ('depart', 'arrivee')


class AdminVol(admin.ModelAdmin):
    list_display = ('prix', 'date', 'heure', 'trajet')


class AdminCompagnie(admin.ModelAdmin):
    list_display = ('logo', 'nom')


admin.site.register(Trajet, AdminTrajet)
admin.site.register(Vol, AdminVol)
admin.site.register(Compagnie, AdminCompagnie)
