from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer
from .models import Medicamento
from .serializers import MedicamentoSerializer
from .models import Pago
from .serializers import PagoSerializer
from .models import Beneficiario
from .serializers import BeneficiarioSerializer
from .models import Personal
from .serializers import PersonalSerializer
from .models import Familiar
from .serializers import FamiliarSerializer
from .models import Patologia
from .serializers import PatologiaSerializer
from .models import Privilegio
from .serializers import PrivilegioSerializer
from .models import Rol
from .serializers import RolSerializer
from .models import Historial_usuario
from .serializers import Historial_usuarioSerializer
from .models import Cuidado
from .serializers import CuidadoSerializer
from .models import Usuario_beneficiario
from .serializers import Usuario_beneficiarioSerializer
from .models import Calle
from .serializers import CalleSerializer    
# Create your views here.

class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class BeneficiarioViewSet(viewsets.ModelViewSet):
    queryset = Beneficiario.objects.all()
    serializer_class = BeneficiarioSerializer



class FamiliarViewSet(viewsets.ModelViewSet):
    queryset = Familiar.objects.all()
    serializer_class = FamiliarSerializer

class PatologiaViewSet(viewsets.ModelViewSet):
    queryset = Patologia.objects.all()
    serializer_class = PatologiaSerializer

class PrivilegioViewSet(viewsets.ModelViewSet):
    queryset = Privilegio.objects.all()
    serializer_class = PrivilegioSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class Historial_usuarioViewSet(viewsets.ModelViewSet):
    queryset = Historial_usuario.objects.all()
    serializer_class = Historial_usuarioSerializer

class CuidadoViewSet(viewsets.ModelViewSet):
    queryset = Cuidado.objects.all()
    serializer_class = CuidadoSerializer

class Usuario_beneficiarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario_beneficiario.objects.all()
    serializer_class = Usuario_beneficiarioSerializer

class CalleViewSet(viewsets.ModelViewSet):
    queryset = Calle.objects.all()
    serializer_class = CalleSerializer

