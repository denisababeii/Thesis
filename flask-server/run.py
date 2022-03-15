from merger import Merger
from contentBased import ContentBasedFilteringRecommender
from coursesCleaner import CoursesCleaner
from collaborativeFiltering import CollaborativeFilteringRecommender
from flask import Flask

app = Flask(__name__)

user = [54.0, 55.0, 19.0, 14.0, 47.0, 48.0, 15.0, 55.0, 45.0, 43.0]  # The list of grades for the current user
user_preference = ['AR_VR', 'CS', 'ML', 50]

@app.route("/result")
def result():
    courses = CoursesCleaner().get_courses()

    cbf_recommender = ContentBasedFilteringRecommender(courses)
    cbf_ranking = cbf_recommender.get_ranking(user)

    cf_recommender = CollaborativeFilteringRecommender()
    cf_ranking = cf_recommender.get_ranking(user)

    merger = Merger(30, 40, 30)
    result = merger.merge(cbf_ranking, cf_ranking, user_preference)
    return {"result": result}

if __name__ == "__main__":
    app.run(debug=True)
