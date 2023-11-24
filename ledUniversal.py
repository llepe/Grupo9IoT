from pathlib import Path
is_rpi = Path("/etc/rpi-issue").exists()

if not is_rpi:
    from tkgpio import TkCircuit

    # initialize the circuit inside the GUI

    configuration = {
        "width": 300,
        "height": 200,
        "leds": [
            {"x": 50, "y": 40, "name": "LED 1", "pin": 14},
            {"x": 100, "y": 40, "name": "LED 1", "pin": 15},
            {"x": 150, "y": 40, "name": "LED 1", "pin": 16},
        ],
    }

    circuit = TkCircuit(configuration)
#@circuit.run
def main ():
    
    # now just write the code you would use on a real Raspberry Pi
    
    from gpiozero import LED, Button
    from time import sleep
    
    leds = {
        "led1": LED(14),
        "led2": LED(15),
        "led3": LED(16)
    }

    for i in leds.keys():
        leds[i].blink()
        sleep(2)

    while True:
        sleep(1)

if is_rpi:
    main()
else:
    circuit.run(main)