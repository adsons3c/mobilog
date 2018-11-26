from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Registro_pagamento, Envio_notificacao
from django.views.generic.detail import DetailView


class Autolist(ListView):
    model = Registro_pagamento

class Envio_notificacao(ListView):
    model = Envio_notificacao


class AutoDetail(DetailView):
    model = Registro_pagamento
