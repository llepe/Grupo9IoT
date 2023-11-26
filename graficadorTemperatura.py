import matplotlib.pyplot as plt

temperatura = {
    "x": [],
    "y": []
}

humedad = {
    "x": [],
    "y": []
}

f = open("datosTemperatura.log", "r")
datos = f.readlines()
for linea in datos:
    dato = linea.replace('\n', '').split(",")
    temperatura["x"].append(dato[0])
    temperatura["y"].append(dato[1])
    humedad["x"].append(dato[0])
    humedad["y"].append(dato[2])

plt.plot(temperatura["x"],temperatura["y"], color="r")
plt.scatter(humedad["x"],humedad["y"], marker = "*")
plt.show()