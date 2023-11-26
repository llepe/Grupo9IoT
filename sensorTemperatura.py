import datetime
from random import randrange
from time import sleep


while True:
    f = open("datosTemperatura.log", "a")
    fecha = datetime.datetime.now()
    temperatura = randrange(30)
    humedad = randrange(100)

    dato = f"{fecha},{temperatura},{humedad}\n"
    print(dato)
    f.write(dato)
    f.close()
    sleep(1)


