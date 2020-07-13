# Traffic Light Classifier

This is the fourth and final project in Udacity's Introduction to Self-Driving Cars Nanodegree. The project emphasizes computer vision fundamentals and techniques without machine learning. Topics covered in the project notebook include pre-processing, feature extraction, classification using if-else logic, and evaluation. The project notebook uses a brightness feature to produce a model with 95% accuracy on test data. In addition, the model never misclassifies a red light as green (which would be a very bad thing for a self-driving car to do!).

## Installation

This project requires Jupyter Notebooks, which can be installed as part of the [Anaconda distribution](https://www.anaconda.com/). Once installed, launch Jupyter Notebooks by running `jupyter notebook` in the terminal.

Additionally, ensure that you have pip installed the `cv2` Python package by running `pip install opencv-python`

## Usage

This project consists of the following files:

* `Traffic_Light_Classifier.ipynb` - Jupyter notebook containing all of the code for this project. Each cell can be run from top to bottom.

    The notebook is sub-divided into several sections:
    * _Loading and Visualizing the Traffic Light Dataset_ uses the helper function in `helpers.py` to load our train and test data. This section also uses `matplotlib` to display a few sample images from the traffic lights dataset.
    * _Pre-Process the Data_ standardizes the inputs and outputs for the classification. This step utilizes one-hot encoding and image resizing.
    * _Feature Extraction_ creates a brightness feature using RGB to HSV color space conversion, additional image cropping, color masking, and a brightness histogram. The final feature is the pixel row number that displays the highest average pixel brightness.
    * _Classification and Visualizing Error_ completes and runs the traffic light classifier. Outstanding errors in the test set are identified in order to determine where the model has deficiencies. This section also includes some commented-out code used for troubleshooting and tinkering with different approaches for masking and cropping images.

* `helpers.py` - Python file containing a single helper function that loads the traffic lights dataset from a directory of images into a list.

* `test_functions.py` - A Python file with tests for one-hot encoding and classification. In addition to achieving 90% accuracy, the classifier must pass these tests in order to constitute a passing submission.

## Citations

Udacity provided the files necessary to complete this project, including project tests in `test_functions.py`. My project work can be found in `Traffic_Light_Classifier.ipynb`.
