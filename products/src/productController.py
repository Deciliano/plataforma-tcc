from flask import Blueprint, request, jsonify
from productService import ProductService

product_bp = Blueprint('product_bp', __name__)
product_service = ProductService()

@product_bp.route('/product/create', methods=['POST'])
def create_product_route():
    product_data = request.json
    product_service.create_product(product_data)
    return jsonify({
        'message': 'Product created successfully'
    }), 201

@product_bp.route('/product/<int:product_id>', methods=['GET'])
def get_product_route(product_id):
    product = product_service.get_product_by_id(product_id)
    if product:
        return jsonify(product.to_dict())
    return jsonify({
        'message': 'Product not found'
    }), 404

@product_bp.route('/products', methods=['GET'])
def get_all_products_route():
    products = product_service.get_all_products()
    return jsonify([product.to_dict() for product in products])

@product_bp.route('/product/update/<int:product_id>', methods=['PUT'])
def update_product_route(product_id):
    data = request.get_json()
    product = product_service.update_product(product_id, data)
    if product:
        return jsonify(product.to_dict())
    return jsonify({
        'message': 'Product not found'
    }), 404

@product_bp.route('/product/<int:product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    product = product_service.delete_product(product_id)
    if product:
        return jsonify({'message': 'Product deleted'})
    return jsonify({'message':'Product not found'}), 404