"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
""" import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def handle_hello():
    # This is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {"hello": "world",
                     "family": members}
    return jsonify(response_body), 200

@app.route('/members/<int:member_id>', methods=['GET'])
def fetch_member(member_id):
    response = jackson_family.get_member(member_id)
    return jsonify(response),200

@app.route('/members', methods=['PÖST'])
def add_member():
    request_body = request.json
    jackson_family._members.append(request_body)
    return jsonify(jackson_family._members),200

@app.route('/members/<int:member_id>', methods=['DELETE'])
def remove_member(member_id):
    jackson_family.delete_member(member_id)
    return jsonify({"done":True}),200

# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
 """

"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Initialize with the 3 members specified in the instructions
jackson_family.add_member({
    "first_name": "Jane",
    "age": 35,
    "lucky_numbers": [10, 14, 3]
})

jackson_family.add_member({
    "first_name": "Jimmy",
    "age": 5,
    "lucky_numbers": [1]
})

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/members/<int:member_id>', methods=['GET'])
def fetch_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"msg": "Member not found"}), 404

@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()

    # Validate required fields
    required_fields = ['first_name', 'age', 'lucky_numbers']
    for field in required_fields:
        if field not in data:
            return jsonify({"msg": f"Missing required field: {field}"}), 400

    if not isinstance(data['age'], int) or data['age'] <= 0:
        return jsonify({"msg": "Age must be a positive integer"}), 400

    if not isinstance(data['lucky_numbers'], list) or not all(isinstance(n, int) for n in data['lucky_numbers']):
        return jsonify({"msg": "Lucky numbers must be a list of integers"}), 400

    new_member = {
        "first_name": data["first_name"],
        "last_name": "Jackson",
        "age": data["age"],
        "lucky_numbers": data["lucky_numbers"]
    }

    jackson_family.add_member(new_member)
    return jsonify(new_member), 200

@app.route('/members/<int:member_id>', methods=['DELETE'])
def remove_member(member_id):
    updated_list = jackson_family.delete_member(member_id)
    if updated_list:
        return jsonify({"done": True}), 200
    else:
        return jsonify({"msg": "Member not found"}), 404


# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
