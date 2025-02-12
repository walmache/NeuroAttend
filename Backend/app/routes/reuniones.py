from flask import Blueprint, jsonify, request
from app import db
from app.models import Reunion

reuniones_bp = Blueprint('reuniones', __name__)

# Obtener todas las reuniones
@reuniones_bp.route('/', methods=['GET'])
def obtener_reuniones():
    reuniones = Reunion.query.all()
    return jsonify([reunion.to_dict() for reunion in reuniones])

# Obtener una reunión por ID
@reuniones_bp.route('/<int:id>', methods=['GET'])
def obtener_reunion(id):
    reunion = Reunion.query.get_or_404(id)
    return jsonify(reunion.to_dict())

# Crear una nueva reunión
@reuniones_bp.route('/', methods=['POST'])
def crear_reunion():
    data = request.get_json()
    nueva_reunion = Reunion(
        organizacion_id=data['organizacion_id'],
        fecha=data['fecha'],
        hora=data['hora'],
        lugar=data['lugar'],
        tipo_reunion_id=data['tipo_reunion_id'],
        organizador=data['organizador'],
        descripcion=data.get('descripcion')
    )
    db.session.add(nueva_reunion)
    db.session.commit()
    return jsonify(nueva_reunion.to_dict()), 201

# Actualizar una reunión existente
@reuniones_bp.route('/<int:id>', methods=['PUT'])
def actualizar_reunion(id):
    reunion = Reunion.query.get_or_404(id)
    data = request.get_json()
    reunion.fecha = data.get('fecha', reunion.fecha)
    reunion.hora = data.get('hora', reunion.hora)
    reunion.lugar = data.get('lugar', reunion.lugar)
    reunion.tipo_reunion_id = data.get('tipo_reunion_id', reunion.tipo_reunion_id)
    reunion.organizador = data.get('organizador', reunion.organizador)
    reunion.descripcion = data.get('descripcion', reunion.descripcion)
    db.session.commit()
    return jsonify(reunion.to_dict())

# Eliminar una reunión
@reuniones_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_reunion(id):
    reunion = Reunion.query.get_or_404(id)
    db.session.delete(reunion)
    db.session.commit()
    return '', 204