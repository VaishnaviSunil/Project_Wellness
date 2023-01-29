
from django.urls import path
from . import views
app_name='common'

urlpatterns = [
    path('',views.index),
    path('consumerlogin/',views.consumerlogin,name='consumerlogin'),
    path('sellerlogin/',views.sellerlogin,name='sellerlogin'),
]
