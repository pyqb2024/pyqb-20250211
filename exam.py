# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Programming in Python
# ## Exam: February 11, 2025
#
#
# You can solve the exercises below by using standard Python 3.12 libraries, NumPy, Matplotlib, Pandas, PyMC.
# You can browse the documentation: [Python](https://docs.python.org/3.12/), [NumPy](https://numpy.org/doc/1.26/index.html), [Matplotlib](https://matplotlib.org/3.10.0/users/index.html), [Pandas](https://pandas.pydata.org/pandas-docs/version/2.2/index.html), [PyMC](https://www.pymc.io/projects/docs/en/stable/api.html).
# You can also look at the [slides](https://homes.di.unimi.it/monga/lucidi2425/pyqb00.pdf) or your code on [GitHub](https://github.com).
#
# **It is forbidden to communicate with others or "ask questions" online (i.e., stackoverflow is ok if the answer is already there, but you cannot ask a new question or use ChatGPT and similar products)**
#
# To test examples in docstrings use
#
# ```python
# import doctest
# doctest.testmod()
# ```

import numpy as np   # type: ignore
import pandas as pd  # type: ignore
import matplotlib.pyplot as plt # type: ignore
import pymc as pm   # type: ignore

# ### Exercise 1 (max 3 points)
#
# Plot a bidimensional grid 51x51 of dots. Your picture should be similar to the following (the color is not important):
#
# ![grid](grid.png)
#

pass

# ### Exercise 2 (max 5 points)
#
# On the grid defined in Exercise 1, compute 5 random walks, starting in the central dot, going on for 50 steps of 1 in the horizontal (left or right), vertical (up or down) or diagonal (i.e. a step of 1 in both the horizontal and vertical directions). If a walk reaches the end of the grid, it starts again on the opposite side: in other words, on a line of dots to the left of the leftmost dot there is the rightmost one; same for all the directions.

pass

# ### Exercise 3 (max 4 points)
#
# Plot the walks computed in Exercise 2.

pass

# ### Exercise 4 (max 7 points)
#
# Define a function that takes two random walks, described by the coordinates of the traversed dots, and computes a new one. The resulting walk:
# 1. the first step is taken from the first path
# 2. the second step is the first step of the second path applied on the current position resulting after 1.
# 3. the next steps are computed in the same way alternating steps from the first and the second path; if one path is shorter, when it finishes the next steps come from the remaining part of the longer path
#
# For example: if the two walks are `[(0,0), (1,1), (1,2), (1,3)]` and `[(1,0), (0,1)]`, 
# the resulting walk is `[(0,0), (-1,1), (0,2), (0,3), (0,4)]`
#
#
# To get the full marks, you should declare correctly the type hints and add a doctest string.

pass

# ### Exercise 5 (max 1 points)
#
# Load the data contained in the file `iris.csv` in a Pandas DataFrame.

pass

# ### Exercise 6 (max 2 points)
#
#
# Add to the dataframe two columns for the ratio between petal width and sepal width, and petal length and sepal length.

pass

# ### Exercise 7 (max 6 points)
#
# Make a figure with two plots, on the left plot the three histograms (use different colors) of the width ratios computed in Exercise 6 for each iris class, on the right plot the three histograms of the length ratios.

pass

# ### Exercise 8 (max 5 points)
#
# Consider this statistical model: the sepal width of Iris-setosa is normally distributed, with an unknown mean, and an unknown standard deviation. Your *a priori* estimation for both distribution is an exponential distribution with $\lambda=1$. Use PyMC to sample the posterior distributions after having seen the actual values for Iris-setosa. Plot the results, then print the mean and the standard deviation of the observed sample in your dataset.

pass
