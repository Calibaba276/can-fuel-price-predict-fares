import numpy as np

def gradient_descent(m_curr, b_curr, X, y, total, learning_rate):
    y_predicted = (m_curr * X) + b_curr
    
    md = (1 / total) * np.sum(X * (y_predicted - y))
    bd = (1 / total ) * np.sum(y_predicted - y)
    
    m_curr = m_curr - (learning_rate * md)
    b_curr = b_curr - (learning_rate * bd)

    return m_curr, b_curr