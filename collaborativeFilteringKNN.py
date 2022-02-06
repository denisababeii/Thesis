import pandas as pd
import numpy as np
from scipy import sparse

# Inspired by the MovieLens example from https://github.com/topspinj/recommender-tutorial/blob/master/part-1-item-item-recommender.ipynb

# Read CSV file
df = pd.read_csv("generatedData.csv")

# Drop first column, with the StudentID
df = df.iloc[: , 1:]

# Create the utility matrix
matrix = df.to_numpy()
sparseMatrix = sparse.csr_matrix(matrix)

# Check sparsity
# Matrix sparsity should be no lower than 0.5%
sparsity = sparseMatrix.count_nonzero()/(sparseMatrix.shape[0]*sparseMatrix.shape[1])

