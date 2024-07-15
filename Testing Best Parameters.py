import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, make_scorer
from sklearn.pipeline import Pipeline
from tabulate import tabulate

# Load the dataset
df = pd.read_csv('diabetes_balanced.csv')

# Separate features and target
X = df.drop('Diabetes_01', axis=1)
y = df['Diabetes_01']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline with StandardScaler and GaussianNB
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('nb', GaussianNB())
])

# Define the parameter grid
param_grid = {
    'nb__var_smoothing': np.logspace(-10, -8, 30),
    'nb__priors': [None, [0.5, 0.5], [0.4, 0.6], [0.6, 0.4]]
}

# Create custom scorers
scorers = {
    'accuracy': make_scorer(accuracy_score),
    'precision': make_scorer(precision_score),
    'recall': make_scorer(recall_score),
    'f1': make_scorer(f1_score)
}

# Set up GridSearchCV
grid_search = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring=scorers,
    refit='recall',  # Optimize for recall
    n_jobs=-1,  # Use all available cores
    verbose=1
)

# Fit the grid search
grid_search.fit(X_train, y_train)

# Get the best model
best_model = grid_search.best_estimator_

# Make predictions with the best model
y_pred = best_model.predict(X_test)

# Calculate scores
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Create a table of scores
scores_table = [
    ["Metric", "Score"],
    ["Accuracy", f"{accuracy:.4f}"],
    ["Precision", f"{precision:.4f}"],
    ["Recall", f"{recall:.4f}"],
    ["F1 Score", f"{f1:.4f}"]
]

# Print the best parameters and scores
print("Best Parameters:")
print(grid_search.best_params_)
print("\nBest Recall Score:", grid_search.best_score_)

print("\nNaive Bayes Classifier Scores (Best Model):")
print(tabulate(scores_table, headers="firstrow", tablefmt="grid"))

# Print feature importances
feature_importance = np.log(best_model.named_steps['nb'].var_).reshape(-1)
feature_names = X.columns
feature_importance_table = list(zip(feature_names, feature_importance))
feature_importance_table.sort(key=lambda x: x[1], reverse=True)

print("\nFeature Importances:")
print(tabulate(feature_importance_table[:10], headers=["Feature", "Importance"], tablefmt="grid"))

# Print cross-validation results
cv_results = grid_search.cv_results_
cv_table = []
for mean_score, params in zip(cv_results["mean_test_recall"], cv_results["params"]):
    cv_table.append([f"{mean_score:.4f}", params])

print("\nTop 5 Cross-validation Results (sorted by recall):")
cv_table.sort(key=lambda x: float(x[0]), reverse=True)
print(tabulate(cv_table[:5], headers=["Mean Recall", "Parameters"], tablefmt="grid"))