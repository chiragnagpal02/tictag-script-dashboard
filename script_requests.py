from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests

app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://tictag@localhost:8889/Tictag'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

MESSAGING_URL = "http://127.0.0.1:5005/send_message"


class Script_Requests(db.Model):
    __tablename__ = 'script_requests'

    id=db.Column(db.Integer, primary_key=True, autoincrement=True) 
    employee_id=db.Column(db.Integer, nullable=False)
    project=db.Column(db.String(120), nullable=False)
    request_description=db.Column(db.String(600), nullable=False)
    impact=db.Column(db.String(80), nullable=False)
    urgency=db.Column(db.String(80), nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.now())
    

    def __init__(self, employee_id, project, request_description, impact, urgency):
        self.employee_id = employee_id
        self.project = project
        self.request_description = request_description
        self.impact = impact
        self.urgency = urgency

    def json(self):
        return {
            'id': self.id,
            'employee_id': self.employee_id,
            'project': self.project,
            'request_description': self.request_description,
            'impact': self.impact,
            'urgency': self.urgency,
            'created_at': self.created_at
        }
    
# route1 - Create the request for a script 

@app.route('/script_requests/create_script_request', methods=['POST'])
def create_script_request():
    employee_id = request.json['employee_id']
    project = request.json['project']
    request_description = request.json['request_description']
    impact = request.json['impact']
    urgency = request.json['urgency']
    print(employee_id, project, request_description, impact, urgency)

    try:
        new_script_request = Script_Requests(
            employee_id,  
            project, 
            request_description, 
            impact, 
            urgency
        )

        db.session.add(new_script_request)
        db.session.commit()

        message = f"A New Script has been created by Employee with ID {employee_id}. The Details are as follows - \nUrgency: {urgency} \nImpact: {impact} \nProject: {project} \nRequest Description: {request_description}"
        print(message)

        data = {
            "to": "+6583606092",
            "body": message
        }

        message_sid = requests.post(MESSAGING_URL, json=data)

        print(message_sid)

        return jsonify(
            {
                "code" : 200,
                "message" : "Script request created successfully",
                "data" : new_script_request.json(),
                "message_sid" : message_sid.json()
            }
        ), 200
    except:
        return jsonify(
            {
                "code" : 404,
                "message" : "Script request not created"
            }
        ), 404


@app.route("/script_requests/get_all_requests", methods=['GET'])
def get_all_requests():
    script_requests = Script_Requests.query.all()
    print(script_requests)
    
    return jsonify(
        {
            "code" : 200,
            "message" : "Script requests fetched successfully",
            "data" : [script_request.json() for script_request in script_requests]
        }
    ), 200

@app.route("/script_requests/get_script_requests_by_email")
def get_script_requests_by_email():
    email = request.args.get('email')
    script_requests = Script_Requests.query.filter_by(employee_email=email).all()
    if script_requests:
        return jsonify(
            {
                "code" : 200,
                "email" : email,
                "message" : "Script requests fetched successfully",
                "data" : [script_request.json() for script_request in script_requests]
            }
        ), 200
    else:
        return jsonify(
            {
                "code" : 404,
                "message" : "No Requests in the Database"
            }
        ), 404
    

@app.route("/script_requests/get_script_requests_by_project")
def get_script_requests_by_project():
    project = request.args.get('project')
    script_requests = Script_Requests.query.filter_by(project=project).all()
    if script_requests:
        return jsonify(
            {
                "code" : 200,
                "project" : project,
                "message" : "Script requests fetched successfully",
                "data" : [script_request.json() for script_request in script_requests]
            }
        ), 200
    else:
        return jsonify(
            {
                "code" : 404,
                "message" : "No Requests in the Database"
            }
        ), 404


@app.route("/script_requests/get_script_requests_by_impact/<impact>")
def get_script_requests_by_impact(impact):
    script_requests = Script_Requests.query.filter_by(impact=impact).all()
    if script_requests:
        return jsonify(
            {
                "code" : 200,
                "impact" : impact,
                "message" : "Script requests fetched successfully",
                "data" : [script_request.json() for script_request in script_requests]
            }
        ), 200
    else:
        return jsonify(
            {
                "code" : 404,
                "message" : "No Requests in the Database"
            }
        ), 404
    

@app.route("/script_requests/get_script_requests_by_urgency/<urgency>")
def get_script_requests_by_urgency(urgency):
    script_requests = Script_Requests.query.filter_by(urgency=urgency).all()
    if script_requests:
        return jsonify(
            {
                "code" : 200,
                "urgency" : urgency,
                "message" : "Script requests fetched successfully",
                "data" : [script_request.json() for script_request in script_requests]
            }
        ), 200
    else:
        return jsonify(
            {
                "code" : 404,
                "message" : "No Requests in the Database"
            }
        ), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



    
