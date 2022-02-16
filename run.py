from contentBased import ContentBasedRecommender
from coursesCleaner import CoursesCleaner

courses = CoursesCleaner().get_courses()
recommender = ContentBasedRecommender(courses)
compulsory_courses = courses[courses["Type"] != "Optional"]
for index, course in compulsory_courses.iterrows():
    print(course['Name'])
    recommendation = recommender.recommend(course['Name'])
    recommender.print(recommendation)
    print("------------------------")