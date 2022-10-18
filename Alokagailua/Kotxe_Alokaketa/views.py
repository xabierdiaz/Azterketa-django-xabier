from django.shortcuts import render
from django.urls import reverse

from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.
# datuak ikusi
def index(request):
    kotx = Kotxea.objects.all()    #lo coge del models.py
    return render(request, 'index.html', {'kotx': kotx})

#sartu kotxeak
def kotxeak_add(request):
    perts = Pertsona.objects.all() # lo coge del models.py
    return render(request, 'kotxeak_add.html', {'perts': perts})

def kotxeak_addrecord(request):
    x = request.POST['modeloa']
    y = request.POST['kolorea']
    z = request.POST['alokatzedata']
    p = request.POST['pertsona']
    perts_ob = Pertsona.objects.get(id=p)

    kotx = Kotxea(modeloa=x, kolorea=y, alokatzedata=z, pertsona=perts_ob)  # coge el modelo de models.py con los valores (platera y kopurua) que nosotros hemos introducido por add.html
    kotx.save()
    return HttpResponseRedirect(reverse('index'))

#kotxea ezabatu
def delete(request, id):
    kotx = Kotxea.objects.get(id=id)
    kotx.delete()
    return HttpResponseRedirect(reverse('index'))

#kotxea aldatu
def kotxea_update(request, id):
    kotx = Kotxea.objects.get(id=id)
    perts = Pertsona.objects.all()

    template = loader.get_template('kotxea_update.html')
    context = {
        'kotx': kotx,
        'perts' : perts,
    }
    return HttpResponse(template.render(context, request))


def kotxea_updaterecord(request, id):
    mod = request.POST['modeloa']
    kol = request.POST['kolorea']
    alok = request.POST['alokatzedata']
    per = request.POST['pertsona']

    pertsona_ob = Pertsona.objects.get(id=per)
    kotx = Kotxea.objects.get(id=id)

    kotx.modeloa = mod
    kotx.kolorea = kol
    kotx.alokatzedata = alok
    kotx.pertsona = pertsona_ob
    kotx.save()
    return HttpResponseRedirect(reverse('index'))

#pertsona
def pertsona_add(request):
    per = Pertsona.objects.all() 
    return render(request, 'pertsona_add.html', {'per': per})

def pertsona_addrecord(request):
  x = request.POST['izena']
  y = request.POST['abizena']
  perts = Pertsona(izena=x, abizena=y) 
  perts.save()
  return HttpResponseRedirect(reverse('index'))

def pertsona_delete(request, id):
    per = Pertsona.objects.get(id=id)
    per.delete()
    return HttpResponseRedirect(reverse('pertsona_add'))

def pertsona_update(request, id):
    per = Pertsona.objects.get(id=id)

    template = loader.get_template('pertsona_update.html')
    context = {
        'per': per,
    }
    return HttpResponse(template.render(context, request))

def pertsona_updaterecord(request, id):
    izen = request.POST['izena']
    abize = request.POST['abizena']

    pe = Pertsona.objects.get(id=id)

    pe.izena = izen
    pe.abizena = abize
    pe.save()
    return HttpResponseRedirect(reverse('pertsona_add'))