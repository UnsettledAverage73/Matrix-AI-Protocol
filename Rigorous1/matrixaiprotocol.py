# -*- coding: utf-8 -*-
"""MatrixAiprotocol.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Yp2xc4hKbz9HTgNmKrUiXMONShQS2I1j
"""

!pip install pandas scikit-learn

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# Load the synthetic dataset created earlier
df = pd.read_csv("/content/drive/MyDrive/synthetic_income_data.csv")

# Show first few rows
df.head()

# List of categorical columns
categorical_cols = ['education_level', 'employment_type', 'region']

# One-hot encode the categorical features
df_encoded = pd.get_dummies(df, columns=categorical_cols)

# View new DataFrame shape and features
print("✅ One-hot encoding done.")
df_encoded.head()

# Encode repayment_status (Yes/No) to 1/0
label_encoder = LabelEncoder()
df_encoded['repayment_status'] = label_encoder.fit_transform(df_encoded['repayment_status'])

# Check value counts
df_encoded['repayment_status'].value_counts()

# Separate features and target
X = df_encoded.drop('repayment_status', axis=1)
y = df_encoded['repayment_status']

print("✅ Features and target split.")

# Standardize (normalize) the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("✅ Features standardized.")

# Split into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42)

print("✅ Data split into training and test sets.")
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Initialize the model
logreg_model = LogisticRegression()

# Train the model
logreg_model.fit(X_train, y_train)

print("✅ Logistic Regression model trained.")

# Make predictions
y_pred = logreg_model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, y_pred)
print(f"🔍 Accuracy: {acc:.4f}")

# Confusion Matrix
print("\n📊 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Classification Report
print("\n📄 Classification Report:")
print(classification_report(y_test, y_pred))

# Get feature importance (coefficients)
feature_importance = pd.Series(logreg_model.coef_[0], index=X.columns)
feature_importance.sort_values(ascending=False).plot(kind='bar', title='Feature Importance (Logistic Regression)')

from sklearn.ensemble import RandomForestClassifier

# Initialize the model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

print("✅ Random Forest model trained.")

# Make predictions
rf_preds = rf_model.predict(X_test)

# Accuracy
rf_acc = accuracy_score(y_test, rf_preds)
print(f"🔍 Random Forest Accuracy: {rf_acc:.4f}")

# Confusion Matrix
print("\n📊 Confusion Matrix:")
print(confusion_matrix(y_test, rf_preds))

# Classification Report
print("\n📄 Classification Report:")
print(classification_report(y_test, rf_preds))

# Feature importance visualization
import matplotlib.pyplot as plt

feat_importances = pd.Series(rf_model.feature_importances_, index=X.columns)
feat_importances.nlargest(10).plot(kind='barh')
plt.title('Top 10 Feature Importances (Random Forest)')
plt.xlabel('Importance Score')
plt.show()

!pip install xgboost

import xgboost as xgb
from xgboost import XGBClassifier

# Initialize the model
xgb_model = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)

# Train the model
xgb_model.fit(X_train, y_train)

print("✅ XGBoost model trained.")

# Predictions
xgb_preds = xgb_model.predict(X_test)

# Accuracy
xgb_acc = accuracy_score(y_test, xgb_preds)
print(f"🔍 XGBoost Accuracy: {xgb_acc:.4f}")

# Confusion Matrix
print("\n📊 Confusion Matrix:")
print(confusion_matrix(y_test, xgb_preds))

# Classification Report
print("\n📄 Classification Report:")
print(classification_report(y_test, xgb_preds))

import matplotlib.pyplot as plt

# Plot top features
xgb.plot_importance(xgb_model, max_num_features=10)
plt.title("Top 10 Feature Importances (XGBoost)")
plt.show()

from sklearn.model_selection import GridSearchCV

# Define the parameter grid
param_grid = {
    'learning_rate': [0.01, 0.1],
    'max_depth': [3, 5, 7],
    'n_estimators': [100, 200],
    'subsample': [0.8, 1]
}

# Initialize the model
xgb_model = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)

# Grid Search
grid_search = GridSearchCV(estimator=xgb_model, param_grid=param_grid,
                           cv=3, scoring='accuracy', verbose=1, n_jobs=-1)

grid_search.fit(X_train, y_train)

# Best Parameters
print("🔧 Best Parameters:", grid_search.best_params_)

# Best Model
best_model = grid_search.best_estimator_

# Predict with tuned model
tuned_preds = best_model.predict(X_test)

# Accuracy
tuned_acc = accuracy_score(y_test, tuned_preds)
print(f"🎯 Tuned XGBoost Accuracy: {tuned_acc:.4f}")

# Confusion Matrix
print("\n📊 Confusion Matrix:")
print(confusion_matrix(y_test, tuned_preds))

# Classification Report
print("\n📄 Classification Report:")
print(classification_report(y_test, tuned_preds))

import joblib

# Save the best model
joblib.dump(best_model, 'xgboost_best_model.pkl')

print("✅ Model saved successfully as xgboost_best_model.pkl")

loaded_model = joblib.load('xgboost_best_model.pkl')

import pandas as pd

# Save test predictions
pred_df = pd.DataFrame({
    'Actual': y_test,
    'Predicted': tuned_preds
})

pred_df.to_csv('predictions.csv', index=False)

print("📁 Predictions saved as predictions.csv")

from google.colab import drive
drive.mount('/content/drive')

# Copy files to drive
!cp xgboost_best_model.pkl /content/drive/MyDrive/
!cp predictions.csv /content/drive/MyDrive/
!cp synthetic_income_data.csv /content/drive/MyDrive/