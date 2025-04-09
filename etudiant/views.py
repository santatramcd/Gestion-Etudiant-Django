from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

#Create your views here
#Cette fonction permet d'ajouter et d'afficher les informations
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()  # Réinitialise le formulaire après l'enregistrement
    else:
        fm = StudentRegistration()  # Formulaire vide pour une requête GET
    
    # Toujours définir stud, que ce soit POST ou GET
    stud = User.objects.all()
    
    # Rendre le template avec le formulaire et la liste des étudiants
    return render(request, 'etudiant/addandshow.html', {'form': fm, 'stu': stud})

#Cette fonction permet de modifier les informations
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk = id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'etudiant/updatestudent.html',{'form': fm})
    
#Cette fonction permet de supprimer les données
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
