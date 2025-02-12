from flask import Blueprint, jsonify, request
from app import db
from app.models import Asistencia

asistencia_bp = Blueprint('asistencia', __name__)

# Obtener todas las asistencias
@asistencia_bp.route('/', methods=['GET'])
def obtener_asistencias():
    asistencias = Asistencia.query.all()
    return jsonify([asistencia.to_dict() for asistencia in asistencias])

# Obtener una asistencia por ID
@asistencia_bp.route('/<int:id>', methods=['GET'])
def obtener_asistencia(id):
    asistencia = Asistencia.query.get_or_404(id)
    return jsonify(asistencia.to_dict())

# Crear una nueva asistencia
@asistencia_bp.route('/', methods=['POST'])
def crear_asistencia():
    data = request.get_json()
    nueva_asistencia = Asistencia(
        reunion_id=data['reunion_id'],
        cliente_id=data['cliente_id'],
        asistio=data['asistio'],
        observaciones=data.get('observaciones'),
        registrado_por=data['registrado_por']
    )
    db.session.add(nueva_asistencia)
    db.session.commit()
    return jsonify(nueva_asistencia.to_dict()), 201

# Actualizar una asistencia existente
@asistencia_bp.route('/<int:id>', methods=['PUT'])
def actualizar_asistencia(id):
    asistencia = Asistencia.query.get_or_404(id)
    data = request.get_json()
    asistencia.asistio = data.get('asistio', asistencia.asistio)
    asistencia.observaciones = data.get('observaciones', asistencia.observaciones)
    asistencia.registrado_por = data.get('registrado_por', asistencia.registrado_por)
    db.session.commit()
    return jsonify(asistencia.to_dict())

# Eliminar una asistencia
@asistencia_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_asistencia(id):
    asistencia = Asistencia.query.get_or_404(id)
    db.session.delete(asistencia)
    db.session.commit()
    return '', 204