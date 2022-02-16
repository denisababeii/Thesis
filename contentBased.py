from pickletools import optimize
import numpy as np
from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ContentBasedRecommender:
    def __init__(self, courses):
        self.courses = courses
        self.matrix_similar = self.build_matrix()

    def build_matrix(self):
        tfidf = TfidfVectorizer(analyzer='word')
        matrix = tfidf.fit_transform(self.courses['CleanDescription'])
        cosine_similarities = cosine_similarity(matrix)
        similarities = {}
        for i in range(len(cosine_similarities)):
            similarities[self.courses['Name'].iloc[i]] = [(cosine_similarities[i][x], self.courses['Name'][x], self.courses['Package'][x]) for x in range(len(cosine_similarities[i]))]
        return similarities

    def filter(self, recom_course):
        optionals = list(filter(lambda course: course[2] != 0, recom_course))
        packages = len(set([x[2] for x in optionals]))
        recommendation = dict([(i+1, [-1, ""]) for i in range(packages)])
        for i in range(len(optionals)):
            if(recommendation[optionals[i][2]][0] < optionals[i][0]):
                recommendation[optionals[i][2]] = [optionals[i][0], optionals[i][1]]
        return recommendation

    def print(self, recommendation):
        for i in range(1, len(recommendation)+1):
            print(f"{recommendation[i][1]} from Package {i} with {round(recommendation[i][0], 3)} similarity score")

    def recommend(self, course):
        recom = self.matrix_similar[course]
        return self.filter(recom_course=recom)