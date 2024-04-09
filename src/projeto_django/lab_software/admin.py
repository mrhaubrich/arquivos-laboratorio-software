from django.contrib import admin
from django.db.models import Sum, Subquery, OuterRef

from lab_software.models import Cliente, Divida, Pagamento

# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("id", "nome")


class PagamentoAdmin(admin.ModelAdmin):
    list_display = ("cliente_id", "data", "valor")
    search_fields = ("data", "valor")


class DividaAdmin(admin.ModelAdmin):
    list_display = (
        "cliente",
        "data",
        "valor_total",
    )
    search_fields = ("cliente__nome", "valor_total")

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        subquery = (
            Divida.objects.filter(cliente=OuterRef("cliente"))
            .filter(pago=False)
            .values("cliente")
            .annotate(valor_total=Sum("valor"))
            .values("valor_total")
        )

        qs = (
            qs.filter(pago=False)
            .annotate(valor_total=Subquery(subquery))
            .distinct("cliente")
            .order_by("cliente")
        )

        return qs

    def valor_total(self, obj):
        return obj.valor_total


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pagamento, PagamentoAdmin)
admin.site.register(Divida, DividaAdmin)
