from django.urls import path
from .views import Autolist, Envio_notificacao, AutoDetail

app_name="log"
urlpatterns = [
    path('registro_pagamento', Autolist.as_view()),
    path('envio_notificacao', Envio_notificacao.as_view()),
    path('registro_detalhes/<int:pk>', AutoDetail.as_view(), name='registro_detalhes'),
]
