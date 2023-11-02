# views.py

from django.shortcuts import render
from myapp.models import Calendar, Allcolor, InventoryCt

# views.py

from django.shortcuts import render
from django.db.models import Q
from .models import Calendar, Allcolor, InventoryCt
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
        ' All Colors': 'allcolor_list',
        'Inventory CTs': 'inventoryct_list',
        'Calendars': 'calendar_list',
        'Join and Multiply': 'join_and_multiply',
        'Annotate Test': 'annotate_test',
        'CT ACs': 'ct_ac_list',
        'Total List': 'total_list',
        'Color Filter List': 'color_filter_list',
        'Color Filter R1': 'color_filter_r1',
        'Graph': 'graph',
        'ORD2ACs': 'ord2ac_list',
        'ORD3ACs': 'ord3ac_list',
        'ORDNware': 'ordNware',
        'CTC Room': 'ctcroom',
        'CTC Room R1': 'ctcroom_r1',
        'Export to Excel': 'export_to_excel',
        'Model Data': 'model_data',  # 추가
    }
    return render(request, 'index.html', {'urls': urls})



def allcolor_list(request):
    allcolors = Allcolor.objects.all()
    return render(request, 'allcolor_list.html', {'allcolors': allcolors})



def calendar_list(request):
    calendars = Calendar.objects.all()
    return render(request, 'calendar_list.html', {'calendars': calendars})


# views.py
from django.shortcuts import render
from .models import Allcolor

def join_and_multiply(request):
    # Allcolor와 InventoryCt 테이블을 INNER JOIN 합니다.
    allcolors = Allcolor.objects.select_related('string_field_1').all()


    # 결과를 템플릿에 전달합니다.
    return render(request, 'join.html', {'allcolors': allcolors})


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
    return render(request, 'annotate_test.html', {'allcolors': allcolors})

def ct_ac_list(request):
    ct_acs = CtAc.objects.all()  # CtAc 모델의 모든 데이터를 가져옴
    return render(request, 'ct_ac_list.html', {'ct_acs': ct_acs})  # 데이터를 템플릿에 전달

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
    return render(request, 'total_list.html', {'results': results})  # 데이터를 템플릿에 전달


from django.http import HttpResponseRedirect
from django.urls import reverse

def color_filter_list(request):
    ct_acs = CtAc.objects.all()  # CtAc 모델의 모든 데이터를 가져옴
    color_codes = CtAc.objects.values_list('color_code', flat=True).distinct()  # 중복되지 않는 color_code 값들을 가져옴
    selected_color = request.GET.get('color_code')  # URL에서 color_code 값을 가져옴
    if selected_color:
        ct_acs = ct_acs.filter(color_code=selected_color)  # 선택한 color_code에 해당하는 데이터만 필터링
    return render(request, 'color_filter_list.html', {
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

    return render(request, 'color_filter_list.html', {
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

    return render(request, 'color_filter_r1.html', {
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

    return render(request, 'graph.html', {
        'color_codes': list(color_codes),
        'total_qtycbm': total_qtycbm,
    })

from .models import Ord2Ac

def ord2ac_list(request):
    ord2acs = Ord2Ac.objects.all()  # Ord2Ac 모델의 모든 데이터를 가져옴
    return render(request, 'ord2ac_list.html', {'ord2acs': ord2acs})

# views.py
from .models import Ord3Ac
def ord3ac_list(request):
    ord3acs = Ord3Ac.objects.all()
    total_pcs_cbm = 0
    for ord3ac in ord3acs:
        ord3ac.pcs_cbm = ord3ac.pcs * ord3ac.cbm
        total_pcs_cbm += ord3ac.pcs_cbm
    return render(request, 'ord3ac_list.html', {'ord3acs': ord3acs, 'total_pcs_cbm': total_pcs_cbm})


#이게 뭐야 의미가 없어 ㅎㅎㅎㅎㅎㅎㅎㅎㅎ 그냥 두 테이블 조인되는지?ㅎㅎ 잘 못 생각했어
from .models import Ord2Ac, CtAc
from django.db.models import Q
def ordNware(request):
    # Ord2Ac와 CtAc를 조인git
    result = Ord2Ac.objects.filter(
        Q(item__in=CtAc.objects.values_list('item', flat=True))
    )
    # 결과를 템플릿에 전달
    return render(request, 'ordNware.html', {'results': result})

from django.http import HttpResponse
import openpyxl
from django.db.models import F, Sum


def color_filter_r2(request):
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

    # 엑셀 파일 생성 및 작성
    if 'download' in request.GET:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(['Color Code', 'On Hand', 'CBM', 'Quantity * CBM'])
        for ct_ac in ct_acs:
            ws.append([ct_ac.color_code, ct_ac.on_hand, ct_ac.cbm, ct_ac.qtycbm])

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=color_filter_r2.xlsx'
        wb.save(response)
        return response

    return render(request, 'color_filter_r2.html', {
        'ct_acs': ct_acs,
        'color_codes': color_codes,
        'selected_color': selected_color,
        'total_qtycbm': total_qtycbm,
    })

from .models import CtRoomStatus
def ctcroom(request):
    data = CtRoomStatus.objects.all()
    context = {'data': data}
    return render(request, 'ctcroom.html', context)



# views.py

from django.shortcuts import render
from .models import CtRoomStatus

from django.db.models import F

def ctcroom_r1(request):
    data = CtRoomStatus.objects.all()
    zeroCBM_sum = 0
    for row in data:
        row.on_hand_diff = row.ny - row.on_hand if row.ny and row.on_hand else None
        row.zero = 0 if row.on_hand_diff and row.on_hand_diff > 0 else row.on_hand_diff
        row.zeroCBM = row.zero * row.cbm if row.zero is not None and row.cbm is not None else None
        if row.zeroCBM is not None:
            zeroCBM_sum += row.zeroCBM
    context = {'data': data, 'zeroCBM_sum': zeroCBM_sum}
    return render(request, 'ctcroom_r1.html', context)


import io
from openpyxl import Workbook
from django.http import FileResponse


def export_to_excel(request):
    data = CtRoomStatus.objects.all()

    output = io.BytesIO()
    wb = Workbook()
    ws = wb.active

    headers = ['CBM', 'Item', 'Total', 'NY', 'NJ4_2', 'CT', 'PA1_7', 'Num', 'On Hand', 'Date', 'NY - On Hand', 'Zero',
               'ZeroCBM']
    ws.append(headers)

    zeroCBM_sum = 0
    for row in data:
        on_hand_diff = row.ny - row.on_hand if row.ny and row.on_hand else None
        zero = 0 if on_hand_diff and on_hand_diff > 0 else on_hand_diff
        zeroCBM = zero * row.cbm if zero is not None and row.cbm is not None else None
        if zeroCBM is not None:
            zeroCBM_sum += zeroCBM

        row_data = [row.cbm, row.item, row.total, row.ny, row.nj4_2, row.ct, row.pa1_7, row.num, row.on_hand, row.date,
                    on_hand_diff, zero, zeroCBM]
        ws.append(row_data)

    ws.append([''] * 12 + [zeroCBM_sum])

    wb.save(output)
    output.seek(0)

    filename = 'ct_room_status.xlsx'
    response = FileResponse(output, as_attachment=True, filename=filename)
    return response

from django.shortcuts import render
from .models import Po300, Po301

def model_data(request):
    model_name = request.GET.get('model_name')
    data = None
    if model_name == 'Po300':
        data = Po300.objects.all()
    elif model_name == 'Po301':
        data = Po301.objects.all()
    return render(request, 'model_data.html', {'data': data, 'model_name': model_name})

from .models import Cw2Order
from django.shortcuts import render
from .models import Cw2Order

def order_data_list(request):
    orders = Cw2Order.objects.all()
    total1 = sum(order.o305 * order.cbm for order in orders if order.o305 is not None and order.cbm is not None)
    total2 = sum(order.o306 * order.cbm for order in orders if order.o306 is not None and order.cbm is not None)
    total3 = sum(order.o307 * order.cbm for order in orders if order.o307 is not None and order.cbm is not None)
    total4 = sum(order.o308 * order.cbm for order in orders if order.o308 is not None and order.cbm is not None)
    total5 = sum(order.o309 * order.cbm for order in orders if order.o309 is not None and order.cbm is not None)
    total6 = sum(order.o342 * order.cbm for order in orders if order.o342 is not None and order.cbm is not None)
    total7 = sum(order.o344 * order.cbm for order in orders if order.o344 is not None and order.cbm is not None)
    total8 = sum(order.o346 * order.cbm for order in orders if order.o346 is not None and order.cbm is not None)
    return render(request, 'order_data_list.html', {'orders': orders,  'orders': orders,
    'total1': total1,
    'total2': total2,
    'total3': total3,
    'total4': total4,
    'total5': total5,
    'total6': total6,
    'total7': total7,
    'total8': total8,})



