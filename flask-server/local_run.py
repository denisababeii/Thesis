from courses_cleaner import CoursesCleaner
from content_based import ContentBasedFilteringRecommender
from collaborative import CollaborativeFilteringRecommender
from merger import Merger

grades=[6, 7, 8, 9, 10, 8, 7, 8, 9, 10]
preference=["IOT", "ACD", "EI", 10]

courses = CoursesCleaner().get_courses()

cbf_recommender = ContentBasedFilteringRecommender(courses)
cbf_ranking = cbf_recommender.get_ranking(grades)
print(cbf_ranking)

cf_recommender = CollaborativeFilteringRecommender()
cf_ranking = cf_recommender.get_ranking(grades)
print(cf_ranking)

merger = Merger(50, 20, 30)
result = merger.merge(cbf_ranking, cf_ranking, preference)
print(result)