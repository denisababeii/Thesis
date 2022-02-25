from tokenize import group
import pandas as pd
from scipy import spatial

NO_PACKAGES = 3 # these ones I can compute in the hybrid as in ContentBased
NO_COMPULSORY = 10

class CollaborativeFilteringRecommender:
    def __init__(self, grades_file='GRADES.csv'):
      self.grades = pd.read_csv(grades_file)

    def get_ranking(self, user):
      cols= list(self.grades.columns.values)
      compulsory_courses = self.grades[cols[1:NO_COMPULSORY+1]]

      similarity = pd.DataFrame(columns = ['Cosine Similarity'])
      for index, row in compulsory_courses.iterrows():
        x = spatial.distance.cosine(user, row)
        similarity = similarity.append({'Cosine Similarity':x}, ignore_index=True)

      similar_data = pd.concat([self.grades,similarity], ignore_index=False, axis=1, verify_integrity=False)
      similar_data = similar_data.sort_values(by=['Cosine Similarity'], ascending=False)
      # Get top data based on set percentage
      percentage = 15
      similar_data = similar_data.head(int(len(similar_data)*(percentage/100)))

      elective_list = []
      for i in range (NO_PACKAGES):
        elective_list.append(f"Elective {i+1}")
      grouped = similar_data.groupby(elective_list).mean()

      mark_list = []
      for i in range (NO_PACKAGES):
        mark_list.append(f"Elective {i+1} Mark")
      marks = grouped[mark_list]

      marks.drop(marks[(marks['Elective 1 Mark'] < 50) | (marks['Elective 2 Mark'] < 50) | (marks['Elective 3 Mark'] < 50)].index, inplace=True)

      marks["Average"] = marks[mark_list].mean(axis=1)
      marks = marks.sort_values(by=['Average'], ascending=False)

      ranks = marks.drop(labels=mark_list, axis=1, inplace=True)

      ranks = marks.to_records()
      return ranks

# optionals = []
# for i in range(NO_PACKAGES):
#     optionals.extend(data[f"Elective {i+1}"].unique())