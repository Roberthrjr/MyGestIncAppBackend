from django.db import models

class Sede(models.Model):
    descripcion = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Sede'
        verbose_name_plural = 'Sedes'

    def __str__(self):
        return self.descripcion

class Area(models.Model):
    descripcion = models.CharField(max_length=255)
    sede =models.ForeignKey(Sede, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

    def __str__(self):
        return self.descripcion

class Cargo(models.Model):
    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.descripcion

class Usuario(models.Model):
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    tipo_doc = models.CharField(max_length=50)
    numero_doc = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    usuario = models.CharField(max_length=255)
    clave = models.CharField(max_length=255)
    foto = models.CharField(max_length=255, null=True, blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(max_length=50, choices=[('usuario', 'Usuario'), ('tecnico', 'Tecnico'), ('administrador', 'Administrador')])
    estado = models.CharField(max_length=50, default='activo')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

class Categoria(models.Model):
    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.descripcion

class Componente(models.Model):
    descripcion = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    numero_serie = models.CharField(max_length=255)
    stock = models.IntegerField()
    foto = models.CharField(max_length=255, null=True, blank=True)
    fecha_compra = models.DateField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Componente'
        verbose_name_plural = 'Componentes'

    def __str__(self):
        return f'{self.descripcion} {self.marca} {self.modelo}'

class Programa(models.Model):
    descripcion = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    licencia = models.CharField(max_length=255)
    foto = models.CharField(max_length=255, null=True, blank=True)
    stock = models.IntegerField()
    fecha_compra = models.DateField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'

    def __str__(self):
        return f'{self.descripcion} {self.marca}'

class Periferico(models.Model):
    descripcion = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    numero_serie = models.CharField(max_length=255)
    stock = models.IntegerField()
    foto = models.CharField(max_length=255, null=True, blank=True)
    fecha_compra = models.DateField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Periferico'
        verbose_name_plural = 'Perifericos'

    def __str__(self):
        return f'{self.descripcion} {self.marca} {self.modelo}'

class Equipo(models.Model):
    codigo_patrimonial = models.CharField(max_length=255)
    presentacion = models.CharField(max_length=255)
    nombre_equipo = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    foto = models.CharField(max_length=255, null=True, blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    fecha_compra = models.DateField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

    def __str__(self):
        return f'{self.codigo_patrimonial} {self.presentacion}'

class Red(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    tipo_conexion = models.CharField(max_length=50, choices=[('ethernet', 'Ethernet'), ('wifi', 'WiFi')])
    direccion_ip = models.CharField(max_length=255)
    grupo_trabajo = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Red'
        verbose_name_plural = 'Redes'

    def __str__(self):
        return f'{self.grupo_trabajo} {self.direccion_ip}'

class Incidencia(models.Model):
    codigo_incidencia = models.CharField(max_length=255, unique=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario_incidencia')
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    descripcion = models.TextField()
    estado = models.CharField(max_length=50, choices=[('Enviado', 'Enviado'), ('Recibido', 'Recibido'), ('En Proceso', 'En Proceso'), ('Servicio Realizado', 'Servicio Realizado'), ('Finalizado', 'Finalizado')])
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Incidencia'
        verbose_name_plural = 'Incidencias'

    def __str__(self):
        return f'{self.codigo_incidencia} {self.descripcion}'

class HistorialEstado(models.Model):
    incidencia = models.ForeignKey(Incidencia, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tecnico_historial')
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Historial de Estado'
        verbose_name_plural = 'Historial de Estados'

    def __str__(self):
        return f'{self.incidencia} {self.usuario} {self.equipo}'

class Valoracion(models.Model):
    incidencia = models.ForeignKey(Incidencia, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario_valoracion')
    calificacion = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Valoracion'
        verbose_name_plural = 'Valoraciones'

    def __str__(self):
        return f'{self.incidencia} {self.usuario} {self.calificacion}'
