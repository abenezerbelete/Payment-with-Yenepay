from django.urls import path
from .views import payment, success, cancel, ipn

urlpatterns = [
    path('', payment, name='payment'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
    path('ipn/', ipn, name='ipn'),
]