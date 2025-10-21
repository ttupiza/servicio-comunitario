from django.db import models

# Create your models here.

class Personal(models.Model):
    nombre_personal=models.CharField(max_length=15)
    apellido_personal=models.CharField(max_length=15)
    fecha_nacimiento=models.DateField()
    telefono=models.CharField(max_length=11)
    email=models.CharField(max_length=15)

    def _str_(self):
        return self.nombre_personal
    
    
class Usuario(models.Model):
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=30)
    status=models.BooleanField(default=True)
    fk_personal=models.OneToOneField(Personal, on_delete=models.CASCADE,related_name='usuario_personal',null=True)

    def _str_(self):
        return self.username
    
class Medicamento(models.Model):
    nombre_medicamento=models.CharField(max_length=20)
    presentacion=models.CharField(max_length=10)
    unidad_presentacion=models.FloatField()
    def _str_(self):
        return self.nombre_medicamento
    
class Beneficiario(models.Model):
    nombre_beneficiario=models.CharField(max_length=15)
    apellido_beneficiario=models.CharField(max_length=15)
    fecha_nacimiento=models.DateField()
    telefono=models.CharField(max_length=11)
    email=models.CharField(max_length=15)
    status=models.BooleanField(default=True)
    fk_usuario=models.OneToOneField(Usuario, on_delete=models.CASCADE,related_name='beneficiario_usuario',null=True)
        
    def _str_(self):
        return self.nombre_beneficiario

class Pago(models.Model):
    fecha=models.DateField()
    monto=models.FloatField()
    tipo_pago=models.CharField(max_length=15)
    numero_referencia=models.CharField(max_length=20)
    banco=models.CharField(max_length=15)
    status=models.BooleanField(default=True)
    fk_beneficiario=models.OneToOneField(Beneficiario, on_delete=models.CASCADE,related_name='pago_beneficiario',null=True)
    def _str_(self):
        return self.numero_referencia
    
class Familiar(models.Model):
    nombre_familiar=models.CharField(max_length=15)
    apellido_familiar=models.CharField(max_length=15)
    fecha_nacimiento=models.DateField()
    telefono=models.CharField(max_length=11)
    email=models.CharField(max_length=15)

    def _str_(self):
        return self.nombre_familiar

class Patologia(models.Model):
    nombre_patologia=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=100)

    def _str_(self):
        return self.nombre_patologia
    
class Privilegio(models.Model):
    nombre_privilegio=models.CharField(max_length=20)
    status=models.BooleanField(default=True)
    fk_rol=models.OneToOneField('Rol', on_delete=models.CASCADE,related_name='privilegio_rol',null=True)
    

    def _str_(self):
        return self.nombre_privilegio  

class Rol(models.Model):
    nombre_rol=models.CharField(max_length=20)

    def _str_(self):
        return self.nombre_rol

class Historial_usuario(models.Model):
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()
    status=models.BooleanField(default=True)
    fk_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name='historial_usuario_usuario',null=True)
    fk_rol=models.ForeignKey(Rol, on_delete=models.CASCADE,related_name='historial_usuario_rol',null=True)


    def _str_(self):
        return self.descripcion
    
class Cuidado(models.Model):
    dosis=models.FloatField()
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()
    frecuencia=models.FloatField()
    unidad_frecuencia=models.CharField(max_length=2)
    status=models.BooleanField(default=True)
    fk_beneficiario=models.ForeignKey(Beneficiario, on_delete=models.CASCADE,related_name='cuidado_beneficiario',null=True)
    fk_patologia=models.ForeignKey(Patologia, on_delete=models.CASCADE,related_name='cuidado_patologia',null=True)
    fk_medicamento=models.ForeignKey(Medicamento, on_delete=models.CASCADE,related_name='cuidado_medicamento',null=True)

    def _str_(self):
        return f"Dosis: {self.dosis} - Frecuencia: {self.frecuencia}{self.unidad_frecuencia}"

class Usuario_beneficiario(models.Model):
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()
    status=models.BooleanField(default=True)
    fk_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name='usuario_beneficiario_usuario',null=True)
    fk_beneficiario=models.ForeignKey(Beneficiario, on_delete=models.CASCADE,related_name='usuario_beneficiario_beneficiario',null=True)
    def _str_(self):
        return f"Usuario-Beneficiario from {self.fecha_inicio} to {self.fecha_fin}"

class Calle(models.Model):
    direccion_calle=models.CharField(max_length=30)
    status=models.BooleanField(default=True)
    fk_beneficiario=models.OneToOneField(Beneficiario, on_delete=models.CASCADE,related_name='calle_beneficiario',null=True)

    def _str_(self):
        return self.direccion_calle
