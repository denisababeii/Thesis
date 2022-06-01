from merger import Merger
from content_based import ContentBasedFilteringRecommender
from courses_cleaner import CoursesCleaner
from collaborative import CollaborativeFilteringRecommender
from flask import Flask, request, session, jsonify
import os
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
import json
from db_util import DatabaseUtils

# Create Application object
app = Flask(__name__)
# Configure secret key
app.config["JWT_SECRET_KEY"] = "long-and-secret-uncrackable-secret-key"
jwt = JWTManager(app)
db = DatabaseUtils()

@app.route("/grades", methods=['POST'])
@jwt_required()
def get_grades():
    grades = json.loads(request.json.get("grades", None))
    username = json.loads(request.json.get("username", None))
    db.save_grades(username, grades)
    return "OK"

@app.route("/preference", methods=['POST'])
@jwt_required()
def get_preference():
    preference = json.loads(request.json.get("preference", None))
    username = json.loads(request.json.get("username", None))
    db.save_preference(username, preference)
    return "OK"
    
@app.route("/compulsory", methods=["GET"])
@jwt_required()
def send_courses():
    courses = db.get_compulsory_courses().split(",")
    return {"courses": courses}

@app.route("/electives1", methods=['GET'])
@jwt_required()
def send_electives1():
    courses = db.get_elective_1().split(",")
    return {"courses": courses}

@app.route("/electives2", methods=["GET"])
@jwt_required()
def send_electives2():
    courses = db.get_elective_2().split(",")
    return {"courses": courses}

@app.route("/electives3", methods=["GET"])
@jwt_required()
def send_electives3():
    courses = db.get_elective_3().split(",")
    return {"courses": courses}

@app.route("/electives_links", methods=["GET"])
@jwt_required()
def send_electives_links():
    courses = db.get_elective_links()
    return {"courses": courses}

@app.route("/result/<username>", methods=["GET"])
@jwt_required()
def result(username):
    grades = db.get_grades(username)
    preference = db.get_preference(username)
    
    courses = CoursesCleaner(db).get_courses()

    cbf_recommender = ContentBasedFilteringRecommender(courses)
    cbf_ranking = cbf_recommender.get_ranking(grades)

    generated_grades = db.get_generated_grades()
    noPackages = len(db.get_packages().split(","))
    noCompulsory = len(db.get_compulsory_courses().split(","))
    cf_recommender = CollaborativeFilteringRecommender(generated_grades, noPackages, noCompulsory)
    cf_ranking = cf_recommender.get_ranking(grades)

    merger = Merger(50, 20, 30, 7)
    result = merger.merge(cbf_ranking, cf_ranking, preference)[0:3]
    print(result)
    db.save_result(username, result)
    return {"result": result}

@app.route("/last_result/<username>", methods=["GET"])
@jwt_required()
def last_result(username):
    result = db.get_result(username)
    return {"result":result}
    
@app.route('/login', methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if db.do_login(username, password) == "FAIL":
        response = {"access_token": None}, 401
    else:
        # Generate access token if the credentials are valid
        access_token = create_access_token(identity=username)
        response = {"access_token":access_token}
    return response

@app.route('/signup', methods=["POST"])
def signup():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if db.do_signup(username, password) == "FAIL":
        response = {"access_token": None}, 401
    else:
        access_token = create_access_token(identity=username)
        response = {"access_token":access_token}
    return response

@app.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True)
