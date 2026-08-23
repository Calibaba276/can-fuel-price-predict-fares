import numpy as np

def compute_cost(m_curr, b_curr, X, y, total):
    y_predicted = (m_curr * X) + b_curr

    cost = (1 / (2 * total)) * np.sum((y_predicted - y) ** 2)
    return cost