import numpy as np
import pandas as pd
from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from wordcloud import STOPWORDS 

courses = pd.read_csv('COURSES.csv')

stopwords = ["case", "weeks", "explanations", "course", "exposition", "concepts", "week", "studies", "interactive", "explanation", "exposure", "example", "examples", "description", "discipline", "demonstration", "presentation", "discussion", "conversation", "dialogue", "debate", "didactical"]
stopwords.extend(STOPWORDS)


tfidf = TfidfVectorizer(analyzer='word', stop_words=stopwords)
matrix = tfidf.fit_transform(courses['Description'])

cosine_similarities = cosine_similarity(matrix)

similarities = {}
for i in range(len(cosine_similarities)):
    similar_indices = cosine_similarities[i].argsort()[:-10:-1] 
    similarities[courses['Name'].iloc[i]] = [(cosine_similarities[i][x], courses['Name'][x]) for x in similar_indices][1:]

class ContentBasedRecommender:
    def __init__(self, matrix):
        self.matrix_similar = matrix

    def _print_message(self, course, recom_course):
        rec_items = len(recom_course)
        
        print(f'The {rec_items} recommended courses for {course} are:')
        for i in range(rec_items):
            print(f"{recom_course[i][1]} with {round(recom_course[i][0], 3)} similarity score") 
            print("--------------------")
        
    def recommend(self, recommendation):
        course = recommendation['course']
        number_courses = recommendation['number_courses']
        recom_course = self.matrix_similar[course][:number_courses]
        self._print_message(course=course, recom_course=recom_course)

recommedations = ContentBasedRecommender(similarities)

recommendation = {
    "course": courses['Name'].iloc[1],
    "number_courses": 1
}
recommedations.recommend(recommendation)

recommendation2 = {
    "course": courses['Name'].iloc[2],
    "number_courses": 1
}
recommedations.recommend(recommendation2)