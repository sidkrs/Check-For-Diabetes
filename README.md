# Diabetes Prediction Program

This project uses a Naive Bayes classifier trained on CDC Diabetes Health Data to predict whether a user is prediabetic or diabetic based on their responses to a series of health-related questions.

## Features

- Utilizes CDC Diabetes Health Indicators dataset
- Implements a Naive Bayes classifier optimized for recall
- Balances the dataset using SMOTE (Synthetic Minority Over-sampling Technique)
- Interactive questionnaire for user input
- Provides prediction along with probability of diabetes

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/diabetes-prediction.git
   ```
2. Navigate to the project directory:
   ```
   cd diabetes-prediction
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script:
   ```
   python Results.py
   ```
2. Answer the series of health-related questions when prompted.
3. The program will provide a prediction on whether you are likely to be prediabetic or diabetic, along with the probability.

## Files

- `Results.py`: Main script that loads the model, asks questions, and makes predictions
- `Questions.py`: Contains the questionnaire logic
- `Testing Best Parameters.py`: Script used to find the best parameters for the Naive Bayes model
- `cleaning_prep_data.ipynb`: Jupyter notebook detailing the data cleaning and preparation process

## Data

The model is trained on the CDC Diabetes Health Indicators dataset, which has been preprocessed and balanced using SMOTE. The original dataset is not included in this repository due to size constraints.

## Model

The program uses a Gaussian Naive Bayes classifier, which has been optimized for recall. This means the model is tuned to minimize false negatives, ensuring that potential cases of diabetes are not missed.
