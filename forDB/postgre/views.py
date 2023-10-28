# views.py

from django.shortcuts import render
from .models import Calendar, Allcolor, InventoryCt, Ord1

def index(request):
    return render(request, 'postgre/index.html')

def allcolor_list(request):
    allcolors = Allcolor.objects.all()
    return render(request, 'postgre/allcolor_list.html', {'allcolors': allcolors})

def inventoryct_list(request):
    inventory_cts = InventoryCt.objects.all()
    return render(request, 'postgre/inventoryct_list.html', {'inventory_cts': inventory_cts})

def ord1_list(request):
    ords = Ord1.objects.all()
    return render(request, 'postgre/ord1_list.html', {'ords': ords})

def calendar_list(request):
    calendars = Calendar.objects.all()
    return render(request, 'postgre/calendar_list.html', {'calendars': calendars})
