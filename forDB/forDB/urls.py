# urls.py
from django.contrib import admin
from django.urls import path
from postgre.views import index, allcolor_list, inventoryct_list, ord1_list, calendar_list, join_and_multiply,annotate_test,ct_ac_list,total_list, color_filter_list,color_filter_r1, graph
from postgre.views import ord2ac_list,ord3ac_list, ordNware


urlpatterns = [
    path('', index, name='index'),
    path('allcolors/', allcolor_list, name='allcolor_list'),
    path('inventorycts/', inventoryct_list, name='inventoryct_list'),
    path('ord1s/', ord1_list, name='ord1_list'),
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

]
