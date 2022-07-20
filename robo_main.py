import time
from datetime import datetime
#import getch       
#import msvcrt      #rodar no visual studio    
from sys import platform
import ultra            #verificar distancia
import servo            #direcao do robo, bracos e mao
import move             #mover robo
import LED              #cores led
import farol            #acender e apagar farois
import OLED             #display
import mpu6050Test      #acelerometro, giroscopio e temperatura

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
temp_string = "Digite C para verificar a temperatura: "
acel_string = "Digite Z para verificar o acelerometro: "
giro_string = "Digite M para verificar o giroscopio: "
led = LED.LED()
screen = OLED.OLED_ctrl()
lista_funcionalidade = ["", "", "", "", ""]


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
    global lista_funcionalidade
    lista_funcionalidade.append("Andar frente")     #inclui "Andar frente" no final da lista
    atualizar_display()
    print("Ande para a frente!")
    distancia = ultra.checkdist()
    print("A distancia é: ", distancia)
    if distancia > 0.10:
        print("Distancia maior que 10!")
        farol.aciona_led(1, True)       #acende farol 1
        farol.aciona_led(2, True)       #acende farol 2
        led.colorWipe(0, 255, 0)            #verde
        speed_set = 60
        move.move(speed_set, 'forward', 'no', 0.8)
        time.sleep(0.3)
        move.motorStop()
        farol.aciona_led(1, False)      #apaga farol 1
        farol.aciona_led(2, False)      #apaga farol 2
        led.colorWipe(0, 0, 255)        #azul
   
def tras():
    global lista_funcionalidade
    lista_funcionalidade.append("Andar tras")       #inclui "Andar tras" no final da lista
    atualizar_display()
    print("Ande para tras!")
    farol.aciona_led(3, True)       #acende farol 3
    led.colorWipe(255, 0, 0)        #vermelho
    speed_set = 60
    move.move(speed_set, 'backward', 'no', 0.8)
    time.sleep(0.3)
    move.motorStop()
    farol.aciona_led(3, False)      #apaga farol 3
    led.colorWipe(0, 0, 255)       #azul
       
def esquerda():
    global lista_funcionalidade
    lista_funcionalidade.append("Virar esquerda")       #inclui "Virar esquerda" no final da lista
    atualizar_display()
    led.colorWipe(200, 162, 200)        #lilas
    farol.aciona_led(1, True)       #acende farol 1
    servo.direcaoleft(10)
    time.sleep(0.3)
    print("Vire para a esquerda!")
    farol.aciona_led(1, False)      #apaga farol 1
    led.colorWipe(0, 0, 255)        #azul

def direita():
    global lista_funcionalidade
    lista_funcionalidade.append("Virar direita")        #inclui "Virar direita" no final da lista
    atualizar_display()
    led.colorWipe(255, 165, 0)      #laranja
    farol.aciona_led(2, True)       #acende farol 2
    servo.direcaoright(10)
    time.sleep(0.3)
    print("Vire para a direita!")
    farol.aciona_led(2, False)      #apaga farol 2
    led.colorWipe(0, 0, 255)        #azul
        
def braco_direita():
    global lista_funcionalidade
    lista_funcionalidade.append("Braco direita")        #inclui "Braco direita" no final da lista
    atualizar_display()
    servo.armright(10)
    print("Vire o braco para a direita!")
        
def braco_esquerda():
    global lista_funcionalidade
    lista_funcionalidade.append("Braco esquerda")       #inclui "Braco esquerda" no final da lista
    atualizar_display()
    servo.armleft(10)
    print("Vire o braco para a esquerda!")

def braco_levanta():
    global lista_funcionalidade
    lista_funcionalidade.append("Braco levanta")        #inclui "Braco levanta" no final da lista
    atualizar_display()
    servo.armup(10)
    print("Levante o braco!")

def braco_abaixa():
    global lista_funcionalidade
    lista_funcionalidade.append("Braco abaixa")     #inclui "Braco abaixa" no final da lista
    atualizar_display()
    servo.armdown(10)
    print("Abaixe o braco!")

def mao_levanta():
    global lista_funcionalidade
    lista_funcionalidade.append("Mao levanta")      #inclui "Mao levanta" no final da lista
    atualizar_display()
    servo.handup(20)
    print("Levante a mao!")

def mao_abaixa():
    global lista_funcionalidade
    lista_funcionalidade.append("Mao abaixa")       #inclui "Mao abaixa" no final da lista
    atualizar_display()
    servo.handdown(10)
    print("Abaixe a mao!")

def mao_fecha():
    global lista_funcionalidade
    lista_funcionalidade.append("Mao fecha")        #inclui "Mao fecha" no final da lista
    atualizar_display()
    servo.grab(10)
    print("Feche a mao!")

def mao_abre():
    global lista_funcionalidade
    lista_funcionalidade.append("Mao abre")         #inclui "Mao abre" no final da lista
    atualizar_display()
    servo.loose(10)
    print("Abra a mao!")

def atualizar_display():
    global lista_funcionalidade
    tamanho = len(lista_funcionalidade)
    if tamanho > 5:
        diferenca = tamanho - 5
        while diferenca > 0:
            lista_funcionalidade.pop(0)     #elimina o primeiro elemento da lista
            diferenca -= 1
    for linha in range(5):
        screen.screen_show(linha + 2, lista_funcionalidade[linha])
    screen.run()
    
        
def funcionalidade():
    executando = True
    screen.screen_show(1, "Historico")      #mostra no display, na linha 1: "Historico"
    print(direcao_string)
    print(braco_string)
    print(temp_string)
    print(acel_string)
    print(giro_string)
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
        elif tecla == "C" or tecla == "c":
            print("Temperatura")
            mpu6050Test.temperatura()           #mostra a temperatura
        elif tecla == "Z" or tecla == "z":
            print("Acelerometro")
            mpu6050Test.acelerometro()          #mostra o acelerometro
        elif tecla == "M" or tecla == "m":
            print("Giroscopio")
            mpu6050Test.giroscopio()            #mostra o giroscopio
        elif tecla == "X" or tecla == "x":
            print("Finalizar programa!")
            executando = False
        else:
            print("Funcionalidade inexistente!", tecla)
            executando = False


if __name__ == '__main__':
    inicio()
    
    try:
        screen.screen_show(1, "Iniciando")      #mostra no display, na linha 1: "Iniciando"
        screen.run()
        servo.servo_init()
        move.setup()
        farol.setup_raspberry()
        farol.apaga_todos_leds()
        funcionalidade()
        screen.screen_show(6, "Finalizando")        #mostra no display, na linha 6: "Finalizando"
        screen.run()
        move.destroy()
        led.colorWipe(0, 0, 0)      #lights out
        farol.apaga_todos_leds()        #apaga todos os farois
    except:
        print("Emergencia!")
   
    fim()
   

