import matplotlib.pyplot as plt

data = {
    "x": [1,2,3,4,5,6,7,8,9],
    "y": [1,4,9,16,25,36,49,64,81]
}

data2 = {
    "x": [i for i in range(1,10)],
    "y": [i * 10 for i in range(1,10)]
}

plt.plot(data["x"],data["y"], color="r")

plt.scatter(data2["x"],data2["y"], marker = "*")

plt.show()

