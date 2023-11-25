#f = open("configuracion3.txt", "a")
#
#for i in range(10,15):
#    f.write(f'Agregado linea {i}\n')
#
#f.close()


f = open("configuracion3.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

f = open("configuracion3.txt", "r")
contenido = f.read()
print(contenido)
f.close()

f = open("configuracion3.txt", "r")
lineas = f.readlines()
for linea in lineas:
    print(linea)
f.close()


