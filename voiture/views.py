from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from voiture.models import Voiture
from client.models import Client


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

#pour ajouter une voiture
def ajoutv_view(request):
    if request.method == 'POST':
        Marque = request.POST.get('Marque')
        Matricule = request.POST.get('Matricule')
        Prix = request.POST.get('Prix')
        image = request.FILES.get('image')  # Accéder au fichier téléchargé

        try:
            voiture = Voiture.objects.create(Marque=Marque, Matricule=Matricule, Pu=Prix, image=image)
            messages.success(request, f'Voiture {voiture.Marque} N° {voiture.Matricule} ajouté avec succès !')
        except IntegrityError as e:
            messages.error(request, 'Ce numéro matricule existe déjà.')

        return redirect('courses')  # Redirige vers une page après avoir ajouté le client
    return render(request, "Voiture/ajoutV.html")


def voiture_delete(request, voiture_id):
    voiture= get_object_or_404(Voiture, pk=voiture_id)
    voiture.delete()
    messages.success(request, f"La voiture marque: {voiture.Marque} N°: {voiture.Matricule} a été supprimé avec succès.")
    return redirect('courses')


def voiture_modify(request, voiture_id):
    voiture = get_object_or_404(Voiture, pk=voiture_id)

    if request.method == 'POST':
        new_matricule = request.POST.get('Matricule')
        new_marque = request.POST.get('Marque')
        new_prix = request.POST.get('Prix')
        image = request.FILES.get('image')
        try:
            voiture.Matricule = new_matricule
            voiture.Marque = new_marque
            voiture.Pu = new_prix
            voiture.save()
            messages.success(request, f'Voiture marque: {voiture.Marque} N°: {voiture.Matricule} modifié avec succès !')
        except IntegrityError as e:
            messages.error(request, 'Ce numéro de client existe déjà.')

        voiture.Matricule = new_matricule
        voiture.NomClient = new_marque
        voiture.AdrClient = new_prix
        voiture.image = image
        voiture.save()

        return redirect('courses')  # Redirigez où vous voulez après la modification

    return render(request, 'Voiture/modifV.html', {'voiture': voiture})




