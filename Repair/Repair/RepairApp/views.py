from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from RepairApp.forms import RepairForm
from RepairApp.models import Repair


# Create your views here.
def index(request):
    repairss = Repair.objects.all()
    return render(request, 'index.html', {'repairss':repairss})

@login_required
def repairs(request):
    repair = Repair.objects.filter(user=request.user, car__type='Sedan')

    if request.method == 'POST':
        form = RepairForm(request.POST, request.FILES)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.user = request.user
            repair.save()
            return redirect('index')
    else:
        form = RepairForm()

    return render(request, 'repairs.html', {'form':form, 'repairs':repair})