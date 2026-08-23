import matplotlib.pyplot as plt
import numpy as np

from data import avg_petrol_price, avg_bus_fare
from main import fit

X = avg_petrol_price

m, b = fit()

x_train = np.linspace(X.min(), X.max(), 100)
y_train = (m * x_train) + b

plt.style.use("seaborn-v0_8-whitegrid")

fig, ax = plt.subplots(figsize=(8, 5), dpi=100)

ax.scatter(
    avg_petrol_price,
    avg_bus_fare,
    color="#1f77b4",
    alpha=0.8,
    edgecolors="white",
    linewidth=0.5,
    s=50,
    label="Petrol Price vs Bus Fare"
)

ax.set_xlabel("Average Petrol Price (₦)", fontsize=11)
ax.set_ylabel("Average Bus Fare (₦)", fontsize=11)
ax.set_title("Petrol Price vs Bus Fare", fontsize=13, fontweight="bold")
ax.legend()

ax.plot(
    x_train,
    y_train,
    color="gold",
    alpha=0.8,
    linewidth=3
)

plt.tight_layout()
plt.show()