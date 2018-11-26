from django.urls import path
from .views import Autolist


urlpatterns = [
    path('registro_pagamento', Autolist.as_view()),
]
