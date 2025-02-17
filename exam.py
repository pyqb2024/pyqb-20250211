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

x = np.linspace(-25, 25, 51)
y = np.linspace(-25, 25, 51)
grid = np.meshgrid(x, y)

fig, ax = plt.subplots(figsize=(10,10))
ax.set_axis_off()
ax.set_aspect('equal')
_ = ax.scatter(grid[0], grid[1], s=.2)


# ### Exercise 2 (max 5 points)
#
# On the grid defined in Exercise 1, compute 5 random walks, starting in the central dot, going on for 50 steps of 1 in the horizontal (left or right), vertical (up or down) or diagonal (i.e. a step of 1 in both the horizontal and vertical directions). If a walk reaches the end of the grid, it starts again on the opposite side: in other words, on a line of dots to the left of the leftmost dot there is the rightmost one; same for all the directions.

def one_step(start: tuple[int, int], step: tuple[int, int], dim: int = 25) -> tuple[int, int]:
    """Return the point after a step applied to start. 
    The borders are at -dim and dim. 
    
    >>> one_step((2, 1), (1, 1))
    (3, 2)
    
    >>> one_step((0, 16), (0, 1), 16)
    (0, -16)
    """
    
    ris = [0, 0]
    for axis in (0, 1):
        ris[axis] = start[axis] + step[axis]
        if ris[axis] > dim:
            ris[axis] = ris[axis] - dim*2 - 1
        elif ris[axis] < -dim:
            ris[axis] = ris[axis] + dim*2 + 1
    
    return (ris[0], ris[1])    


# +
walk = np.zeros((5, 100, 2))

for w in range(0, 5):
    steps = np.random.randint(-1, 1+1, size=(100-1, 2))

    i = 1
    for s in steps:
        walk[w][i] = np.array(one_step((walk[w][i-1][0], walk[w][i-1][1]), (s[0], s[1])))
        i = i + 1
# -

# ### Exercise 3 (max 3 points)
#
# Plot the walks computed in Exercise 2.

fig, ax = plt.subplots(figsize=(10,10))
ax.scatter(grid[0], grid[1], s=.2, color='black')
ax.set_axis_off()
ax.set_aspect('equal')
for w in range(0,5):
    _ = ax.plot(walk[w,:,0], walk[w,:,1])


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

# +
def step_between(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    """Compute the delta to step from a to b.

    >>> step_between((1, 0), (0, 1)) == (-1, 1)
    True
    """
    return b[0] - a[0], b[1] - a[1]

def merge_walks(w1: list[tuple[int, int]], w2: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge w1 and w2.
    
    >>> merge_walks([(0, 0), (1, 1), (1, 2), (1,3)], [(1, 0), (0, 1)]) == [(0, 0), (-1, 1), (0, 2), (0, 3), (0, 4)]
    True
    """
    steps1 = [step_between(w1[i], w1[i+1]) for i in range(len(w1)-1)]
    steps2 = [step_between(w2[i], w2[i+1]) for i in range(len(w2)-1)]
    ris = w1[:1]
    while len(steps1 + steps2) > 0:
        if len(steps2) > 0:
            n = one_step(ris[-1], steps2.pop(0))
            ris.append(n)
        if len(steps1) > 0:
            n = one_step(ris[-1], steps1.pop(0))
            ris.append(n)
    return ris


# -

import doctest
doctest.testmod()

# ### Exercise 5 (max 1 points)
#
# Load the data contained in the file `iris.csv` in a Pandas DataFrame.

iris = pd.read_csv('iris.csv', sep=',')
iris.head()

# ### Exercise 6 (max 2 points)
#
#
# Add to the dataframe two columns for the ratio between petal width and sepal width, and petal length and sepal length.

iris['width ratio'] = iris['petal width'] / iris['sepal width']
iris['length ratio'] = iris['petal length'] / iris['sepal length']
iris.head()

# ### Exercise 7 (max 6 points)
#
# Make a figure with two plots, on the left plot the three histograms (use different colors) of the width ratios computed in Exercise 6 for each iris class, on the right plot the three histograms of the length ratios.

# +
fig, ax = plt.subplots(ncols=2, figsize=(10,5))

for k in iris['class'].unique():
    ax[0].hist(iris[iris['class'] == k]['width ratio'], bins='auto', density=True, label=k)
    ax[0].legend()
    ax[1].hist(iris[iris['class'] == k]['length ratio'], bins='auto', density=True, label=k)
    ax[1].legend()


# -

# ### Exercise 8 (max 5 points)
#
# Consider this statistical model: the sepal width of Iris-setosa is normally distributed, with an unknown mean, and an unknown standard deviation. Your *a priori* estimation for both distribution is an exponential distribution with $\lambda=1$. Use PyMC to sample the posterior distributions after having seen the actual values for Iris-setosa. Plot the results, then print the mean and the standard deviation of the observed sample in your dataset.

# +
mymodel = pm.Model()


with mymodel:
    mu_sw = pm.Exponential('mu_sw', 1)
    s_sw = pm.Exponential('s_sw', 1)
    
    sw = pm.Normal('sw', mu=mu_sw, sigma=s_sw, observed=iris.query('`class` == "Iris-setosa"')['sepal width'])
    
    post = pm.sample()
    
# -

with mymodel:
    pm.plot_posterior(post)

iris[iris['class'] == 'Iris-setosa']['sepal width'].agg(['mean','std'])
