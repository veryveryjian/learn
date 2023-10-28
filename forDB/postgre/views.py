# views.py

from django.shortcuts import render
from .models import Calendar, Allcolor, InventoryCt, Ord1

# views.py

from django.shortcuts import render
from django.db.models import Q
from .models import Calendar, Allcolor, InventoryCt, Ord1

# ... (다른 뷰 함수들)
# views.py
from django.db.models import F  # F 객체를 import


def inventoryct_list(request):
    # InventoryCt와 Allcolor 모델을 Inner Join하여 unnamed_0 = string_field_1 조건으로 필터링
    result = InventoryCt.objects.filter(unnamed_0=F('allcolor__string_field_1'))

    return render(request, 'postgre/inventoryct_list.html', {'result': result})


def index(request):
    return render(request, 'postgre/index.html')

def allcolor_list(request):
    allcolors = Allcolor.objects.all()
    return render(request, 'postgre/allcolor_list.html', {'allcolors': allcolors})

def ord1_list(request):
    ords = Ord1.objects.all()
    return render(request, 'postgre/ord1_list.html', {'ords': ords})

def calendar_list(request):
    calendars = Calendar.objects.all()
    return render(request, 'postgre/calendar_list.html', {'calendars': calendars})




