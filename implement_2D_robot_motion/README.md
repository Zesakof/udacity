# Implement 2D Robot Motion Project

This is the second project in Udacity's Introduction to Self-Driving Cars Nanodegree. It emphasizes C++ fundamentals such as headers, control flow, debugging, and standard libraries. The final output is a simulation of probabilistic robot motion and localization on a 4x4 grid.

## Installation

This project requires a compiler that is compatible with C++11, such as g++.

## Usage

This project consists of the following files:

* `localizer.cpp` - C++ file containing functions that allow the robot to initialize itself on a grid, move on x and y axes, and update its location probabilities using Bayesian math.

* `helpers.cpp` - C++ file containing helper functions for `localizer.cpp` to leverage. Examples include normalizing probabilities and adding uncertainty to the robot's movements.

* `simulate.cpp` - C++ file containing a Simulation class. This class uses the functions in `localizer.cpp` to run a simulation of robot motion on a 4x4 grid.

    To run the simulation, execute the following the terminal:
    ```
    cd implement_2D_robot_motion
    g++ -std=c++11 simulate.cpp
    ./a.out
    ```

* `debugging_helpers.cpp` - C++ file containing functions designed to help debug the project.

* `tests.cpp` - C++ file containing the tests that qualify a passing submission.

## Citations

Udacity provided many of the files necessary to complete this project, including project tests in `test.cpp`. My project work can be found in `localizer.cpp` and `simulate.cpp`.
