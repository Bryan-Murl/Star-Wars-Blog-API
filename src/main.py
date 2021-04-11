"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/user/<int:id>', methods=['GET'])
def get_people(id):

    return jsonify({"msg": id}), 200

@app.route('/all_characters', methods=['GET'])
def get_all_characters():

    # get all the people
   character_query  = Character.query.all()

    # map the results and your list of people  inside of the all_people variable
    all_characters = list(map(lambda x: x.serialize(), character_query))

    return jsonify(all_characters), 200
    
@app.route('/characters/<int:id>', methods=['GET'])
def get_character_id(id):

    # get only the ones id
    character_query = Character.query.filter_by(id=id)

    # map the results and your list of people  inside of the all_people variable
    all_characters = list(map(lambda x: x.serialize(), character_query))

    return jsonify(all_characters), 200

@app.route('/all_planets', methods=['GET'])
def get_all_planets():

    # get all the people
    planet_query = Planet.query.all()

    # map the results and your list of people  inside of the all_people variable
    all_planets = list(map(lambda x: x.serialize(), planet_query))

    return jsonify(all_planets), 200

@app.route('/planets/<int:id>', methods=['GET'])
def get_planet_id(id):

    # get only the ones id
    planet_query = Planet.query.filter_by(id=id)

    # map the results and your list of people  inside of the all_people variable
    all_planets = list(map(lambda x: x.serialize(), planet_query))

    return jsonify(all_planets), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)