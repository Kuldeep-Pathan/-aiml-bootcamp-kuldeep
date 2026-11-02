# California Housing: Regression Model Comparison

## Overview
This project predicts California house values using the MedHouseVal target.

## Models
- Baseline: predicts the mean target value.
- Linear Regression: learns linear relationships.
- Ridge: applies L2 regularisation.
- Lasso: applies L1 regularisation and can set coefficients to zero.

## How to Run
1. Install pandas, matplotlib, and scikit-learn.
2. Place california_housing.csv in the project folder.
3. Run the notebook from top to bottom.

## Results
model_comparison.csv contains the mean 5-fold cross-validation R² scores.
The final test R² is reported for Lasso, evaluated once on the held-out test set.
A higher R² generally indicates better predictive performance.

coefficients.png visualises standardised Lasso coefficients.
Positive and negative coefficients indicate associations with predicted values;
they do not prove causation.
