import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

X = np.array([
    [1000, 1],
    [2000, 1],
    [3000, 2],
    [4000, 2],
    [5000, 3]
])

y = np.array([
    1,
    2,
    2,
    3,
    3
])

model = RandomForestClassifier()

model.fit(X, y)

joblib.dump(model, "ml_models/seat_model.pkl")

print("seat_model.pkl created")