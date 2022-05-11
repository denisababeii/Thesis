from merger import Merger
from content_based import ContentBasedFilteringRecommender
from courses_cleaner import CoursesCleaner
from collaborative import CollaborativeFilteringRecommender
from flask import Flask, request, session, jsonify
import configparser
import os
from get_electives_links import Elective_Links
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity,unset_jwt_cookies, jwt_required, JWTManager
import json

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "long-and-secret-uncrackable-secret-key"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=4)
jwt = JWTManager(app)

@app.route("/grades", methods=['POST'])
@jwt_required()
def get_grades():
    grades = json.loads(request.json.get("grades", None))
    print(grades)
    data = session.pop('data', None)
    data['grades'] = grades
    session['data'] = data
    # add to database here
    print(session['data'])
    return "OK"

@app.route("/preference", methods=['POST'])
@jwt_required()
def get_preference():
    preference = json.loads(request.json.get("preference", None))
    data = session.pop('data', None)
    data['preference'] = preference
    session['data'] = data
    # add to database here
    print(session['data'])
    return "OK"
    
@app.route("/compulsory", methods=["GET"])
@jwt_required()
def send_courses():
    parser = configparser.ConfigParser()
    parser.read("config.txt")
    courses = parser.get("config", "compulsory_courses").split(",")
    session['data'] = {'grades':[], 'preference':[]}
    return {"courses": courses}

@app.route("/electives1", methods=['GET'])
@jwt_required()
def send_electives1():
    parser = configparser.ConfigParser()
    parser.read("config.txt")
    courses = parser.get("config", "elective_1").split(",")
    return {"courses": courses}

@app.route("/electives2", methods=["GET"])
@jwt_required()
def send_electives2():
    parser = configparser.ConfigParser()
    parser.read("config.txt")
    courses = parser.get("config", "elective_2").split(",")
    return {"courses": courses}

@app.route("/electives3", methods=["GET"])
@jwt_required()
def send_electives3():
    parser = configparser.ConfigParser()
    parser.read("config.txt")
    courses = parser.get("config", "elective_3").split(",")
    return {"courses": courses}

@app.route("/electives_links", methods=["GET"])
@jwt_required()
def send_electives_links():
    courses = Elective_Links.get()
    return {"courses": courses}

@app.route("/result", methods=["GET"])
@jwt_required()
def result():
    data = session.pop('data')
    grades = data['grades']
    preference = data['preference']
    # get from database 
    preference.append(10)
    
    courses = CoursesCleaner().get_courses()

    cbf_recommender = ContentBasedFilteringRecommender(courses)
    cbf_ranking = cbf_recommender.get_ranking(grades)

    cf_recommender = CollaborativeFilteringRecommender()
    cf_ranking = cf_recommender.get_ranking(grades)

    merger = Merger(50, 20, 30)
    result = merger.merge(cbf_ranking, cf_ranking, preference)[0:3]
    print(result)
    # add to database
    return {"result": result}

@app.route("/last_result", methods=["GET"])
@jwt_required()
def last_result():
    #return {"result": ['Computer science investigations -an iot perspective, Advanced compiler design, History of computer science', 'Network and system administration, Advanced compiler design, History of computer science', 'Computer science investigations -an iot perspective, Design patterns, History of computer science']}
    return {"result":[]}
    
@app.route('/login', methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return {"msg": "Wrong username or password"}, 401

    access_token = create_access_token(identity=username)
    response = {"access_token":access_token}
    return response

@app.route('/signup', methods=["POST"])
def signup():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    # add to database here

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
