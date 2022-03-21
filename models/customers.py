from database import db


class CustomerModel(db.Model):
    __tablename__ = "customers"
    username = db.Column(db.String(100), primary_key=True)
    email = db.Column(db.String(100))
    name = db.Column(db.String(100))
    newsletter_status = db.Column(db.Boolean, default=False)

    trips = db.relationship('TripModel')

    def __init__(self, trip_id, destination, price, customer_username):
        self.trip_id = trip_id
        self.destination = destination
        self.price = price
        self.customer_username = customer_username

    def find_by_username(self, username):
        return CustomerModel.query.filter_by(username=username).first()

    def json(self):
        return {
            'username': self.username,
            'email': self.email,
            'name': self.name,
            'newsletter_status': self.newsletter_status,
            'trips': [trip.json() for trip in self.trips]
        }

    def create_customer(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_database(self):
        db.session.delete(self)
        db.session.commit()

