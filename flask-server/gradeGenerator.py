import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define mean and standard deviation
mu, sigma = 7, 1
grades = np.random.normal(mu, sigma, 2945)

# Display the histogram of the samples
# plt.hist(grades, 25, density=True)
# plt.show()

ExcelDataInPandasDataFrame = pd.read_excel("grades_test.xlsx")
YourDataInAList = grades.tolist()
ExcelDataInPandasDataFrame ["OOP"] = YourDataInAList
ExcelDataInPandasDataFrame .to_excel("grades_test.xlsx",index=False)