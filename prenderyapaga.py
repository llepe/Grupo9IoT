from gpiozero import LED

led = LED(14)

while True:
    orden = input("Que quieres que haga?\n\r")

    if (orden == "prendete"):
        led.on()
        print ("Prendido\n\r")
    elif (orden == "apagate"):
        led.off()
        print ("Apagado\n\r")
    elif (orden == "parpadea"):
        led.blink()
        print ("Parpadeando\n\r")
    elif (orden == "salte"):
        led.off()
        print ("Adios\n\r")
        break;
    else:
        print ("Orden invalida\n\r")
