from app import db

class Organizacion(db.Model):
    __tablename__ = 'organizaciones'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200))
    representante = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(100))
    observaciones = db.Column(db.Text)
    estado = db.Column(db.SmallInteger, nullable=False, default=1)
    fecha_creacion = db.Column(db.TIMESTAMP, server_default=db.func.now())
    fecha_actualizacion = db.Column(db.TIMESTAMP, server_default=db.func.now(), onupdate=db.func.now())
    creado_por = db.Column(db.Integer, nullable=False)  # Nuevo campo

    # Relación con Cliente
    clientes = db.relationship('Cliente', backref='organizacion', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'direccion': self.direccion,
            'representante': self.representante,
            'telefono': self.telefono,
            'email': self.email,
            'observaciones': self.observaciones,
            'estado': self.estado,
            'fecha_creacion': self.fecha_creacion.isoformat() if self.fecha_creacion else None,
            'fecha_actualizacion': self.fecha_actualizacion.isoformat() if self.fecha_actualizacion else None,
            'creado_por': self.creado_por
        }

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    organizacion_id = db.Column(db.Integer, db.ForeignKey('organizaciones.id'), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    identificacion = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(100))
    telefono = db.Column(db.String(20))
    rol = db.Column(db.String(50), nullable=False)
    foto = db.Column(db.String(255))
    estado = db.Column(db.SmallInteger, nullable=False, default=1)
    fecha_creacion = db.Column(db.TIMESTAMP, server_default=db.func.now())
    fecha_actualizacion = db.Column(db.TIMESTAMP, server_default=db.func.now(), onupdate=db.func.now())
    creado_por = db.Column(db.Integer, nullable=False)  # Nuevo campo
    usuario = db.Column(db.String(50), unique=True, nullable=False)  # Nuevo campo
    password = db.Column(db.String(255), nullable=False)  # Nuevo campo

    # Relación con Asistencia (como asistente)
    asistencias = db.relationship(
        'Asistencia',
        foreign_keys='Asistencia.cliente_id',
        back_populates='cliente',  # Usamos back_populates en lugar de backref
        lazy=True
    )
    
    # Método para convertir el objeto a un diccionario
    def to_dict(self):
        return {
            'id': self.id,
            'organizacion_id': self.organizacion_id,
            'nombre': self.nombre,
            'identificacion': self.identificacion,
            'correo': self.correo,
            'telefono': self.telefono,
            'rol': self.rol,
            'foto': self.foto,
            'estado': self.estado,
            'fecha_creacion': self.fecha_creacion.isoformat() if self.fecha_creacion else None,
            'fecha_actualizacion': self.fecha_actualizacion.isoformat() if self.fecha_actualizacion else None,
            'creado_por': self.creado_por,
            'usuario': self.usuario
        }

class Reunion(db.Model):
    __tablename__ = 'reuniones'
    id = db.Column(db.Integer, primary_key=True)
    organizacion_id = db.Column(db.Integer, db.ForeignKey('organizaciones.id'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    lugar = db.Column(db.String(200), nullable=False)
    tipo_reunion_id = db.Column(db.Integer, db.ForeignKey('tipos_reunion.id'), nullable=False)
    descripcion = db.Column(db.Text)
    estado = db.Column(db.SmallInteger, nullable=False, default=1)
    fecha_creacion = db.Column(db.TIMESTAMP, server_default=db.func.now())
    fecha_actualizacion = db.Column(db.TIMESTAMP, server_default=db.func.now(), onupdate=db.func.now())
    creado_por = db.Column(db.Integer, nullable=False)  # Nuevo campo

    # Relación con Asistencia
    asistencias = db.relationship(
        'Asistencia',
        back_populates='reunion',  # Usamos back_populates en lugar de backref
        lazy=True
    )
    
    def to_dict(self):
        return {
            'id': self.id,
            'organizacion_id': self.organizacion_id,
            'fecha': self.fecha.isoformat() if self.fecha else None,
            'hora': str(self.hora) if self.hora else None,
            'lugar': self.lugar,
            'tipo_reunion_id': self.tipo_reunion_id,
            'descripcion': self.descripcion,
            'estado': self.estado,
            'fecha_creacion': self.fecha_creacion.isoformat() if self.fecha_creacion else None,
            'fecha_actualizacion': self.fecha_actualizacion.isoformat() if self.fecha_actualizacion else None,
            'creado_por': self.creado_por
        }

class TipoReunion(db.Model):
    __tablename__ = 'tipos_reunion'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    estado = db.Column(db.SmallInteger, nullable=False, default=1)
    fecha_creacion = db.Column(db.TIMESTAMP, server_default=db.func.now())
    fecha_actualizacion = db.Column(db.TIMESTAMP, server_default=db.func.now(), onupdate=db.func.now())
    creado_por = db.Column(db.Integer, nullable=False)  # Nuevo campo
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'estado': self.estado,
            'fecha_creacion': self.fecha_creacion.isoformat() if self.fecha_creacion else None,
            'fecha_actualizacion': self.fecha_actualizacion.isoformat() if self.fecha_actualizacion else None,
            'creado_por': self.creado_por
        }

class Asistencia(db.Model):
    __tablename__ = 'asistencias'
    id = db.Column(db.Integer, primary_key=True)
    reunion_id = db.Column(db.Integer, db.ForeignKey('reuniones.id'), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    asistio = db.Column(db.Boolean, nullable=False, default=False)
    observaciones = db.Column(db.Text)
    estado = db.Column(db.SmallInteger, nullable=False, default=1)
    fecha_creacion = db.Column(db.TIMESTAMP, server_default=db.func.now())
    fecha_actualizacion = db.Column(db.TIMESTAMP, server_default=db.func.now(), onupdate=db.func.now())
    creado_por = db.Column(db.Integer, nullable=False)  # Nuevo campo

    # Relación con Reunion
    reunion = db.relationship(
        'Reunion',
        back_populates='asistencias'  # Usamos back_populates en lugar de backref
    )

    # Relación con Cliente (quien asiste)
    cliente = db.relationship(
        'Cliente',
        foreign_keys=[cliente_id],
        back_populates='asistencias'  # Usamos back_populates en lugar de backref
    )
    
    def to_dict(self):
        return {
            'id': self.id,
            'reunion_id': self.reunion_id,
            'cliente_id': self.cliente_id,
            'asistio': self.asistio,
            'observaciones': self.observaciones,
            'estado': self.estado,
            'fecha_creacion': self.fecha_creacion.isoformat() if self.fecha_creacion else None,
            'fecha_actualizacion': self.fecha_actualizacion.isoformat() if self.fecha_actualizacion else None,
            'creado_por': self.creado_por
        }