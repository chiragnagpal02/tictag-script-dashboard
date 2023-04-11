from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://tictag@localhost:8889/Tictag'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

class Employees(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    position = db.Column(db.String(80), nullable=False)
    department = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, name, email, position, department):
        self.name = name
        self.email = email
        self.position = position
        self.department = department

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'position': self.position,
            'department': self.department,
            'created_at': self.created_at
        }

@app.route("/employees/get_all_employees", methods=['GET'])
def get_all_employees():
    all_employees = Employees.query.all()
    print(all_employees)
    output = []
    if all_employees:
        for employee in all_employees:
            output.append(employee.json())
        return jsonify(
            {
                "message": "All employees",
                "data": output
            }
        ), 200
    else:
        return jsonify(
            {
                "message": "No employees found"
            }
        ), 404
    
@app.route("/employees/create_employee", methods=['POST'])
def create_employee():
    name = request.json['name']
    email = request.json['email']
    position = request.json['position']
    department = request.json['department']
    print(name, email, position, department)
    existing_employee = Employees.query.filter_by(email=email).first()
    if existing_employee:
        return jsonify(
            {
                "code" : 409,
                "message" : "Employee with email already exists"
            }
        ), 409


    try:
        new_employee = Employees(
            name,
            email,
            position,
            department
      )

        db.session.add(new_employee)
        db.session.commit()

        return jsonify(
            {
                "code" : 200,
                "message" : "Employee created successfully",
                "data" : new_employee.json()
            }
        ), 200
        
    except:
        return jsonify(
            {
                "code" : 400,
                "message" : "Employee already exists"
            }
        ), 400

@app.route('/employees/get_employee_details/<email>')
def get_employee_details(email):
    employee = Employees.query.filter_by(email=email).first()
    if employee:
        return jsonify(
            {
                "code" : 200,
                "message" : "Employee fetched successfully",
                "data" : employee.json()
            }
        ), 200
    else:
        return jsonify(
            {
                "code" : 404,
                "message" : "Employee not found"
            }
        ), 404


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)

