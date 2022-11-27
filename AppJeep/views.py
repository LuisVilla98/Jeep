from django.shortcuts import render,redirect
from AppJeep.models import Jeeps
from . import forms
from AppJeep.forms import Registrojeep

# Create your views here.
def JeepTemplates(request):
    jeep = Jeeps.objects.all()
    data = {'Jeeps': jeep}
    return render(request,'AppJeep/AppJeep.html',data)

def RegistroViews(request):
    form = forms.Registrojeep
    if request.method == 'POST':
        form = forms.Registrojeep(request.POST)
        if form.is_valid():
            form.save()
        return JeepTemplates(request)   
    data = {'form':form}
    return render(request,'AppJeep/Registrojeep.html',data)

def eliminarJeeps(request, id):
    jeeps = Jeeps.objects.get(id = id)
    jeeps.delete()
    return redirect('/Jeeps')

def actualizarJeeps(request,id):
    jeeps = Jeeps.objects.get(id = id)
    form = Registrojeep(instance=jeeps)
    if request.method == 'POST':
        form = Registrojeep(request.POST, instance=jeeps)
        if form.is_valid():
            form.save()
        return JeepTemplates(request)
    data = {'form':form}
    return render(request,'AppJeep/Registrojeep.html',data)        
    








