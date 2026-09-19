import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv("dataset.csv")

# Features
FEATURES = ["followers", "following", "posts", "bio_length", "profile_pic"]
X = data[FEATURES]
y = data["is_fake"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model & feature order
with open("fake_profile_model.pkl", "wb") as f:
    pickle.dump((model, FEATURES), f)

print("✅ Model trained and saved successfully!")
