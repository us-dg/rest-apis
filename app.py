from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import json
import data_loader

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

try:
    data_loader.load_data(db.engine)
except:
    pass


class Customers(db.Model):
    CustomerID = db.Column(db.String(5), primary_key=True)
    CompanyName = db.Column(db.String(40))
    ContactName = db.Column(db.String(30))
    ContactTitle = db.Column(db.String(30))
    Address = db.Column(db.String(60))
    City = db.Column(db.String(15))
    Region = db.Column(db.String(15))
    PostalCode = db.Column(db.String(10))
    Country = db.Column(db.String(15))
    Phone = db.Column(db.String(24))
    Fax = db.Column(db.String(24))

    def __init__(self, CustomerID, CompanyName, ContactName, ContactTitle,
                 Address, City, Region, PostalCode, Country, Phone, Fax):
        self.CustomerID = CustomerID
        self.CompanyName = CompanyName
        self.ContactName = ContactName
        self.ContactTitle = ContactTitle
        self.Address = Address
        self.City = City
        self.Region = Region
        self.PostalCode = PostalCode
        self.Country = Country
        self.Phone = Phone
        self.Fax = Fax


# Customer Schema
class CustomerSchema(ma.Schema):
    class Meta:
        fields = ('CustomerID', 'CompanyName', 'ContactName', 'ContactTitle', 'Address', 'City', 'Region', 'PostalCode',
                  'Country', 'Phone', 'Fax')


# Init Schema
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)


# Get All Customers
@app.route('/customer', methods=['GET'])
def get_customers():
    all_customers = db.engine.execute('SELECT * FROM customers')
    result = customers_schema.dump(all_customers)
    return json.dumps(result)

# Get a Customer
@app.route('/customer/<cid>', methods=['GET'])
def get_customer(cid):
    customer = Customers.query.get(cid)
    result = customer_schema.dump(customer)
    return jsonify(result)


# Add a Customer
@app.route('/customer', methods=['POST'])
def add_customer():
    CustomerID = request.json['CustomerID']
    CompanyName = request.json['CompanyName']
    ContactName = request.json['ContactName']
    ContactTitle = request.json['ContactTitle']
    Address = request.json['Address']
    City = request.json['City']
    Region = request.json['Region']
    PostalCode = request.json['PostalCode']
    Country = request.json['Country']
    Phone = request.json['Phone']
    Fax = request.json['Fax']

    new_customer = Customers(CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode,
                             Country, Phone, Fax)
    db.session.add(new_customer)
    db.session.commit()

    return customer_schema.jsonify(new_customer)

# Update a Customer
@app.route('/customer/<cid>', methods=['PUT'])
def update_customer(cid):
    customer = Customers.query.get(cid)

    CustomerID = request.json['CustomerID']
    CompanyName = request.json['CompanyName']
    ContactName = request.json['ContactName']
    ContactTitle = request.json['ContactTitle']
    Address = request.json['Address']
    City = request.json['City']
    Region = request.json['Region']
    PostalCode = request.json['PostalCode']
    Country = request.json['Country']
    Phone = request.json['Phone']
    Fax = request.json['Fax']

    customer.CustomerID = CustomerID
    customer.CompanyName = CompanyName
    customer.ContactName = ContactName
    customer.ContactTitle = ContactTitle
    customer.Address = Address
    customer.City = City
    customer.Region = Region
    customer.PostalCode = PostalCode
    customer.Country = Country
    customer.Phone = Phone
    customer.Fax = Fax

    db.session.commit()

    return customer_schema.jsonify(customer)


# Delete a Customer
@app.route('/customer/<cid>', methods=['DELETE'])
def delete_customer(cid):
    customer = Customers.query.get(cid)
    db.session.delete(customer)
    db.session.commit()
    return customer_schema.jsonify(customer)


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
