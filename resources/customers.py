from flask_restful import Resource, reqparse
from auth import api_key_required
from models.customers import CustomerModel

class Customers(Resource):
    @api_key_required
    def get(self):
        return list(map(lambda x: x.json(), CustomerModel.query.all()))
class Customer(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('name', type=str, required=True)
    parser.add_argument('newsletter_status', type=bool, required=True)
    @api_key_required
    def get(self, username):
        customer = CustomerModel.find_by_username(self, username)
        if customer:
            return customer.json(), 200
        return {'message': 'username not found'}, 404
    @api_key_required
    def post(self, username):
        if CustomerModel.find_by_username(self, username):
            return {'error': 'username already exist'}, 409
        data = self.parser.parse_args()
        new_customer = CustomerModel(username, **data)
        new_customer.create_customer()
        return new_customer.json(), 201
    @api_key_required
    def put(self, username):
        data = self.parser.parse_args()
        updated_customer = CustomerModel.find_by_username(self, username)
        if updated_customer:
            updated_customer.email = data['email']
            updated_customer.name = data['name']
            updated_customer.newsletter_status = data['newsletter_status']
        else:
            updated_customer = CustomerModel(username, **data)
        updated_customer.create_customer()
        return updated_customer.json(), 201
    @api_key_required
    def delete(self, username):
        customer = CustomerModel.find_by_username(self, username)
        if customer:
            customer.delete_from_database()
            return {'message': 'customer was successfully removed'}, 200
        return {'message': 'username not found'}, 404
