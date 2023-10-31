# views.py

from django.shortcuts import render
from .models import Calendar, Allcolor, InventoryCt, Ord1

# views.py

from django.shortcuts import render
from django.db.models import Q
from .models import Calendar, Allcolor, InventoryCt, Ord1
from .models import CtAc  # CtAc 모델을 import

# ... (다른 뷰 함수들)
# views.py
from django.db.models import F  # F 객체를 import


def inventoryct_list(request):
    # InventoryCt와 Allcolor 모델을 Inner Join하여 unnamed_0 = string_field_1 조건으로 필터링
    result = InventoryCt.objects.filter(unnamed_0=F('allcolor__string_field_1'))

    return render(request, 'postgre/inventoryct_list.html', {'result': result})


def index(request):
    urls = {
        'All Colors': 'allcolor_list',
        'Inventory CTs': 'inventoryct_list',
        'ORD1s': 'ord1_list',
        'Calendars': 'calendar_list',
        'Join and Multiply': 'join_and_multiply',
        'Annotate Test': 'annotate_test',
        'CT ACs': 'ct_ac_list',
        'Total List': 'total_list',
        'Color Filter List': 'color_filter_list',
        'Color Filter R1': 'color_filter_r1',
        'Graph': 'graph',
    }
    return render(request, 'postgre/index.html', {'urls': urls})



def allcolor_list(request):
    allcolors = Allcolor.objects.all()
    return render(request, 'postgre/allcolor_list.html', {'allcolors': allcolors})

def ord1_list(request):
    ords = Ord1.objects.all()
    return render(request, 'postgre/ord1_list.html', {'ords': ords})

def calendar_list(request):
    calendars = Calendar.objects.all()
    return render(request, 'postgre/calendar_list.html', {'calendars': calendars})


# views.py
from django.shortcuts import render
from .models import Allcolor

def join_and_multiply(request):
    # Allcolor와 InventoryCt 테이블을 INNER JOIN 합니다.
    allcolors = Allcolor.objects.select_related('string_field_1').all()


    # 결과를 템플릿에 전달합니다.
    return render(request, 'postgre/join.html', {'allcolors': allcolors})


# views.py
from django.db.models import F
from django.shortcuts import render
from .models import Allcolor, InventoryCt

# views.py
from django.db.models import F
from django.shortcuts import render
from .models import Allcolor, InventoryCt

def annotate_test(request):
    allcolors = Allcolor.objects.annotate(
        total_on_hand=F('string_field_1__on_hand')
    )
    return render(request, 'postgre/annotate_test.html', {'allcolors': allcolors})

def ct_ac_list(request):
    ct_acs = CtAc.objects.all()  # CtAc 모델의 모든 데이터를 가져옴
    return render(request, 'postgre/ct_ac_list.html', {'ct_acs': ct_acs})  # 데이터를 템플릿에 전달

def total_list(request):
    ct_acs = CtAc.objects.all()  # CtAc 모델의 모든 데이터를 가져옴
    results = []
    for ct_ac in ct_acs:
        total = ct_ac.cbm * ct_ac.on_hand  # CBM과 On_hand 값을 곱하여 total에 저장
        results.append({
            'unnamed_0': ct_ac.unnamed_0,
            'color_code': ct_ac.color_code,
            'qty':ct_ac.on_hand,
            'cbm':ct_ac.cbm,
            'total': total,
        })
    return render(request, 'postgre/total_list.html', {'results': results})  # 데이터를 템플릿에 전달


from django.http import HttpResponseRedirect
from django.urls import reverse

def color_filter_list(request):
    ct_acs = CtAc.objects.all()  # CtAc 모델의 모든 데이터를 가져옴
    color_codes = CtAc.objects.values_list('color_code', flat=True).distinct()  # 중복되지 않는 color_code 값들을 가져옴
    selected_color = request.GET.get('color_code')  # URL에서 color_code 값을 가져옴
    if selected_color:
        ct_acs = ct_acs.filter(color_code=selected_color)  # 선택한 color_code에 해당하는 데이터만 필터링
    return render(request, 'postgre/color_filter_list.html', {
        'ct_acs': ct_acs,
        'color_codes': color_codes,
        'selected_color': selected_color,
    })


from django.db.models import F, Sum


def color_filter_list(request):
    ct_acs = CtAc.objects.all()  # CtAc 모델의 모든 데이터를 가져옴
    color_codes = CtAc.objects.values_list('color_code', flat=True).distinct()  # 중복되지 않는 color_code 값들을 가져옴
    selected_color = request.GET.get('color_code')  # URL에서 color_code 값을 가져옴
    if selected_color:
        ct_acs = ct_acs.filter(color_code=selected_color)  # 선택한 color_code에 해당하는 데이터만 필터링

    ct_acs = ct_acs.annotate(qtycbm=F('on_hand') * F('cbm'))  # on_hand와 cbm을 곱한 값을 qtycbm으로 추가

    total_qtycbm = {}
    for color_code in color_codes:
        total_qtycbm[color_code] = CtAc.objects.filter(color_code=color_code).aggregate(Sum('qtycbm'))['qtycbm__sum']

    return render(request, 'postgre/color_filter_list.html', {
        'ct_acs': ct_acs,
        'color_codes': color_codes,
        'selected_color': selected_color,
        'total_qtycbm': total_qtycbm,
    })


from django.db.models import F, Sum


def color_filter_r1(request):
    ct_acs = CtAc.objects.all()
    color_codes = CtAc.objects.values_list('color_code', flat=True).distinct()
    selected_color = request.GET.get('color_code')
    if selected_color:
        ct_acs = ct_acs.filter(color_code=selected_color)

    ct_acs = ct_acs.annotate(qtycbm=F('on_hand') * F('cbm'))

    total_qtycbm = {}
    for color_code in color_codes:
        filtered_ct_acs = CtAc.objects.filter(color_code=color_code)
        total = 0
        for ct_ac in filtered_ct_acs:
            total += ct_ac.on_hand * ct_ac.cbm
        total_qtycbm[color_code] = total

    return render(request, 'postgre/color_filter_r1.html', {
        'ct_acs': ct_acs,
        'color_codes': color_codes,
        'selected_color': selected_color,
        'total_qtycbm': total_qtycbm,
    })

def graph(request):
    ct_acs = CtAc.objects.all()
    color_codes = CtAc.objects.values_list('color_code', flat=True).distinct()

    total_qtycbm = {}
    for color_code in color_codes:
        filtered_ct_acs = CtAc.objects.filter(color_code=color_code)
        total = 0
        for ct_ac in filtered_ct_acs:
            total += ct_ac.on_hand * ct_ac.cbm
        total_qtycbm[color_code] = total

    return render(request, 'postgre/graph.html', {
        'color_codes': list(color_codes),
        'total_qtycbm': total_qtycbm,
    })

from .models import Ord2Ac

def ord2ac_list(request):
    ord2acs = Ord2Ac.objects.all()  # Ord2Ac 모델의 모든 데이터를 가져옴
    return render(request, 'postgre/ord2ac_list.html', {'ord2acs': ord2acs})

# views.py
from .models import Ord3Ac
def ord3ac_list(request):
    ord3acs = Ord3Ac.objects.all()
    total_pcs_cbm = 0
    for ord3ac in ord3acs:
        ord3ac.pcs_cbm = ord3ac.pcs * ord3ac.cbm
        total_pcs_cbm += ord3ac.pcs_cbm
    return render(request, 'postgre/ord3ac_list.html', {'ord3acs': ord3acs, 'total_pcs_cbm': total_pcs_cbm})


#이게 뭐야 의미가 없어 ㅎㅎㅎㅎㅎㅎㅎㅎㅎ 그냥 두 테이블 조인되는지?ㅎㅎ 잘 못 생각했어
from .models import Ord2Ac, CtAc
from django.db.models import Q
def ordNware(request):
    # Ord2Ac와 CtAc를 조인
    result = Ord2Ac.objects.filter(
        Q(item__in=CtAc.objects.values_list('item', flat=True))
    )
    # 결과를 템플릿에 전달
    return render(request, 'postgre/ordNware.html', {'results': result})
