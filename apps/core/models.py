from django.contrib.auth.models import User
from django.db import models


class Pet(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    idade = models.IntegerField()
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    duracao_minutos = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    STATUS = (
        ('Pendente', 'Pendente'),
        ('Confirmado', 'Confirmado'),
        ('Cancelado', 'Cancelado'),
    )
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS, blank=False,
                              null=False)
    observacao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pet.nome


class ServicoRealizado(models.Model):
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    data_execucao = models.DateTimeField()
    observacao = models.TextField()
    avaliacao = models.IntegerField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.agendamento.pet.nome
