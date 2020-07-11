# Implement Route Planner

This is the third project in Udacity's Introduction to Self-Driving Cars Nanodegree. The project implements the A* search algorithm, though this course unit also covers breadth-first and uniform cost search methods. Python data structures and algorithm heuristics are also covered in the project notebook.

## Installation

This project requires Jupyter Notebooks, which can be installed as part of the [Anaconda distribution](https://www.anaconda.com/). Once installed, launch Jupyter Notebooks by running `jupyter notebook` in the terminal.

Additional, ensure that you have pip installed the following Python packages: `networkx`, `chart_studio`, and `plotly`.

## Usage

This project consists of the following files:

* `project_notebook.ipynb` - Jupyter notebook containing all of the code for this project. Each cell can be run from top to bottom.

    The notebook is sub-divided into several sections:
    * _The map_ and _The algorithm_ were provided by Udacity and set-up the map and PathPlanner class, respectively.

    * _Data structures_ and _Set initial variables_ initialize fields that the PathPlanner class needs to track information about its nodes, their neighbors, and the map that it is navigating.

    * _Get node information_ defines functions that retrieve node information such as neighbors, f-score, and whether the node has already been traversed.

    * _Scores and costs_ and _Recording the best path_ define functions that calculate the f, g, and h scores that the algorithm uses to compute total path cost.

    * The remainder of the notebook consists of tests and theoretical questions surrounding A* and algorithm heuristics.

* `helpers.py` - Python file with functions that load and display the large and small maps traversed in this project.

* `test.py` - Python file that tests whether the algorithm in `project_notebook.ipynb` produces the correct output for three test cases. That is, the shortest path from point 5 to point 34, from 5 to 5, and from 8 to 24.

## Citations

Udacity provided the files necessary to complete this project, including project tests in `test.py`. My project work can be found in `project_notebook.ipynb`.
