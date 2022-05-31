from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ContentBasedFilteringRecommender:
    def __init__(self, courses):
        self.courses = courses
        self.similarities = self.compute_similarities()

    def compute_similarities(self):
        tfidf = TfidfVectorizer(analyzer='word')
        matrix = tfidf.fit_transform(self.courses['CleanDescription'])
        cosine_similarities = cosine_similarity(matrix)
        similarities = {}
        # Store in similarities the names and packages of the courses along with the value of the cosine similarity
        for i in range(len(cosine_similarities)):
            similarities[self.courses['Name'].iloc[i]] = [(cosine_similarities[i][x], self.courses['Name'][x],
                                                           self.courses['Package'][x]) for x in
                                                          range(len(cosine_similarities[i]))]
        return similarities

    @staticmethod
    def get_most_similar_electives_per_package(compulsory_course_similarities):
        # Retrieve only the similarities with elective courses
        # Entries with the package marked as 0 (corresponding to compulsory courses) are filtered out from the list of similarities
        electives = list(filter(lambda similarity: similarity[2] != 0, compulsory_course_similarities))
        # Store the number of available packages
        packages = len(set([x[2] for x in electives]))
        # Create a dictionary with an entry for each package
        # An entry represents a pair of similarity and name
        recommendation = dict([(i + 1, [-1, ""]) for i in range(packages)])
        for i in range(len(electives)):
            # Store in the dictionary the electives with the highest similarity for the current package
            if recommendation[electives[i][2]][0] < electives[i][0]:
                recommendation[electives[i][2]] = [electives[i][0], electives[i][1]]
        return recommendation

    @staticmethod
    def print(recommendation):
        for i in range(1, len(recommendation) + 1):
            print(f"{recommendation[i][1]} from Package {i} with {round(recommendation[i][0], 3)} similarity score")

    def recommend(self, compulsory_course):
        # Get the cosine similarities values for the current compulsory course
        similarities = self.similarities[compulsory_course]
        # Return the highest similarities with elective courses
        return self.get_most_similar_electives_per_package(compulsory_course_similarities=similarities)

    @staticmethod
    def find(ranking, combination):
        index = -1
        for item in ranking:
            index += 1
            if item[0] == combination[0] and item[1] == combination[1] and item[2] == combination[2]:
                return index
        return -1

    @staticmethod
    def compute_weight(combination, ranking):
        weight = 0
        count = 0
        # The weight is computed as the average of the weights of the duplicate combinations
        for item in ranking:
            if item[0] == combination[0] and item[1] == combination[1] and item[2] == combination[2]:
                weight += item[3]
                count += 1
        weight /= count
        return weight

    def process_ranking(self, ranking):
        # Values in cbf_ranking are not necessarily unique as compulsory courses can be similar to the same set of elective courses
        # The ranking is processed so as to only contain unique values, with weights computed as the sum of the previous weights assigned to each combination 
        processed_ranking = []
        for combination in ranking:
            # Use a helper function which returns the index of the combination in the ranking in case it is found, or -1 otherwise
            index = self.find(processed_ranking, combination)
            if index == -1:
                # If the element has not been processed before, it is added to the new ranking with the newly computed weight
                combination[3] = self.compute_weight(combination, ranking)
                processed_ranking.append(combination)
        return processed_ranking

    def get_ranking(self, user):
        compulsory_courses = self.courses[self.courses["Type"] != "Optional"]
        ranking = []
        for index, course in compulsory_courses.iterrows():
            recommendation = self.recommend(course['Name'])
            # Only the names of the electives are stored, without the similarity score
            electives = [pair[1] for pair in list(recommendation.values())]
            # Python list decomposition is used to provide the required output format
            # user[index] represents the grade of the user at the compulsory course from the position given by index
            ranking.append([*electives, user[index]])
            ranking = self.process_ranking(ranking)
        return ranking
