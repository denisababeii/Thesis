from merger import Merger
from content_based import ContentBasedFilteringRecommender
from courses_cleaner import CoursesCleaner
from collaborative import CollaborativeFilteringRecommender
from flask import Flask, request, session

app = Flask(__name__)

@app.route("/grades")
def get_grades():
    session['grades'] = request.json['grades']

@app.route("/preference")
def get_preference():
    session['preference'] = request.json['preference']

@app.route("/result")
def result():
    grades = session.pop('grades')
    preference = session.pop('preference')

    courses = CoursesCleaner().get_courses()

    cbf_recommender = ContentBasedFilteringRecommender(courses)
    cbf_ranking = cbf_recommender.get_ranking(grades)

    cf_recommender = CollaborativeFilteringRecommender()
    cf_ranking = cf_recommender.get_ranking(grades)

    merger = Merger(50, 20, 30)
    result = merger.merge(cbf_ranking, cf_ranking, preference)
    return {"result": result}

if __name__ == "__main__":
    app.run(debug=True)
