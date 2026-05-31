import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

from xgboost import XGBClassifier


# Load Dataset
df = pd.read_csv("dataset/phishing.csv")

print(df.head())

# Features
X = df.drop("label", axis=1)

# Labels
y = df["label"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# XGBoost Model
model = XGBClassifier(
    n_estimators=500,
    max_depth=10,
    learning_rate=0.05,
    subsample=0.9,
    colsample_bytree=0.9,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

# Classification Report
print("\nClassification Report:\n")

print(classification_report(y_test, y_pred))

# Confusion Matrix
print("\nConfusion Matrix:\n")

print(confusion_matrix(y_test, y_pred))

# Save Model
joblib.dump(model, "model.pkl")

joblib.dump(scaler, "scaler.pkl")

print("\nModel Saved Successfully")