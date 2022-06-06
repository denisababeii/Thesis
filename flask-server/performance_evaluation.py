from collaborative import CollaborativeFilteringRecommender
from db_util import DatabaseUtils
from merger import Merger
from content_based import ContentBasedFilteringRecommender
from courses_cleaner import CoursesCleaner

def is_in_k_recommendations(k, noPackages, top_k, actual_result):
    # Return 1 if the actual result is in the first k recommendations; return 0 otherwise
    if len(top_k) < k:
        k = len(top_k)
    for i in range(k):
        found = True
        for j in range(noPackages):
            if top_k[i][j] != actual_result[j]:
                found = False
        if found:
            return 1
    return 0
                
def evaluate_one_call_at_k_top_ranked(k, cbf_percentage, cf_percentage, user_percentage, user_rank):
    db = DatabaseUtils()

    generated_grades = db.get_generated_grades()
    # Split the generated grades in two sets
    middle = int(len(generated_grades)/2)
    first_set = generated_grades.iloc[:middle]
    second_set = generated_grades.iloc[middle:]

    noPackages = len(db.get_packages().split(","))
    noCompulsory = len(db.get_compulsory_courses().split(","))
    cf_recommender = CollaborativeFilteringRecommender(first_set, noPackages, noCompulsory)
    courses = CoursesCleaner(db).get_courses()
    cbf_recommender = ContentBasedFilteringRecommender(courses)
    merger = Merger(cbf_percentage, cf_percentage, user_percentage, user_rank)

    one_call_at_k_top_ranked = 0

    for index, row in second_set.iterrows():
        row_as_list = row.tolist()
        grades = row_as_list[1:noCompulsory+1]
        # Compute recommendation
        cf_ranking = cf_recommender.get_ranking(grades)
        cbf_ranking = cbf_recommender.get_ranking(grades)
        actual_result = row_as_list[noCompulsory+1:noCompulsory+1+noPackages]
        result = merger.merge(cbf_ranking, cf_ranking, actual_result)
        # Check if actual result is between top k recommendations
        top_k = result[0:k]
        one_call_at_k_top_ranked += is_in_k_recommendations(k, noPackages, top_k, actual_result)

    # Compute ratio of users which receive their actual result as one of the top k recommendations
    ratio = one_call_at_k_top_ranked/middle
    return ratio

ratio = evaluate_one_call_at_k_top_ranked(1, 50, 20, 30, 7)
print(ratio*100)

ratio = evaluate_one_call_at_k_top_ranked(1, 33.33, 33.33, 33.33, 7)
print(ratio*100)



ratio = evaluate_one_call_at_k_top_ranked(3, 50, 50, 0, 7)
print(ratio*100)

ratio = evaluate_one_call_at_k_top_ranked(3, 50, 20, 30, 7)
print(ratio*100)

ratio = evaluate_one_call_at_k_top_ranked(3, 33.33, 33.33, 33.33, 7)
print(ratio*100)


ratio = evaluate_one_call_at_k_top_ranked(5, 50, 50, 0, 7)
print(ratio*100)

ratio = evaluate_one_call_at_k_top_ranked(5, 50, 20, 30, 7)
print(ratio*100)

ratio = evaluate_one_call_at_k_top_ranked(5, 33.33, 33.33, 33.33, 7)
print(ratio*100)
