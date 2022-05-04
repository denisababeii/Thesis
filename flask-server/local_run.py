from courses_cleaner import CoursesCleaner
from content_based import ContentBasedFilteringRecommender
from collaborative import CollaborativeFilteringRecommender
from merger import Merger

grades=[6, 7, 8, 9, 10, 8, 7, 8, 9, 10]
preference=["Computer science investigations -an iot perspective", "Advanced compiler design", "Academic ethics and integrity (in computer science)", 10]

courses = CoursesCleaner().get_courses()

cbf_recommender = ContentBasedFilteringRecommender(courses)
cbf_ranking = cbf_recommender.get_ranking(grades)

cf_recommender = CollaborativeFilteringRecommender()
cf_ranking = cf_recommender.get_ranking(grades)

merger = Merger(50, 20, 30)
result = merger.merge(cbf_ranking, cf_ranking, preference)
print(result)