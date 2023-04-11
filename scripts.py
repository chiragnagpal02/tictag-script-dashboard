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

class Scripts(db.Model):
    __tablename__ = 'scripts'

    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    script_name=db.Column(db.String(80), nullable=False)
    script_description=db.Column(db.String(600), nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.now())
    project = db.Column(db.String(120), nullable=False)
    created_by=db.Column(db.String(80), nullable=False)
    request_id = db.Column(db.Integer, nullable=True)
    script_link = db.Column(db.String(400), nullable=False)
    comments = db.Column(db.String(1000), nullable=True)

    def __init__(self, script_name, script_description, project, created_by, request_id, script_link, comments):
        self.script_name = script_name
        self.script_description = script_description
        self.project = project
        self.created_by = created_by
        self.request_id = request_id
        self.script_link = script_link
        self.comments = comments

    def json(self):
        return {
            'id': self.id,
            'script_name': self.script_name,
            'script_description': self.script_description,
            'project': self.project,
            'created_by': self.created_by,
            'request_id': self.request_id,
            'script_link': self.script_link,
            'comments': self.comments
        }
    
app.route('/scripts/create_script', methods=['POST'])
def create_script():
    script_name = request.json['script_name']
    script_description = request.json['script_description']
    project = request.json['project']
    created_by = request.json['created_by']
    request_id = request.json['request_id']
    script_link = request.json['script_link']
    comments = request.json['comments']
    
    try:
            new_script = Scripts(
            script_name,
            script_description,
            project,
            created_by,
            request_id,
            script_link,
            comments
        )
            db.session.add(new_script)
            db.session.commit()

            return jsonify(
                {
                    'code': 200,
                    'message': 'Script created successfully',
                    'data': new_script.json()

                }
            ),200
    
    except: 
        return jsonify(
                {
                    'code': 500,
                    'message': 'Error creating script'
                }
            ),500
    
@app.route("/scripts/get_all_scripts", methods=['GET'])
def get_all_scripts():
    scripts = Scripts.query.all()
    if scripts:
        return jsonify(
                {
                    'code': 200,
                    'message': 'Scripts fetched successfully',
                    'data': [script.json() for script in scripts]
                }
            ), 200
    else:
        return jsonify(
                {
                    'code': 404,
                    'message': 'No Scripts found'
                }
            ), 404
    

app.route("/scripts/get_scripts_by_project")
def get_scripts_by_project():
    project = request.args.get('project')
    scripts = Scripts.query.filter_by(project=project).all()
    if scripts:
        return jsonify(
                {
                    'code': 200,
                    'message': 'Scripts fetched successfully',
                    'project' : project,
                    'data': [script.json() for script in scripts]
                }
            ), 200
    else:
        return jsonify(
                {
                    'code': 404,
                    'message': 'No Scripts found in the Database'
                }
            ), 404
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)
    


