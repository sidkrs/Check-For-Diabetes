import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import Questions

# Load the dataset
df = pd.read_csv('diabetes_balanced.csv')

# Separate features and target
X = df.drop('Diabetes_01', axis=1)
y = df['Diabetes_01']

# Store feature names
feature_names = X.columns.tolist()

# Create a pipeline with StandardScaler and GaussianNB
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('nb', GaussianNB(priors=[0.4, 0.6], var_smoothing=1e-10))
])

# Train the model on the entire dataset
pipeline.fit(X, y)

# Function to predict diabetes for new inputs
def predict_diabetes(inputs):
    # Ensure inputs is a 2D array
    if len(np.array(inputs).shape) == 1:
        inputs = [inputs]
    
    # Convert inputs to a DataFrame with correct feature names
    inputs_df = pd.DataFrame(inputs, columns=feature_names)
    
    # Make prediction
    predictions = pipeline.predict(inputs_df)
    probabilities = pipeline.predict_proba(inputs_df)
    
    results = []
    for pred, prob in zip(predictions, probabilities):
        results.append({
            'prediction': int(pred),
            'probability': f"{prob[1]:.4f}"
        })
    
    return results

# Make predictions
predictions = predict_diabetes(Questions.main())

# Print results
print("Predictions:")
for i, pred in enumerate(predictions):
    print(f"Input {i+1}: Prediction = {pred['prediction']} (Probability of diabetes: {pred['probability']})")

if predictions[0]['prediction'] == 1:
    print("You have diabetes or are pre-diabetic. Please consult a doctor.")
else:
    print("You do not have diabetes. Please maintain a healthy lifestyle.")

# Uncomment the following lines if you want to print feature names for reference
# print("\nFeature names for reference:")
# print(", ".join(feature_names))