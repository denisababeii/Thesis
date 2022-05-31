import pandas as pd
from scipy import spatial

pd.options.mode.chained_assignment = None  # Ignore False Positive warning
# See post https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas

class CollaborativeFilteringRecommender:
    def __init__(self, grades, noPackages, noCompulsory):
        self.grades = grades
        self.noPackages = noPackages
        self.noCompulsory = noCompulsory
        self.percentage = 15
        
    def get_ranking(self, user_grades):
        columns = list(self.grades.columns.values)
        # Store the grades from the compulsory courses for all previous students
        compulsory_courses = self.grades[columns[1:self.noCompulsory + 1]]

        similarity = pd.DataFrame(index=range(len(compulsory_courses)))
        similarity['Cosine Similarity'] = 0
        # Compute the cosine similarity between the current user and each previous student
        for index, row in compulsory_courses.iterrows():
            similarity['Cosine Similarity'][index] = spatial.distance.cosine(user_grades, row)

        # Concatenate the similarities to the corresponding grades
        similar_data = pd.concat([self.grades, similarity], ignore_index=False, axis=1, verify_integrity=False)
        # Sort the rows descending by the similarity
        similar_data = similar_data.sort_values(by=['Cosine Similarity'], ascending=False)
        # Get top data based on set percentage (currently set to 15%)
        similar_data = similar_data.head(int(len(similar_data) * (self.percentage / 100)))
        
        elective_list = []
        for i in range(self.noPackages):
            elective_list.append(f"Elective_{i + 1}")
        # Group all data by elective name and compute for each group the average grade
        groups = similar_data.groupby(elective_list).mean()

        elective_mark_list = []
        for i in range(self.noPackages):
            elective_mark_list.append(f"Elective_{i + 1}_Mark")
        # Select only the averages per group and discard useless data
        data = groups[elective_mark_list]

        # Compute the total average of the grades corresponding to each combination of electives
        # E.g.: elective X has an average grade of 5.25, elective Y - 6.5 and elective Z - 8. So the total average of the combination of electives X-Y-Z is (5.25+6.5+8)/3~= 6.58.
        data["Average"] = data[elective_mark_list].mean(axis=1)
        # Sort descending by total average
        data = data.sort_values(by=['Average'], ascending=False)

        # Drop the columns with the grades, in order to store only the names of the elective courses
        data.drop(labels=elective_mark_list, axis=1, inplace=True)

        ranks = [list(x) for x in data.to_records()]
        return ranks
