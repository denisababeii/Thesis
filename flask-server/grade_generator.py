import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import configparser

def process_grades(grades):
    grades = grades.tolist()
    for index in range(len(grades)):
        # Transform to integer values
        grades[index] = int(grades[index])
        
        # The values out of the interval [5,10] 
        # are rounded to the margins
        if grades[index] < 5:
            grades[index] = 5
        if grades[index] > 10:
            grades[index] = 10
    return grades

def generate_grades_per_package(df, package):
    elective_names = df[package].unique()
    for name in elective_names:
        data_per_elective = df[df[package] == name]
        size = len(data_per_elective.index)
        mu, sigma = 8, 1
        grades = np.random.normal(mu, sigma, size)
        grades = process_grades(grades)
        df.loc[df[package] == name, f"{package} Mark"] = grades


def generate_grades_compulsory(compulsory_courses, file):
    df = pd.read_excel(file)

    for index in range(len(compulsory_courses)):
        # Define mean and standard deviation
        mu, sigma, size = 8, 1, 2944
        grades = np.random.normal(mu, sigma, size)

        # Display the histogram of the samples
        plt.hist(grades, 25, density=True)
        plt.show()

        grades = process_grades(grades)

        # Display the histogram of the samples
        plt.hist(grades, 25, density=True)
        plt.show()

        df[compulsory_courses[index]] = grades

    df.to_excel(file, index=False)

def generate_grades_elective(file, packages):
    df = pd.read_excel(file)
    for package in packages:
        generate_grades_per_package(df, package)
    df.to_excel(file, index=False)

parser = configparser.ConfigParser()
parser.read("config.txt")
file = parser.get("config", "grades")
compulsory_courses = parser.get("config", "compulsory_courses").split(",")
generate_grades_compulsory(compulsory_courses, file)
packages = parser.get("config", "packages").split(",")
generate_grades_elective(file, packages)
