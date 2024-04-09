from django.contrib import admin

from lab_software.models import Cliente, Pagamento

# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("id", "nome")


class PagamentoAdmin(admin.ModelAdmin):
    list_display = ("cliente", "data", "valor")
    search_fields = ("cliente", "data", "valor")


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pagamento, PagamentoAdmin)
