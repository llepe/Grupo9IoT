servidor = ""
baseDeDatos = ""
usuario = ""

f = open("configuracion.txt", "r")
lineas = f.readlines()
for linea in lineas:
    datos = linea.split('=')
    if (datos[0] == "servidor"):
        servidor = datos[1]
    elif (datos[0] == "baseDeDatos"):
        baseDeDatos = datos[1]
    elif (datos[0] == "usuario"):
        usuario = datos[1]
f.close()

print(f"Servidor: {servidor}")
print(f"baseDeDatos: {baseDeDatos}")
print(f"usuario: {usuario}")
