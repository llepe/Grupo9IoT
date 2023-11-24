from tkgpio import TkCircuit

# initialize the circuit inside the GUI

configuration = {
    "width": 300,
    "height": 200,
    "leds": [
        {"x": 50, "y": 40, "name": "LED 1", "pin": 14},
    ],
}

circuit = TkCircuit(configuration)
@circuit.run
def main ():
    
    # now just write the code you would use on a real Raspberry Pi
    
    from gpiozero import LED, Button
    from time import sleep
    
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
