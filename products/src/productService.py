from db import db
from product import Product

class ProductService:

    def create_product(self, product_data):
        new_product = Product(
            name=product_data.get('name'),
            desc=product_data.get('desc'),
            price=product_data.get('price'),
            quantity=product_data.get('quantity')
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product
    
    def get_all_products(self):
        return Product.query.all()
    
    def get_product_by_id(self, product_id):
        return Product.query.get(product_id)
    
    def update_product(self, product_id, data):
        product = Product.query.get(product_id)
        if product:
            for key, value in data.items():
                setattr(product, key, value)
            db.session.commit()
        return product
        
    def delete_product(self, product_id):
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
        return product