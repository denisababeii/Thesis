import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import configparser

def process_grades(grades):
    grades = grades.tolist()
    for index in range(len(grades)):
        # Transform to integer values
        grades[index] = int(grades[index])
        
        # The values out of the interval [5,10] are rounded to the margins
        if grades[index] < 5:
            grades[index] = 5
        if grades[index] > 10:
            grades[index] = 10
    return grades

def generate_grades_per_package(df, package):
    # Select the unique course names in the current package column (e.g. column ’Elective 1’)
    elective_names = df[package].unique()
    # Set the parameters
    mu, sigma = 8, 1
    for name in elective_names:
        # Select only rows containing the current course name
        data_per_elective = df[df[package] == name]
        # Get the number of selected rows
        size = len(data_per_elective.index)
        # Generate grades corresponding to the selected rows
        grades = np.random.normal(mu, sigma, size)
        # Filter the grades
        grades = process_grades(grades)
        # Insert the generated grades in the selected rows, in the designated ’Mark’ column (e.g. column ’Elective 1 Mark’)
        df.loc[df[package] == name, f"{package} Mark"] = grades


def generate_grades_compulsory(compulsory_courses, file):
    # Store Excel data in a Dataframe object
    df = pd.read_excel(file)
    # Define mean and standard deviation
    mu, sigma, size = 8, 1, 2944

    # Generate a collection of grades per course
    for index in range(len(compulsory_courses)):
        grades = np.random.normal(mu, sigma, size)

        # Display the histogram of the samples
        plt.hist(grades, 25, density=True)
        plt.show()

        # Filter the grades
        grades = process_grades(grades)

        # Display the histogram of the samples
        plt.hist(grades, 25, density=True)
        plt.show()
        
        # Insert the grades in the corresponding column of the DataFrame
        df[compulsory_courses[index]] = grades
    # Write the modified DataFrame object to the Excel file
    df.to_excel(file, index=False)

def generate_grades_elective(file, packages):
    # Store Excel data in a Dataframe object
    df = pd.read_excel(file)
    # Generate grades for each availabe package of elective courses
    for package in packages:
        generate_grades_per_package(df, package)
    # Write the modified DataFrame object to the Excel file
    df.to_excel(file, index=False)

parser = configparser.ConfigParser()
parser.read("config.txt")
file = parser.get("config", "grades")
compulsory_courses = parser.get("config", "compulsory_courses").split(",")
generate_grades_compulsory(compulsory_courses, file)
packages = parser.get("config", "packages").split(",")
generate_grades_elective(file, packages)
