import numpy as np

from data import avg_petrol_price, avg_bus_fare
from gradient_descent import gradient_descent
from cost import compute_cost

def fit():

    m_curr = b_curr = 0
    iterations = 200
    learning_rate = 0.0000001

    X = avg_petrol_price
    y = avg_bus_fare

    total = X.shape[0]

    for i in range(iterations):
        m_curr, b_curr = gradient_descent(m_curr, b_curr, X, y, total, learning_rate)
        cost = compute_cost(m_curr, b_curr, X, y, total)

        print(f"Linear Equation: y = {m_curr:.3f}x + {b_curr:.3f}. Cost: {cost:.2f}. Iteration {i}")
    return m_curr, b_curr


def predict(X):
    m, b = fit()

    y = (m * X) + b
    return y