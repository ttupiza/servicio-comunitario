from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Medicamento)
admin.site.register(Pago)
admin.site.register(Beneficiario)
admin.site.register(Personal)
admin.site.register(Familiar)
admin.site.register(Patologia)
admin.site.register(Privilegio)
admin.site.register(Rol)
admin.site.register(Historial_usuario)
admin.site.register(Cuidado)
admin.site.register(Usuario_beneficiario)
admin.site.register(Calle)