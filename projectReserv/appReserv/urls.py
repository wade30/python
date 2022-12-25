from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='acceuil'),
    # --------compagnie---------------------------------------
    path('compagnie/', list_compagnie, name='compagnie'),
    path('ajoutCompagnie/', created_compagnie, name='ajoutCompagnie'),
    path('updateCompagnie/<int:id>', updated_compagnie, name='updateCompagnie'),
    path('supprimerCompagnie/<int:id>', deleted_compagnie, name='supprimerCompagnie'),
    # ---------trajet-----------------------------------------
    path('trajet/', list_trajet, name='trajet'),
    path('ajoutTrajet/', created_trajet, name='ajoutTrajet'),
    path('updateTrajet/<int:id>', updated_trajet, name='updateTrajet'),
    path('supprimerTrajet/<int:id>', deleted_trajet, name='supprimerTrajet'),
    # ----------vol--------------------------------------------
    path('vol/', list_vol, name='vol'),
    path('ajoutVol/', created_vol, name='ajoutVol'),
    path('updateVol/<int:id>', updated_vol, name='updateVol'), 
    path('supprimerVol/<int:id>', deleted_vol, name='supprimerVol'),
    path('detail/<int:id>', detail_vol, name='detail')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
