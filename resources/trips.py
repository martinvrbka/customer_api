from flask_restful import Resource, reqparse
from auth import api_key_required
from models.trips import TripModel

class Trips(Resource):
    @api_key_required
    def get(self):
        return list(map(lambda x: x.json(), TripModel.query.all()))

class Trip(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('destination', type=str, required=True)
    parser.add_argument('price', type=float, required=True)
    parser.add_argument('customer_username', type=str, required=True)

    @api_key_required
    def get(self, trip_id):
        trip = TripModel.find_by_id(trip_id)
        if trip:
            return trip.json(), 200
        return {'message': 'trip not found'}, 404

    @api_key_required
    def post(self, trip_id):
        if TripModel.find_by_id(trip_id):
            return {'error': 'trip already exist'}, 409
        data = self.parser.parse_args()
        new_trip = TripModel(trip_id, **data)
        new_trip.create_trip()
        return new_trip.json(), 201

    @api_key_required
    def put(self, trip_id):
        data = self.parser.parse_args()
        updated_trip = TripModel.find_by_id(trip_id)
        if updated_trip:
            updated_trip.destination = data['destination']
            updated_trip.price = data['price']
            updated_trip.customer_username = data['customer_username']
        else:
            updated_trip = TripModel(**data)
        updated_trip.create_trip()
        return updated_trip.json(), 201

    @api_key_required
    def delete(self, trip_id):
        trip = TripModel.find_by_id(trip_id)
        if trip:
            trip.delete_from_database()
            return {'message': 'trip was successfully removed'}, 200
        return {'message': 'trip not found'}, 404

