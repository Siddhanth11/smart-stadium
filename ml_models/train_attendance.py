import joblib
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([
    [10000],
    [20000],
    [30000],
    [40000],
    [50000]
])

y = np.array([
    12000,
    23000,
    35000,
    47000,
    60000
])

model = LinearRegression()

model.fit(X, y)

joblib.dump(model, "ml_models/attendance.pkl")

print("attendance.pkl created")