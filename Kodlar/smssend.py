import serial
import RPi.GPIO as GPIO     
import os, time

GPIO.setmode(GPIO.BOARD)   

# Enable Serial Communication
port = serial.Serial("/dev/serial0", baudrate=115200, timeout=1)

# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key

port.write('AT'+'\r\n')#Sim modulu aktif mi kontrolu yapiyoruz.
rcv = port.read(10)
print rcv
time.sleep(1)

port.write('ATE0'+'\r\n')  #Echo modu kapatildi.
rcv = port.read(10)
print rcv
time.sleep(1)


port.write('AT+CSQ'+'\r\n') #Sinyal Seviyesi Sorgusu
rcv = port.read(10)
print rcv
time.sleep(1)


port.write('AT+CMGF=1'+'\r\n') #Sms icin text moduna aliyoruz.
rcv = port.read(10)
print rcv
time.sleep(1)

port.write('AT+CNMI=2,1,0,0,0'+'\r\n')  #Yeni mesaj olusturuyoruz.
rcv = port.read(10)
print rcv
time.sleep(1)

# Sending a message to a particular Number

port.write('AT+CMGS="+90555xxx1122"'+'\r\n') #Module telefon numarasini giriyoruz.
rcv = port.read(10)
print rcv
time.sleep(1)

port.write('Hello User'+'\r\n')  #Mesaj icerigini yaziyoruz.
rcv = port.read(10)
print rcv

port.write("\x1A") #SMS'i gonderiyoruz.
for i in range(10):
    rcv = port.read(10)
    print rcv

port.close()
