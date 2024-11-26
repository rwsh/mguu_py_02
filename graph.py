import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5,]
Y = [10, 5, -15, 20, 0]

plt.plot(X, Y, label = "Первая линия", color="red", linestyle="--", marker="o")
plt.grid(True)
plt.title("Мой первый график")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.legend()

plt.show()

Names = ['Roman', 'Elena', 'Alexander']
Values = [5, 7, 3]
plt.bar(Names, Values, color='blue')
plt.show()

Data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6]
plt.hist(Data, bins=6, color='green')
plt.show()

import random

X = []
Y = []

for n in range(1000):
    X.append(random.random())
    Y.append(random.random())

plt.scatter(X, Y, color='purple', s=5)
plt.savefig("graph.jpg")
plt.show()
