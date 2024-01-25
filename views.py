# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Mechine,Runned
from .forms import MechineForm
from django.contrib.auth import authenticate, login as auth_login


def login(request):
    return render(request,'Board/login.html')
def dashboard(request):
    mechins = Mechine.objects.all()
    runned = Runned.objects.all()
    total_mechin=mechins.count()
    mechins_on=runned.filter(status='Mechine on').count()
    mechins_off=runned.filter(status='Mechine off').count()
    mechins_outof=runned.filter(status='Mechine outoff service').count()


    context = {
        'mechins': mechins,
        'runned': runned,
        'total_mechin':total_mechin,
        'mechins_on':mechins_on,
        'mechins_off':mechins_off,
        'mechins_outof':mechins_outof,


    }
    return render(request, 'Board/dashboard.html', context)

def mechine(request):
    rmechin= Mechine.objects.all()
    rumechin= Runned.objects.all()
    context = {
        'rmechin': rmechin,
        'rumechin': rumechin,
    }

    return  render(request,'Board/machin.html',context)


def createMechine(request):
    form = MechineForm()

    if request.method == "POST":
        form = MechineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')


    context = {'form': form}
    return render(request, 'Board/create_mechin.html', context)


def updateMechine(request, pk):
    mechin = get_object_or_404(Mechine, mechin_id=pk)
    form = MechineForm(instance=mechin)
    if request.method == "POST":
        form = MechineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')

    context = {
        'form': form,
    }
    return render(request, 'Board/create_mechin.html', context)





def deleteMechin(request, pk):
    mechin = get_object_or_404(Mechine, mechin_id=pk)

    if request.method == "POST":
        confirm_delete = request.POST.get("confirm")
        if confirm_delete:
            mechin.delete()
            return redirect('Home')

    context = {'mechin': mechin}
    return render(request, 'Board/delete.html', context)

def update_delete_Mechine(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        selected_mechins = request.POST.getlist('selected_mechins')

        if action == 'update':
            # Handle the update action for each selected item
            for mechin_id in selected_mechins:
                return updateMechine(request, mechin_id)

        elif action == 'delete':
            # Handle the delete action for each selected item
            for mechin_id in selected_mechins:
                return deleteMechin(request, mechin_id)

    # Redirect to the dashboard after processing
    return redirect('Home')

