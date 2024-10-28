from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from client.models import Client

def home(request):
    return render(request,"index.html")#Templates

#pour Lister les Clients
def client_view(request):
    listCli = Client.objects.all()
    context = {"ListCli":listCli}
    return render(request,"client.html",context)

def course_view(request):
    return render(request,"voiture.html")

#pour ajouter un client
def ajout_view(request):
    if request.method == 'POST':
        NomCli = request.POST.get('NomCli')
        NumCli = request.POST.get('NumCli')
        AdrCli = request.POST.get('AdrCli')

        try:
            client = Client.objects.create(NumClient=NumCli, NomClient=NomCli, AdrClient=AdrCli)
            messages.success(request, f'Client {client.NomClient} ajouté avec succès !')
        except IntegrityError as e:
            messages.error(request, 'Ce numéro de client existe déjà.')

        return redirect('client')  # Redirige vers une page après avoir ajouté le client
    return render(request, "Client/ajoutCli.html")

def client_delete(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    messages.success(request, f"Le client {client.NomClient} a été supprimé avec succès.")
    client.delete()
    return redirect('client')



def client_modify(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    if request.method == 'POST':
        new_num = request.POST.get('NumCli')
        new_nom = request.POST.get('NomCli')
        new_adr = request.POST.get('AdrCli')

        try:
            client.NumClient = new_num
            client.NomClient = new_nom
            client.AdrClient = new_adr
            client.save()
            messages.success(request, f'Client {client.NomClient} modifié avec succès !')
        except IntegrityError as e:
            messages.error(request, 'Ce numéro de client existe déjà.')

        return redirect('client')  # Redirige vers la liste des clients après modification

    return render(request, 'Client/client_modify.html', {'client': client})

def search_client(request):
    query = request.GET.get('q')  # Récupérer le terme de recherche depuis les paramètres GET
    clients = []

    if query:
        clients = Client.objects.filter(NomClient__icontains=query)

    context = {
        'query': query,
        'clients': clients,
    }

    return render(request, 'Client/recherche.html', context)

