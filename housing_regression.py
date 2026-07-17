
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

rng = np.random.default_rng(42)
n = 5000

MedInc = rng.gamma(shape=5.0, scale=0.75, size=n).clip(0.5, 15)
HouseAge = rng.uniform(1, 52, size=n)
AveRooms = rng.normal(5.4, 1.1, size=n).clip(2, 12)
AveBedrms = (AveRooms * rng.normal(0.19, 0.03, size=n)).clip(0.5, 3)
Population = rng.gamma(shape=4.0, scale=350, size=n).clip(50, 15000)

noise = rng.normal(0, 45_000, size=n)
MedHouseVal_USD = (
    45_000
    + MedInc * 38_000
    + AveRooms * 9_000
    - AveBedrms * 12_000
    - HouseAge * 700
    - Population * 3
    + noise
).clip(30_000, 800_000)

df = pd.DataFrame({
    "MedInc": MedInc,
    "AveRooms": AveRooms,
    "AveBedrms": AveBedrms,
    "HouseAge": HouseAge,
    "Population": Population,
    "MedHouseVal_USD": MedHouseVal_USD,
})

features = ["MedInc", "AveRooms", "AveBedrms", "HouseAge", "Population"]
X = df[features]
y = df["MedHouseVal_USD"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("=== Model Performance ===")
print(f"RMSE: ${rmse:,.2f}")
print(f"R^2 score: {r2:.4f}")
print()
print("=== Feature Coefficients ===")
for f, c in zip(features, model.coef_):
    print(f"{f:12s}: {c:,.2f}")
print(f"Intercept   : {model.intercept_:,.2f}")

plt.figure(figsize=(7, 7))
plt.scatter(y_test, y_pred, alpha=0.3, s=15, color="#2563eb")
lims = [0, max(y_test.max(), y_pred.max())]
plt.plot(lims, lims, color="red", linestyle="--", linewidth=2, label="Perfect prediction")
plt.xlabel("Actual House Value ($)")
plt.ylabel("Predicted House Value ($)")
plt.title(f"Predicted vs. Actual House Prices\nR² = {r2:.3f}   RMSE = ${rmse:,.0f}")
plt.legend()
plt.tight_layout()
plt.savefig("predicted_vs_actual.png", dpi=150)
print("\nSaved plot to predicted_vs_actual.png")
