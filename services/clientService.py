from models.client import Client
from storage.db import db

class ClientService:

    def get_all_clients(self):
        return Client.query.all()
    
    def get_client_by_id(clent_id):
        return Client.query.get(clent_id)
    
    def create_client(self, client_data):
        new_client = Client(name=client_data.get('name'), 
                            email=client_data.get('email'), 
                            phone=client_data.get('phone'))
        db.session.add(new_client)
        db.session.commit()
    
    def update_client(client_id, data):
        client = Client.query.get(client_id)
        if client:
            for key, value in data.items():
                setattr(client, key, value)
            db.session.commit()
            return client
        
    def delete_client(client_id):
        client = Client.query.get(client_id)
        if client:
            db.session.delete(client)
            db.session.commit()
        return client