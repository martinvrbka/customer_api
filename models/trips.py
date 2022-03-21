from database import db

class TripModel(db.Model):
    __tablename__ = 'trips'

    trip_id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100))
    price = db.Column(db.Float(precision=2))
    customer_username = db.Column(db.ForeignKey('customers.username'))
    customer = db.relationship('CustomerModel')

    def find_by_id(trip_id):
        return TripModel.query.filter_by(trip_id=trip_id).first()

    def json(self):
        return {
            'trip_id': self.trip_id,
            'destination': self.destination,
            'price': self.price,
            'customer_username': self.customer_username
        }

    def create_trip(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_database(self):
        db.session.delete(self)
        db.session.commit()