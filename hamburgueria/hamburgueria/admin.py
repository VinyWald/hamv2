from django.contrib import admin
from .models import Pedido, Pao, Carne, Opcionais

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'nome', 'pao', 'carne', 'dataPedido', 'status']
    list_filter = ['status', 'dataPedido']
    search_fields = ['cliente__username', 'nome']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.cliente = request.user
        obj.save()

admin.site.register(Pao)
admin.site.register(Carne)
admin.site.register(Opcionais)

