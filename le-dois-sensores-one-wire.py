
import onewire, ds18x20
from machine import Pin
import sys
global pinn
global value_sensor
import utime
import _thread

pin2 = Pin(4, Pin.OUT)

def sensor_read(gpio_port):
    try:
      temperature_sensor_pin = Pin(gpio_port)
      ds = ds18x20.DS18X20(onewire.OneWire(temperature_sensor_pin))
      temperature_sensor_list = ds.scan()    
      ds.convert_temp()
      sensor_value = ds.read_temp(temperature_sensor_list[0]) 
      print(sensor_value)
      #utime.sleep(5)
    except Exception as e:
      raise Exception("sensor error (pin specification or operation)")
      
      
      
#_thread.start_new_thread(thread_sensor_read, ())
while True:
  print("  ") 
  print("Sensor Porta 2")
  sensor_read(2)
  utime.sleep(3)
  print("Sensor Porta 4")
  sensor_read(4)
  utime.sleep(3)
  pin2.value(1)
  utime.sleep(5)
  pin2.value(0)
  utime.sleep(5)  
