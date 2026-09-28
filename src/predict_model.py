import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv("data/social_media_data.csv")

# Create engagement rate
df["engagement_rate"] = (
    (df["likes"] + df["comments"] + df["shares"] + df["saves"])
    / df["views"]
) * 100

# Convert categorical columns into numbers
df_encoded = pd.get_dummies(
    df,
    columns=["platform", "content_type", "topic"],
    drop_first=True
)

# Features
X = df_encoded.drop(
    columns=["engagement_rate", "post_id", "post_date"]
)

# Target
y = df_encoded["engagement_rate"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Model trained successfully!")
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))
# Save predictions
results = X_test.copy()
results["actual_engagement"] = y_test.values
results["predicted_engagement"] = predictions

results.to_csv(
    "data/predictions.csv",
    index=False
)

print("Predictions saved to data/predictions.csv")