# urls.py
from django.contrib import admin
from django.urls import path
from myapp.views import index, allcolor_list, inventoryct_list, calendar_list, join_and_multiply,annotate_test,ct_ac_list,total_list, color_filter_list,color_filter_r1, graph
from myapp.views import ord2ac_list,ord3ac_list, ordNware, color_filter_r2
from myapp.views import ctcroom
from myapp.views import ctcroom_r1
from myapp.views import export_to_excel, model_data
from myapp.views import order_data_list
from myapp.views import ord_join_py
from myapp.views import ord_full_join, ord_join_sql, ord_union_sum






urlpatterns = [
    path('ctcroom/', ctcroom, name='ctcroom'),
]


urlpatterns = [
    path('', index, name='index'),
    path('allcolors/', allcolor_list, name='allcolor_list'),
    path('inventorycts/', inventoryct_list, name='inventoryct_list'),
    path('calendars/', calendar_list, name='calendar_list'),
    path('join/', join_and_multiply, name='join_and_multiply'),  # 이 부분을 추가합니다.
    path('annotate_test/', annotate_test, name='annotate_test'),  # 이 부분을 추가합니다.
    path('ct_acs/', ct_ac_list, name='ct_ac_list'),  # CtAc 모델의 데이터를 보여줄 URL 패턴을 추가
    path('totals/', total_list, name='total_list'),  # 새로운 URL 패턴 추가
    path('color_filter/', color_filter_list, name='color_filter_list'),  # 새로운 URL 패턴 추가
    path('color_filter_r1/', color_filter_r1, name='color_filter_r1'),
    path('graph/', graph, name='graph'),
    path('ord2acs/', ord2ac_list, name='ord2ac_list'),
    path('ord3acs/',ord3ac_list, name='ord3ac_list'),
    path('ordNware/', ordNware, name='ordNware'),
    path('color_filter_r2/', color_filter_r2, name='color_filter_r2'),  # Add URL pattern for color_filter_r2 view
    path('ctcroom/', ctcroom, name='ctcroom'),
    path('ctcroom_r1/', ctcroom_r1, name='ctcroom_r1'),
    path('export_to_excel/', export_to_excel, name='export_to_excel'),
    path('model_data/', model_data, name='model_data'),  # 추가
    path('orders/', order_data_list, name='order-data-list'),
    path('ord-join-py/', ord_join_py, name='ord_join_py'),
    path('ord-full-join/', ord_full_join, name='ord_full_join'),
    path('ord-join-sql/', ord_join_sql, name='ord-join-sql'),
    path('ord-union-sum/', ord_union_sum, name='ord-union-sum'),

]
