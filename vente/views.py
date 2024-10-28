from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vente
from client.models import Client
from voiture.models import Voiture
from django.utils import timezone

def home(request):
    return render(request,"index.html")#Templates

#pour Lister les Clients
def client_view(request):
    listCli = Client.objects.all()
    context = {"ListCli":listCli}
    return render(request,"client.html", context)

def course_view(request):
    listV = Voiture.objects.all()
    context = {"ListV": listV}
    return render(request,"voiture.html", context)

def vente_view(request):
    vente = Client.objects.filter(vente__isnull=False).distinct()
    return render(request, 'vente.html', {'vente': vente})

def ajoutVente_view(request):
    if request.method == 'POST':
        # Récupérez les données du formulaire (peut varier en fonction de votre formulaire)
        client_id = request.POST.get('client_id')
        voiture_id = request.POST.get('voiture_id')

        client = Client.objects.get(pk=client_id)
        voiture = Voiture.objects.get(pk=voiture_id)

        vente = Vente(client=client, voiture=voiture, DateVente=timezone.now())
        vente.save()

        messages.success(request,f'Vente de la voiture {voiture.Matricule} au client {client.NomClient} ajoutée avec succès !')

        return redirect('vente')  # Redirigez où vous voulez après la création de la vente

    clients = Client.objects.all()
    voitures = Voiture.objects.all()

    return render(request, 'Vente/ajoutVente.html', {'clients': clients, 'voitures': voitures})

def vente_modify(request, id):
    vente = get_object_or_404(Vente, pk=id)

    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        voiture_id = request.POST.get('voiture_id')

        client = Client.objects.get(pk=client_id)
        voiture = Voiture.objects.get(pk=voiture_id)

        vente.client = client
        vente.voiture = voiture
        vente.DateVente = timezone.now()
        vente.save()
        messages.success(request, f'Vente de la voiture {voiture.Matricule} au client {client.NomClient} modifiée avec succès !')

        return redirect('vente')  # Redirigez où vous voulez après la modification

    clients = Client.objects.all()
    voiture = Voiture.objects.all()

    return render(request, 'Vente/modifV.html', {'vente': vente, 'clients': clients, 'voiture': voiture})

def vente_delete(request, id):
    vente = get_object_or_404(Vente, pk=id)
    vente.delete()
    messages.success(request,f'Vente supprimée avec succès !')
    return redirect('vente')  # Redirigez où vous voulez après la suppression
