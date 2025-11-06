from django.contrib import admin

from .models import Pet, Servico, Agendamento, ServicoRealizado


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especie', 'raca', 'idade', 'tutor')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco', 'duracao_minutos')


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('pet', 'servico', 'data', 'status', 'observacao')


@admin.register(ServicoRealizado)
class ServicoRealizadoAdmin(admin.ModelAdmin):
    list_display = ('agendamento', 'pet', 'servico', 'data_execucao',
                    'observacao', 'avaliacao')
