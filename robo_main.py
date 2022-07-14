from dis import dis
import time
from datetime import datetime
#import getch       
#import msvcrt      #rodar no visual studio    
from sys import platform
import ultra

plat_win = False
if platform == "linux" or platform == "linux2":
    # linux
    plat_win = False
elif platform == "win32":
    # Windows...
    plat_win = True
else:
    print("Plataforma desconhecida: ", platform)

if plat_win:
    import msvcrt
else:
    import getch


#Variaveis
direcao_string = "Digite uma tecla para mover o robo (A, W, S, D): "
braco_string = "Digite uma tecla para utilizar o braco (T, G, Y, H, U, J, I, K): "

def inicio():
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("\n Iniciando ROBO:", dt_string, "\n")
    time.sleep(0.5)

def fim():
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("\n Finalizando ROBO:", dt_string, "\n")
    time.sleep(0.5)


def frente():
    print("Ande para a frente!")
    distancia = ultra.checkdist()
    print("A distancia é: ", distancia)
    if distancia > 0.10:
        print("Distancia maior que 10!")
        
def tras():
    print("Ande para tras!")
       
def esquerda():
    print("Vire para a esquerda!")

def direita():
    print("Vire para a direita!")
        
def braco_direita():
    print("Vire o braco para a direita!")
        
def braco_esquerda():
    print("Vire o braco para a esquerda!")

def braco_levanta():
    print("Levante o braco!")

def braco_abaixa():
    print("Abaixe o braco!")

def mao_levanta():
    print("Levante a mao!")

def mao_abaixa():
    print("Abaixe a mao!")

def mao_fecha():
    print("Feche a mao!")

def mao_abre():
    print("Abra a mao!")


def funcionalidade():
    executando = True
    print(direcao_string)
    print(braco_string)
    while executando:
        if plat_win:
            tecla = msvcrt.getwch()     #rodar no visual studio
        else:
            tecla = getch.getch()     
        if tecla == "W" or tecla == "w":
            frente()
        elif tecla == "S" or tecla == "s":
            tras()
        elif tecla == "A" or tecla == "a":
            esquerda()
        elif tecla == "D" or tecla == "d":
            direita()
        elif tecla == "T" or tecla == "t":
            braco_direita()
        elif tecla == "G" or tecla == "g":
            braco_esquerda()
        elif tecla == "Y" or tecla == "y":
            braco_levanta()
        elif tecla == "H" or tecla == "h":
            braco_abaixa()
        elif tecla == "U" or tecla == "u":
            mao_levanta()
        elif tecla == "J" or tecla == "j":
            mao_abaixa()
        elif tecla == "I" or tecla == "i":
            mao_fecha()
        elif tecla == "K" or tecla == "k":
            mao_abre()        
        elif tecla == "X" or tecla == "x":
            print("Finalizar programa!")
            executando = False
        else:
            print("Funcionalidade inexistente!", tecla)
            executando = False


if __name__ == '__main__':
    inicio()
    funcionalidade()
    fim()
