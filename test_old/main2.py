import time
import click
import mouse
import keyboard
import pyautogui
''' 674x581 conect wallet
    1254x544 metamask button
    1089x630 heroes button
    592x255 work all = 600x273
    732x206 button fechar
    243x120 button home
    142x12 click browser
    691x407 button mining

    => montar função para pegar a loc de x e y
    => montar função para logar no Metamask
    ==> Criar função de login caso desconectado
    comando para dar f5 ==>pyautogui.hotkey('ctrl','f5')

'''
#coordenadas tela notebook 1365 x 767

def click_home():
   
    print("voltando tela....")
    xloc = 243
    yloc = 124
    
    mouse.move(xloc, yloc, absolute=True, duration=0.1)
    mouse.click('left')
    time.sleep(5)

def click_browser():
    
    print("selecionando browser....")
    xloc = 142
    yloc = 12
    mouse.move(xloc, yloc, absolute=True, duration=0.1)
    mouse.click('left')
    time.sleep(5)

def click_mining():
    xloc = 691
    yloc = 407

    mouse.move(xloc, yloc, absolute=True, duration=0.1)
    mouse.click('left')
    print('iniciando a mineração....')  
    time.sleep(5)  

def click_heroes():
    xloc = 1089
    yloc = 630
    
    mouse.move(xloc,yloc,absolute=True, duration=0.1)
    mouse.click('left')
    print('selecionando os herois....')
    time.sleep(5)

def click_all_work():
    xloc = 600
    yloc = 273

    mouse.move(xloc,yloc,absolute=True, duration=0.1)
    mouse.click('left')
    print('colocando os herois para trabalhar....')
    time.sleep(5)

    mouse.move(731,225,absolute=True, duration=0.1)
    mouse.click('left')
    print('>>---> fechando tela....') 
    time.sleep(5)
'''comando para entrar no game 691 x 407

👆 Clicking in %d heroes
🔃 Refreshing Heroes Positions
🎉 Connect wallet button detected, logging in!
⚒️ Sending all heroes to work
💪 {} heroes sent to work
>>---> Home feature not enabled
'🗺️ New Map button clicked!

tentar usar essa função
        moveToWithRandomness(pos_click_x,pos_click_y,1)
        pyautogui.click()

'''

def main():

    while True:
        click_browser()
        click_home()
        click_heroes()
        click_all_work()
        click_mining()
        time.sleep(600)

if __name__== '__main__':
    main()
