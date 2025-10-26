from rest_framework import serializers
from .models import Usuario
from .models import Medicamento
from .models import Pago
from .models import Beneficiario
from .models import Personal
from .models import Familiar
from .models import Patologia
from .models import Privilegio
from .models import Rol 
from .models import Historial_usuario
from .models import Cuidado
from .models import Usuario_beneficiario
from .models import Calle


class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = ['id', 'nombre_personal', 'apellido_personal', 'fecha_nacimiento', 'telefono', 'email', 'status', 'created_at', 'updated_at']
        read_only_fields = ('created_at',)

class UsuarioSerializer(serializers.ModelSerializer):
    fk_personal = PersonalSerializer(read_only=True)      
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'password', 'status', 'fk_personal', 'created_at', 'updated_at']
        read_only_fields = ('created_at',)
    
    def create(self, validated_data):
        return Usuario.objects.create(**validated_data)


class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = ['id', 'nombre_medicamento', 'presentacion', 'unidad_presentacion', 'status', 'created_at', 'updated_at']
        read_only_fields = ('created_at',)

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ['id', 'fecha', 'monto', 'tipo_pago', 'numero_referencia', 'banco', 'fk_beneficiario', 'status', 'created_at', 'updated_at']
        read_only_fields = ('created_at',)

class BeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiario
        fields = ['id', 'nombre_beneficiario', 'apellido_beneficiario', 'fecha_nacimiento', 'telefono', 'email', 'fk_usuario', 'status', 'created_at', 'updated_at']
        read_only_fields = ('created_at',)

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = ['id', 'nombre_familiar', 'apellido_familiar', 'fecha_nacimiento', 'telefono', 'email', 'status', 'created_at', 'updated_at']
        read_only_fields = ('created_at',)

class PatologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patologia
        fields = ['id', 'nombre_patologia', 'descripcion', 'status', 'created_at', 'updated_at']
        read_only_fields = ('created_at',)

class PrivilegioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Privilegio
        fields = ['id', 'nombre_privilegio', 'fk_rol', 'status', 'created_at', 'updated_at']
        read_only_fields = ('created_at',)

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'nombre_rol', 'status', 'created_at', 'updated_at']
        read_only_fields = ('created_at',)

class Historial_usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historial_usuario
        fields = ['id', 'fecha_inicio', 'fecha_fin', 'fk_usuario', 'fk_rol', 'status', 'created_at', 'updated_at']
        read_only_fields = ('created_at',)

class CuidadoSerializer(serializers.ModelSerializer):
    #fk_beneficiario = BeneficiarioSerializer(read_only=True, many=True)
    fk_patologia = PatologiaSerializer(read_only=True, many=True)
    fk_medicamento = MedicamentoSerializer(read_only=True, many=True)

    class Meta:
        model = Cuidado
        fields = ['id', 'dosis', 'fecha_inicio', 'fecha_fin', 'frecuencia', 'unidad_frecuencia', 'fk_beneficiario', 'status','fk_patologia', 'fk_medicamento', 'created_at', 'updated_at']
        read_only_fields = ('created_at',)

class Usuario_beneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario_beneficiario
        fields = ['id', 'fecha_inicio', 'fecha_fin', 'fk_usuario', 'fk_beneficiario', 'status', 'created_at', 'updated_at']
        read_only_fields = ('created_at',)

class CalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calle
        fields = ['id', 'direccion_calle', 'fk_beneficiario', 'status', 'created_at', 'updated_at']
        read_only_fields = ('created_at',)