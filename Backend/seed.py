from app import create_app, db
from app.models import Organizacion, Cliente, Reunion, TipoReunion, Asistencia
from sqlalchemy import inspect

app = create_app()

def seed_data():
    with app.app_context():
        
        # Verificar si la tabla 'organizaciones' existe
        inspector = inspect(db.engine)
        if 'organizaciones' not in inspector.get_table_names():
            print("Las tablas no existen. Ejecuta las migraciones primero.")
            return

        # Verificar si ya existen datos en alguna tabla
        if Organizacion.query.first() is not None:
            print("La base de datos ya tiene datos. No se ejecutará el seed.")
            return
        
        
        # Crear tipos de reunión
        tipo_asamblea = TipoReunion(
            nombre='Asamblea',
            descripcion='Reunión general de la organización',
            creado_por=1  # ID del usuario que crea el registro
        )
        tipo_minga = TipoReunion(
            nombre='Minga',
            descripcion='Reunión para trabajo comunitario',
            creado_por=1  # ID del usuario que crea el registro
        )
        db.session.add(tipo_asamblea)
        db.session.add(tipo_minga)
        db.session.commit()

        # Crear una organización
        organizacion = Organizacion(
            nombre='Organización Ejemplo',
            direccion='Calle 123, Ciudad',
            representante='Juan Pérez',
            telefono='123456789',
            email='info@organizacion.com',
            observaciones='Organización de prueba',
            creado_por=1  # ID del usuario que crea el registro
        )
        db.session.add(organizacion)
        db.session.commit()

        # Crear clientes
        cliente1 = Cliente(
            organizacion_id=organizacion.id,
            nombre='Cliente 1',
            identificacion='1234567890',
            correo='cliente1@example.com',
            telefono='0987654321',
            rol='Administrador',
            usuario='cliente1',  # Nuevo campo
            password='password1',  # Nuevo campo (debe estar encriptado en producción)
            creado_por=1  # ID del usuario que crea el registro
        )
        cliente2 = Cliente(
            organizacion_id=organizacion.id,
            nombre='Cliente 2',
            identificacion='0987654321',
            correo='cliente2@example.com',
            telefono='1234567890',
            rol='Asistente',
            usuario='cliente2',  # Nuevo campo
            password='password2',  # Nuevo campo (debe estar encriptado en producción)
            creado_por=1  # ID del usuario que crea el registro
        )
        db.session.add(cliente1)
        db.session.add(cliente2)
        db.session.commit()

        # Crear reuniones
        reunion1 = Reunion(
            organizacion_id=organizacion.id,
            fecha='2023-10-01',
            hora='14:00',
            lugar='Oficina Principal',
            tipo_reunion_id=tipo_asamblea.id,
            descripcion='Reunión de planificación',
            creado_por=1  # ID del usuario que crea el registro
        )
        reunion2 = Reunion(
            organizacion_id=organizacion.id,
            fecha='2023-10-05',
            hora='10:00',
            lugar='Parque Central',
            tipo_reunion_id=tipo_minga.id,
            descripcion='Minga de limpieza',
            creado_por=1  # ID del usuario que crea el registro
        )
        db.session.add(reunion1)
        db.session.add(reunion2)
        db.session.commit()

        # Crear asistencias
        asistencia1 = Asistencia(
            reunion_id=reunion1.id,
            cliente_id=cliente1.id,
            asistio=True,
            observaciones='Asistió puntual',
            creado_por=1  # ID del usuario que crea el registro
        )
        asistencia2 = Asistencia(
            reunion_id=reunion2.id,
            cliente_id=cliente2.id,
            asistio=False,
            observaciones='No asistió',
            creado_por=1  # ID del usuario que crea el registro
        )
        db.session.add(asistencia1)
        db.session.add(asistencia2)
        db.session.commit()

        print("Datos dummy creados exitosamente.")

if __name__ == '__main__':
    seed_data()