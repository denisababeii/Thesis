from venv import create
from contentBased import ContentBasedFilteringRecommender
from coursesCleaner import CoursesCleaner
from collaborativeFiltering import CollaborativeFilteringRecommender

user = [54.0,	55.0,	19.0,	14.0,	47.0,	48.0,	15.0,	55.0,	45.0,	43.0] # The list of grades for the current user
courses = CoursesCleaner().get_courses()

CBFrecommender = ContentBasedFilteringRecommender(courses)
print(CBFrecommender.get_ranking(user))

CFrecommender = CollaborativeFilteringRecommender()
print(CFrecommender.get_ranking(user))

