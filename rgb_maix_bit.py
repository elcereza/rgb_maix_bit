import time                                                            # Importa biblioteca de tempo
from Maix import GPIO                                                  # Importa pinos do Maix
from fpioa_manager import fm                                           # Importa biblioteca de registradores
from board import board_info                                           # Importa as informações da placa 
 
fm.register(board_info.LED_R, fm.fpioa.GPIO0, force=True)              # Registra pino do LED_R como função IO 
fm.register(board_info.LED_G, fm.fpioa.GPIOHS0, force=True)            # Registra pino do LED_G como função IO
fm.register(board_info.LED_B, fm.fpioa.GPIO2, force=True)              # Registra pino do LED_B como função IO
 
led_r = GPIO(GPIO.GPIO0, GPIO.OUT)                                     # Define led_r como uma saída da porta GPIO0
led_g = GPIO(GPIO.GPIOHS0, GPIO.OUT)                                   # Define led_g como uma saída da porta GPIHS0
led_b = GPIO(GPIO.GPIO2, GPIO.OUT)                                     # Define led_b como uma saída da porta GPIO2
 
while(True):                                                           # Inicia Loop infinito
    led_r.value(0)                                                     # Liga a cor vermelha
    time.sleep_ms(300)                                                 # Delay de 300ms
    led_r.value(1)                                                     # Desliga cor vermelha
    led_g.value(0)                                                     # Liga cor verde
    time.sleep_ms(300)                                                 
    led_g.value(1)                                                     
    led_b.value(0)                                                     # Liga cor azul
    time.sleep_ms(300)
  
    led_r.value(0)
    led_g.value(0)
    led_b.value(0)
    time.sleep_ms(1000)
     
    led_r.value(1)
    led_g.value(1)
    led_b.value(1)
 
fm.unregister(board_info.LED_R)                                        # Limpa registro do pino LED_R
fm.unregister(board_info.LED_G)                                        # Limpa registro do pino LED_G
fm.unregister(board_info.LED_B)                                        # Limpa registro do pino LED_B
