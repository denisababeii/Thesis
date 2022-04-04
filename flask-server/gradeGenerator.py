import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def generate_grades(compulsory_courses, file):
    df = pd.read_excel(file)

    for index in range(len(compulsory_courses)):
        # Define mean and standard deviation
        mu, sigma, size = 8, 1, 2944
        grades = np.random.normal(mu, sigma, size)

        # Display the histogram of the samples
        plt.hist(grades, 25, density=True)
        plt.show()

        grades = grades.tolist()
        for subindex in range(len(grades)):
            # Transform to integer values
            grades[subindex] = int(grades[subindex])
            
            # The values out of the interval [6,10] 
            # are rounded to the margins
            if grades[subindex] < 6:
                grades[subindex] = 6
            if grades[subindex] > 10:
                grades[subindex] = 10

        # Display the histogram of the samples
        plt.hist(grades, 25, density=True)
        plt.show()

        df[compulsory_courses[index]] = grades

    df.to_excel(file, index=False)


file = "grades.xlsx"
compulsory_courses = ['OOP', 'DSA', 'DBMS', 'ASC', 'FP', 'SE', 'FLCD', 'OS', 'WEBDEV', 'PDP']
elective_courses_1 = ['NLP', 'AR_VR', 'SVV']
elective_courses_2 = ['CC', 'CS']
elective_courses_3 = ['IOT', 'ML']
generate_grades(compulsory_courses, file)