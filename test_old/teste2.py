
import time
import mouse
import keyboard
import pyautogui

# keyboard.is_pressed()

def identifica():
    while True:
        if keyboard.is_pressed("q"):
            stopApp()
            break

def stopApp():

    print("Closing Application....")
    exit()

def main():
    identifica()

main()