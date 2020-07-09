# Implement Matrix Class Project

This is the first project in Udacity's Introduction to Self-Driving Cars Nanodegree. It emphasizes object-oriented programming and builds a matrix class in python

## Installation

This project is largely self-contained and only requires common python packages such as `matplotlib` and `pandas`

## Usage

This project consists of the following files:

* `matrix.py` - The main python file that contains helper functions, basic matrix arithmetic, operator overloading, and advanced matrix operations involving minors and cofactors. The mathematical background on these advanced operations is available [here](https://ltcconline.net/greenl/courses/203/MatricesApps/cofactors.htm)

* `matrix_playground.ipynb` - A notebook used for testing the methods implemented in `matrix.py`. Includes additional tests to calculate the inverses and determinants of 3x3 and 4x4 matrices

* `matrix_cheat_sheet.ipynb` - A notebook summarizing the material covered in this unit of the Introduction to Self-Driving Cars Nanodegree

* `kalman_filter_demo.ipynb` - A notebook that implements a Kalman Filter using the Matrix class in `matrix.py`. This includes visualizations of vehicle position, velocity, acceleration, and simulated lidar data

* `test.py` - A python file containing the tests that qualify a passing submission

* `datagenerator.py` - A python file that generates ground truth data for simulating autonomous vehicle motion in `kalman_filter_demo.ipynb`

## Citations

Udacity provided the files necessary to complete this project, including project tests in `test.py` and visualizations in `kalman_filter_demo.ipynb`. My project work can be found in `matrix.py`.
