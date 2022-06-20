
import ConnectWiFi
import ntptime
import time

ConnectWiFi.connect()

#if needed, overwrite default time server
ntptime.host = "1.europe.pool.ntp.org"

try:
  print("Horário antes da sincronizacao：%s" %str(time.localtime()))
  #confirme se a base wireless esta ativa
  ntptime.settime()
  print("Horário após sincronizacao：%s" %str(time.localtime()))
except:
  print("Error syncing time")

