
import machine
import time
import utime

pin2 = machine.Pin(2, machine.Pin.OUT)

def pisca_uma_vez(duracao):
   apagado=int(duracao/1)
   pin2.value(1)
   utime.sleep_ms(duracao)
   pin2.value(0)
   utime.sleep_ms(apagado)
   
while(True):
  pisca_uma_vez(200)

