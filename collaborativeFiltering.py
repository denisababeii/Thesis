import pandas as pd
from scipy import spatial

NO_PACKAGES = 3 # these ones I can compute in the hybrid as in ContentBasedRecommender
NO_COMPULSORY = 10

data = pd.read_csv('GRADES.csv')

# optionals = []
# for i in range(NO_PACKAGES):
#     optionals.extend(data[f"Elective {i+1}"].unique())

USER = [54.0,	55.0,	19.0,	14.0,	47.0,	48.0,	15.0,	55.0,	45.0,	43.0] # The list of grades for the current user

cols= list(data.columns.values)
compulsory_courses = data[cols[1:NO_COMPULSORY+1]]

similarity = pd.DataFrame(columns = ['Cosine Similarity'])
for index, row in compulsory_courses.iterrows():
  x = spatial.distance.cosine(USER, row)
  similarity = similarity.append({'Cosine Similarity':x}, ignore_index=True)

similar_data = pd.concat([data,similarity], ignore_index=False, axis=1, verify_integrity=False)
similar_data = similar_data.sort_values(by=['Cosine Similarity'], ascending=False)
# Get top data based on set percentage
percentage = 15
similar_data = similar_data.head(int(len(similar_data)*(percentage/100)))

# grouped = similar_data.groupby(['Elective 1', 'Elective 2', 'Elective 3']).mean()

