from django.db import models


class Registro_pagamento(models.Model):
    AUTO = models.CharField(max_length=15)
    codigo_returno = models.CharField(max_length=3)
    mensagem_retorno = models.CharField(max_length=200)
    hora = models.CharField(max_length=10)
    mensagem_envio = models.CharField(max_length=200)
    date_file = models.CharField(max_length=10)


    def __str__(self):
        return self.AUTO


class Envio_notificacao(models.Model):
    AUTO = models.CharField(max_length=15)
    codigo_returno = models.CharField(max_length=3)
    mensagem_retorno = models.CharField(max_length=200, null=True)
    hora = models.CharField(max_length=10)
    mensagem_envio = models.CharField(max_length=200)
    date_file = models.CharField(max_length=10)
    proprietario = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.AUTO
