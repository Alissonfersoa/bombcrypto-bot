#Import Libs
import time
import click
import mouse
import keyboard
import pyautogui


def inicialize():
    
    print('''
    =========================================================================
    ||  Configure according to screen size:                                ||
    ||  Configurar de acordo com o tamanho da tela:                        ||
    ||                                                                     ||
    ||    => Remember to configure the positions in the functions          ||
    ||    => Lembre-se de configurar as posições nas funções               ||
    ||    variable [position xloc] and [position yloc]                     ||
    ||                                                                     ||
    ||  Make sure the browser is open before running the script            ||
    ||  Verfique se o navegador está aberto antes de executar o script     ||
    ||                                                                     ||
    ||  Screen size     ==  1365x767                                       ||
    ||  Tamanho da tela ==  1365x767                                       || 
    ||                                                                     ||
    ||    ===> Press CTRL + C to kill the bot.                             ||
    ||    ===> Pressione CTRL + C para encerrar o bot.                     ||
    =========================================================================
    
>>-----> Initializing Application <-----<<
''')

def selectBrowser():

    xloc = 142
    yloc = 12
    
    print(">>-----> Selecting browser....")
    print(">>-----> Leave the browser open !!!")  
    
    # mouse.move(xloc, yloc, absolute=True, duration=0.1)
    # mouse.click('left')
    time.sleep(5)

def clickHome():
    
    xloc = 243
    yloc = 124

    # mouse.move(xloc, yloc, absolute=True, duration=0.1)
    # mouse.click('left')
    time.sleep(5)

    print("<-----<< Returning to home....")
        
def login():
    # Developing function
    pass

def selectHeroes():
    
    xloc = 1089
    yloc = 630
    
    print(">>-----> Selecting heroes....")  
    
    # mouse.move(xloc, yloc, absolute=True, duration=0.1)
    # mouse.click('left')
    time.sleep(5)

def loadAllHeroes():
        
    xloc = 600
    yloc = 273
    
    print(">>-----> Putting the heroes to work....")  
    
    # mouse.move(xloc, yloc, absolute=True, duration=0.1)
    # mouse.click('left')
    # time.sleep(5)
    # #comando para fechar a tela
    # mouse.move(731,225,absolute=True, duration=0.1)
    # mouse.click('left')
    print('>>-----> Close screen....') 
    time.sleep(5)

def goTogame():
            
    xloc = 691
    yloc = 407
    
    print(">>-----> Starting mining!....")  
    
    # mouse.move(xloc, yloc, absolute=True, duration=0.1)
    # mouse.click('left')
    time.sleep(5)

def countDown(num_of_secs):
    
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m,s)
        print(">>-----> Waiting time : " + min_sec_format, end='\r')
        time.sleep(1)
        num_of_secs -=1
    print("\n<-----<< Restarting routine!!\n")

def closeApp():
    
    print(">>-----> ## Closing Application ## <-----<<")
    exit()

def main():
    
    inicialize()

    try:
        while True: 
            selectBrowser()
            clickHome()
            selectHeroes()
            loadAllHeroes()
            goTogame()
            countDown(5) #real 600
    except:
        print(">>-----> Command CTRL + C detected")
        print(">>-----> ## Closing Application ## <-----<<")
        exit()

if __name__=='__main__':
    main()