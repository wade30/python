from django.shortcuts import render, redirect, get_object_or_404

from .models import Trajet, Vol, Compagnie
from .forms import CompagnieForm

# -------request-----------
vol = Vol.objects.all()
trajet = Trajet.objects.all()
compagnie = Compagnie.objects.all()


# -------------------------------------------------------------------------------


# Create your views here.
def index(request):

    return render(request, 'index.html', {'vol': vol, 'trajet': trajet, 'compagnie': compagnie})


# -------------------------------------------------------------------------
# -------------------------------------------------------------------------


def list_compagnie(request):
    return render(request, 'compagnie/list_compagnie.html', {'compagnie': compagnie, 'vol': vol})


def created_compagnie(request):
    if request.method == "POST":
        form = CompagnieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("/compagnie/")
    form = CompagnieForm()
    return render(request=request, template_name='compagnie/ajout_compagnie.html', context={'form':form})

    #     logo = request.POST['logo']
    #     nom = request.POST['nom']
    #     compc = Compagnie.objects.create(
    #         nom=nom,
    #         logo=logo
    #     )
    #     compc.save()
    #     return redirect("/compagnie/")
    # return render(request, 'compagnie/ajout_compagnie.html')


def updated_compagnie(request, id):
    comp_up = get_object_or_404(Compagnie, id=id)
    form = CompagnieForm(instance=comp_up)
    if request.method == "POST":
        logo = request.POST['logo']
        nom = request.POST['nom']
        compc = Compagnie.objects.filter(pk=comp_up.id).update(
            nom=nom,
            logo=logo
        )
        return redirect("/compagnie/")
    return render(request, 'compagnie/update_compagnie.html', {'form': form})


def deleted_compagnie(request, id):
    comp_del = get_object_or_404(Compagnie, id=id)
    if request.method == "POST":
        comp_del = Compagnie.objects.filter(pk=comp_del.id).delete()
        return redirect("/compagnie/")
    return render(request, 'compagnie/deleted_compagnie.html', {'comp_del': comp_del})


# --------------------------------------------------------------------
# ----------------------------------------------------------------------

def list_trajet(request):
    return render(request, 'trajet/list_trajet.html', {'trajet': trajet, 'vol': vol})


def created_trajet(request):
    if request.method == "POST":
        depart = request.POST['depart']
        arrivee = request.POST['arrivee']
        trajetc = Trajet.objects.create(
            depart=depart,
            arrivee=arrivee
        )
        trajetc.save()
        return redirect("/trajet/")
    return render(request, 'trajet/ajout_trajet.html')


def updated_trajet(request, id):
    trajet_one = get_object_or_404(Trajet, id=id)
    if request.method == "POST":
        depart = request.POST['depart']
        arrivee = request.POST['arrivee']
        trajet_one = Trajet.objects.filter(pk=trajet_one.id).update(
            depart=depart,
            arrivee=arrivee
        )
        return redirect("/trajet/")
    return render(request, 'trajet/update_trajet.html', {'trajet_one': trajet_one})


def deleted_trajet(request, id):
    trajet_del = get_object_or_404(Trajet, id=id)
    if request.method == "POST":
        trajet_del = Trajet.objects.filter(pk=trajet_del.id).delete()
        return redirect("/trajet/")
    return render(request, 'trajet/deleted_trajet.html', {'trajet_del': trajet_del})

def detail_vol(request, id):
    trajet_detail = get_object_or_404(Trajet, id=id)
    return render(request, 'vol/get_vol.html', {'trajet_detail': trajet_detail})


# --------------------------------------------------------------------
# --------------------------------------------------------------------

def list_vol(request):
    return render(request, 'vol/list_vol.html', {'vol': vol})


def created_vol(request):
    if request.method == "POST":
        prix = request.POST['prix']
        date = request.POST['date']
        heure = request.POST['heure']
        trajetv = request.POST['trajet']
        compa = request.POST['compagnie']

        volc = Vol.objects.create(
            prix=prix,
            date=date,
            heure=heure,
            trajet_id=trajetv
        ).save()
        volc.compagnie.add(compa)
        return redirect("/vol/")
    return render(request, 'vol/ajout_vol.html', {'trajet': trajet, 'compagnie': compagnie})


def updated_vol(request, id):
    vol_up = get_object_or_404(Vol, pk=id)
    if request.method == "POST":
        prix = request.POST['prix']
        date = request.POST['date']
        heure = request.POST['heure']
        vol_up = Vol.objects.filter(pk=vol_up.id).update(
            prix=prix,
            date=date,
            heure=heure
        )
        return redirect("/vol/")
    return render(request, 'vol/update_vol.html', {'vol_up': vol_up})


def deleted_vol(request, id):
    vol_del = get_object_or_404(Vol, pk=id)
    if request.method == "POST":
        vol_del = Vol.objects.filter(pk=vol_del.id).delete()
    return render(request, 'vol/deleted_vol.html', {'vol_del': vol_del})


def detail_vol(request, id):
    vol_detail = get_object_or_404(Vol, id=id)
    return render(request, 'vol/get_vol.html', {'vol_detail': vol_detail})
