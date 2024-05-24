from flask import Blueprint, request, jsonify
from services.clientService import ClientService

client_bp = Blueprint('client_bp', __name__)
client_service = ClientService()

@client_bp.route('/clients', methods=['GET'])
def get_clients_route():
    clients = client_service.get_all_clients()
    return jsonify([client.to_dict() for client in clients])

@client_bp.route('/clients/<int:client_id>', methods=['GET'])
def get_client_route(client_id):
    client = ClientService.get_client_by_id(client_id)
    if client:
        return jsonify(client.to_dict())
    return jsonify({'message': 'Client not found'}), 404

@client_bp.route('/client/create', methods=['POST'])
def create_client_route():
    client_data = request.json
    client_service.create_client(client_data)
    return jsonify({
        "message": "Client created successfully"
    }), 201

@client_bp.route('/clients/<int:client_id>', methods=['PUT'])
def update_client_route(client_id):
    data = request.get_json()
    client = ClientService.update_client(client_id, data)
    if client:
        return jsonify(client.to_dict())
    return jsonify({'message': 'Client not found'}), 404

@client_bp.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client_route(client_id):
    client = ClientService.delete_client(client_id)
    if client:
        return jsonify({'message': 'Client deleted'})
    return jsonify({'message': 'Client not found'}), 404