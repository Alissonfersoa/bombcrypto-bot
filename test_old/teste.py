import time
import mouse
import keyboard
import pyautogui


def countdown(num_of_secs): #passar o parametro dentro da função para o tempo que quero o contador
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m,s)
        print(min_sec_format, end='\r')
        time.sleep(1)
        num_of_secs -=1    
    print('\nCountdown finished.')

def main():
    countdown(5)

main()