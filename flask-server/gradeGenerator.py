import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel("grades.xlsx")

compulsory_courses = ['OOP', 'DSA', 'DBMS', 'ASC', 'FP', 'SE', 'FLCD', 'OS', 'WEBDEV', 'PDP']
elective_courses_1 = ['NLP', 'AR_VR', 'SVV']
elective_courses_2 = ['CC', 'CS']
elective_courses_3 = ['IOT', 'ML']

for i in range(len(compulsory_courses)):
    # Define mean and standard deviation
    mu, sigma = 7, 1
    grades = np.random.normal(mu, sigma, 2944)


    # Display the histogram of the samples
    # plt.hist(grades, 25, density=True)
    # plt.show()

    grades = grades.tolist()
    for j in range(len(grades)):
        grades[j] = int(grades[j])
        if grades[j] < 6:
            grades[j] = 6
        if grades[j] > 10:
            grades[j] = 10

    df[compulsory_courses[i]] = grades

df.to_excel("grades.xlsx",index=False)