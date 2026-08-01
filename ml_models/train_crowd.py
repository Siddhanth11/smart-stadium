import joblib
import numpy as np
from sklearn.tree import DecisionTreeRegressor

X = np.array([
    [100],
    [200],
    [300],
    [400],
    [500]
])

y = np.array([
    120,
    260,
    330,
    470,
    600
])

model = DecisionTreeRegressor()

model.fit(X, y)

joblib.dump(model, "ml_models/crowd.pkl")

print("crowd.pkl created")