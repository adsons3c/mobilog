from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Registro_pagamento


class Autolist(ListView):
    model = Registro_pagamento
