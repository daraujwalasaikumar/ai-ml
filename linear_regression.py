import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('studytime_scores.csv')

# dataset contains num of hours students studied for an exam (<9000 hrs i.e < 1 year)
# and their score (<300)


data['StudyTime_Hours_Norm'] = data['StudyTime_Hours'] / data['StudyTime_Hours'].max()


def loss_function(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].StudyTime_Hours_Norm
        y = points.iloc[i].ExamScore
        total_error += (y - (m*x + b))**2
    return total_error / float(len(points))

def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0
    n = len(points)
    for i in range(n):
        x = points.iloc[i].StudyTime_Hours_Norm
        y = points.iloc[i].ExamScore
        m_gradient += -(2/n) * x * (y - (m_now*x + b_now))
        b_gradient += -(2/n) * (y - (m_now*x + b_now))
    m = m_now - L * m_gradient
    b = b_now - L * b_gradient
    return m, b


m = 0
b = 0
L = 0.01 
epochs = 2000

loss_history = []

for i in range(epochs+1):
    m, b = gradient_descent(m, b, data, L)
    current_loss = loss_function(m, b, data)
    loss_history.append(current_loss)
    if i % 200 == 0:
        print(f"Epoch {i}: m={m:.6f}, b={b:.3f}, loss={loss_function(m,b,data):.3f}")

print(f"\nFinal model: y = {m:.6f}x + {b:.3f}")



plt.figure(figsize=(12,5))


plt.subplot(1, 2, 1)
plt.scatter(data.StudyTime_Hours_Norm, data.ExamScore, color="black", label="Data points")
x_range = np.linspace(data.StudyTime_Hours_Norm.min(), data.StudyTime_Hours_Norm.max(), 100)
plt.plot(x_range, m*x_range + b, color="red", label="Regression line")
plt.xlabel("Normalized Study Time")
plt.ylabel("Exam Score")
plt.title("Linear Regression Fit")
plt.legend()


plt.subplot(1, 2, 2)
plt.plot(range(epochs+1), loss_history, color='blue')
plt.xlabel("Epochs")
plt.ylabel("Loss (MSE)")
plt.title("Loss vs Epochs")

plt.tight_layout()
plt.show()