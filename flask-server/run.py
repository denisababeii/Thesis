from merger import Merger
from content_based import ContentBasedFilteringRecommender
from courses_cleaner import CoursesCleaner
from collaborative import CollaborativeFilteringRecommender
from flask import Flask, request, session
import configparser
import os
from get_electives_links import Elective_Links

app = Flask(__name__)

@app.route("/grades")
def get_grades():
    session['grades'] = request.json['grades']

@app.route("/preference")
def get_preference():
    session['preference'] = request.json['preference']

@app.route("/compulsory")
def send_courses():
    parser = configparser.ConfigParser()
    parser.read("config.txt")
    courses = parser.get("config", "compulsory_courses").split(",")
    return {"courses": courses}

@app.route("/electives1")
def send_electives1():
    parser = configparser.ConfigParser()
    parser.read("config.txt")
    courses = parser.get("config", "elective_1").split(",")
    return {"courses": courses}

@app.route("/electives2")
def send_electives2():
    parser = configparser.ConfigParser()
    parser.read("config.txt")
    courses = parser.get("config", "elective_2").split(",")
    return {"courses": courses}

@app.route("/electives3")
def send_electives3():
    parser = configparser.ConfigParser()
    parser.read("config.txt")
    courses = parser.get("config", "elective_3").split(",")
    return {"courses": courses}

@app.route("/electives_links")
def send_electives_links():
    courses = Elective_Links.get()
    return {"courses": courses}

@app.route("/result")
def result():
    #grades = session.pop('grades')
    #preference = session.pop('preference')
    grades=[6, 7, 8, 9, 10, 8, 7, 8, 9, 10]
    preference=["Computer science investigations -an iot perspective", "Advanced compiler design", "Academic ethics and integrity (in computer science)", 10]

    courses = CoursesCleaner().get_courses()

    cbf_recommender = ContentBasedFilteringRecommender(courses)
    cbf_ranking = cbf_recommender.get_ranking(grades)

    cf_recommender = CollaborativeFilteringRecommender()
    cf_ranking = cf_recommender.get_ranking(grades)

    merger = Merger(50, 20, 30)
    result = merger.merge(cbf_ranking, cf_ranking, preference)[0:3]
    return {"result": result}

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True)
