from flask import Blueprint, jsonify, request
from app import db
from app.models import Cliente
from werkzeug.security import check_password_hash,generate_password_hash
import jwt
import datetime
from flask import current_app as app

clientes_bp = Blueprint('clientes', __name__)

# Obtener todos los clientes
@clientes_bp.route('/', methods=['GET'])
def obtener_clientes():
    clientes = Cliente.query.all()
    return jsonify([cliente.to_dict() for cliente in clientes])

# Obtener un cliente por ID
@clientes_bp.route('/<int:id>', methods=['GET'])
def obtener_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    return jsonify(cliente.to_dict())

# Crear un nuevo cliente
@clientes_bp.route('/', methods=['POST'])
def crear_cliente():
    data = request.get_json()

    # Verificar si la contraseña está presente
    if 'password' not in data or not data['password']:
        return jsonify({'message': 'La contraseña es obligatoria'}), 400
    # Hashear la contraseña antes de guardarla
    hashed_password = generate_password_hash(data['password'])

    nuevo_cliente = Cliente(
        organizacion_id=data['organizacion_id'],
        nombre=data['nombre'],
        identificacion=data['identificacion'],
        correo=data.get('correo'),
        telefono=data.get('telefono'),
        rol=data['rol'],
        foto=data.get('foto'),
        creado_por=data['creado_por'],
        usuario=data['usuario'],
        password=hashed_password  # Guardar la contraseña hasheada
    )

    db.session.add(nuevo_cliente)
    db.session.commit()
    
    return jsonify(nuevo_cliente.to_dict()), 201


# Actualizar un cliente existente
@clientes_bp.route('/<int:id>', methods=['PUT'])
def actualizar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    data = request.get_json()
    cliente.nombre = data.get('nombre', cliente.nombre)
    cliente.identificacion = data.get('identificacion', cliente.identificacion)
    cliente.correo = data.get('correo', cliente.correo)
    cliente.telefono = data.get('telefono', cliente.telefono)
    cliente.rol = data.get('rol', cliente.rol)
    cliente.foto = data.get('foto', cliente.foto)
    db.session.commit()
    return jsonify(cliente.to_dict())

# Eliminar un cliente
@clientes_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return '', 204

# Autenticar cliente
@clientes_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    password = data.get('password')

    if not usuario or not password:
        return jsonify({'message': 'Usuario y contraseña son obligatorios'}), 400

    cliente = Cliente.query.filter_by(usuario=usuario).first()

    if not cliente or not check_password_hash(cliente.password, password):
        return jsonify({'message': 'Credenciales incorrectas'}), 401
    
    rol = cliente.rol if cliente.rol else 'desconocido'

    # Generar token JWT
    token = jwt.encode({
        'user_id': cliente.id,
        'rol': cliente.rol,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=12)
    }, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'token': token, 'rol': rol, 'message': 'Inicio de sesión exitoso'})