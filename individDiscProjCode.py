from gpiozero import Button, LED
from random import choice, uniform
from time import sleep

# Setting up Buttons
redBt = Button(27)
greenBt = Button(26)
blueBt = Button(22)
yellowBt = Button(21)

# Setting up LEDS
redLed = LED(5)
greenLed = LED(6)
blueLed = LED(17)
yellowLed = LED(23)
ledList = [redLed, greenLed, blueLed, yellowLed]
colors = ledList

# Defining a function to turn off all the LEDs (for troubleshooting)
def off():
    for led in ledList:
        led.off()

# Defining a function to blink the LEDs as an opening sequence       
def introBlink():
    redLed.on()
    greenLed.on()
    yellowLed.on()
    blueLed.on()
    sleep(0.2)
    redLed.off()
    greenLed.off()
    blueLed.off()
    yellowLed.off()
    sleep(0.2)

# Calling the opening sequence    
for i in range(5):
    introBlink()

# Setting up the gameplay
while True:
    rnd_colors = []
    player = []
# The game begins when the player presses the green button
    if greenBt.value == True:
        delay = round(uniform(0.3,0.7),1)
        print(delay)
        for i in range(4):
            rnd_colors.append(choice(colors))
            print(rnd_colors)
        for color in rnd_colors:
            print(color)
            color.on()
            sleep(delay)
            color.off()
            sleep(delay)
# Lets try and match the sequence of lights shown
        while len(player) <4:
            sleep(0.2)
            if redBt.value == True:
                player.append(redLed)
                print(player)
                redLed.on()
                sleep(0.1)
                redLed.off()
            elif greenBt.value == True:
                player.append(greenLed)
                print(player)
                greenLed.on()
                sleep(0.1)
                greenLed.off()
            elif blueBt.value == True:
                player.append(blueLed)
                print(player)
                blueLed.on()
                sleep(0.1)
                blueLed.off()
            elif yellowBt.value == True:
                player.append(yellowLed)
                print(player)
                yellowLed.on()
                sleep(0.1)
                yellowLed.off()
# If the player is correct, the green light flashes
        if player == rnd_colors:
            for i in range(10):
                greenLed.on()
                sleep(0.2)
                greenLed.off()
                sleep(0.1)
# If the player is incorrect, the red light flashes
        else:
            for i in range(10):
                redLed.on()
                sleep(0.2)
                redLed.off()
                sleep(0.1)
                
# The player can press the green button to play another round
