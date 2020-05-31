import serial
import RPi.GPIO as GPIO
import os, time
from PIL import Image


GPIO.setmode(GPIO.BOARD)
# Enable Serial Communication
port = serial.Serial("/dev/serial0", baudrate=115200, timeout=1)

# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key

#Test Module
port.write('AT'+'\r\n') #Sim modulu aktif mi kontrolu yapiyoruz.
rcv = port.read(10)
print "AT"+rcv
time.sleep(1)
port.write('ATE0'+'\r\n') #Echo modu kapatildi.
rcv = port.read(10)
print "ATE0"+rcv
time.sleep(1)

port.write('AT+CSQ'+'\r\n') #Sinyal Seviyesi Sorgusu
rcv = port.read(20)
print "Sinyal Seviyesi"+rcv
time.sleep(2)


port.write('AT+CMMSINIT'+'\r\n')  #MMS modu aktif ediliyor
rcv = port.read(20)
print "MMS Init\r\nLoading"
time.sleep(2)

port.write('AT+CMMSCURL="mms.turktelekom.com.tr/servlets/mms"'+'\r\n')  #Operatorumuze ait mms url sini giriyoruz
rcv = port.read(20)
print "---"
time.sleep(2)

port.write('AT+CMMSCID=1'+'\r\n')  #Sim tasiyici aktif ediliyor
rcv = port.read(20)
print "---"
time.sleep(2)

port.write('AT+CMMSPROTO="213.161.151.201",8080'+'\r\n')  #Operatorumuze ait ip ve port bilgilerini giriyoruz
rcv = port.read(20)
print "---"
time.sleep(2)


#Operator ile alakali datasheet de gecen asagidaki adimlar uygulaniyor
port.write('AT+SAPBR=3,1,"Contype","GPRS"'+'\r\n') 
rcv = port.read(20)
print "---"
time.sleep(1)
port.write('AT+SAPBR=3,1,"APN","mms"'+'\r\n')  
rcv = port.read(20)
print "---"
time.sleep(1)
port.write('AT+SAPBR=1,1'+'\r\n')  
rcv = port.read(20)
print "---\r\n"
time.sleep(1)

print "Tamamlandi"

port.close()
