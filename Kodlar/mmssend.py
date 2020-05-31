import serial
import RPi.GPIO as GPIO
import os, time
from PIL import Image


GPIO.setmode(GPIO.BOARD)
# Enable Serial Communication
port = serial.Serial("/dev/serial0", baudrate=115200, timeout=1)
# Sending a message to a particular Number

port.write('AT+CMMSEDIT=1'+'\r\n') #MMS mesaji duzenleme modu aciliyor.
rcv = port.read(20)
print "MMS Mesaji Olusturuldu"
time.sleep(1)

#----------------PIC---------------------
imgsize=os.stat("picture.jpg").st_size	#Fotograf boyutunu okuyoruz.
print "Resim Boyutu= "+str(imgsize)+" Byte"

port.write('AT+CMMSDOWN="PIC",'+str(imgsize)+',60000'+'\r\n')  #Fotograf yukleme yapacagimizi module bildiriyoruz.
rcv = port.read(20)
print "Resim Yukleniyor"+rcv
time.sleep(1)


with open("picture.jpg","rb") as f: #Fotoragi uart protokolu uzerinden byte byte basiyoruz.
	img=f.read(1)
	while img !="":
		port.write(img)
		if (img<0x10):
			print "--"
		else:
			print hex(ord(img))+" "
		img=f.read(1)
print "Resim Yuklemesi Tamamlandi"+rcv
time.sleep(1)
#----------------------------------------

#----------------TITLE------------------
titlesize=os.stat("title.txt").st_size #Konu basligi boyutunu okuyoruz.
print "Konu Basligi Boyutu= "+str(titlesize)+" Byte"

port.write('AT+CMMSDOWN="TITLE",'+str(titlesize)+',60000'+'\r\n')  #Konu basligi yukleme yapacagimizi module bildiriyoruz.
rcv = port.read(20)
print "Konu Basligi Ekleniyor"+rcv
time.sleep(1)


with open("title.txt","rb") as f: #Konu basligi uart protokolu uzerinden byte byte basiyoruz.
	title=f.read(1)
	while title !="":
		port.write(title)
		if (title<0x10):
			print "--"
		else:
			print hex(ord(title))+" "
		title=f.read(1)
print "Tamamlandi"+rcv
time.sleep(1)
#-----------------------------------------

#-----------------TEXT---------------------
textsize=os.stat("text.txt").st_size #Mesaj iceriginin boyutunu okuyoruz.
print "Mesaj Icerigi Boyutu= "+str(textsize)+" Byte"

port.write('AT+CMMSDOWN="TEXT",'+str(titlesize)+',60000'+'\r\n')  #Mesaj icerigini yukleme yapacagimizi module bildiriyoruz.
rcv = port.read(20)
print "Mesaj Icerigi Ekleniyor"+rcv
time.sleep(1)


with open("text.txt","rb") as f: #Mesaj icerigini uart protokolu uzerinden byte byte basiyoruz.
	text=f.read(1)
	while text !="":
		port.write(text)
		if (text<0x10):
			print "--"
		else:
			print hex(ord(text))+" "
		text=f.read(1)
print "Tamamlandi"+rcv
time.sleep(1)

#---------------------------------------------
port.write('AT+CMMSRECP="+90555xxx1122"'+'\r\n')  #Module telefon numarasini giriyoruz.
rcv = port.read(20)
print "Numara Eklendi"+rcv
time.sleep(1)

port.write('AT+CMMSSEND'+'\r\n')  #MMS mesajini gonderiyoruz.
rcv = port.read(20)
print "Mesaj Gonderiliyor"+rcv
time.sleep(1)

port.write('AT+CMMSEDIT=0'+'\r\n') #MMS mesaji duzenleme modu kapatiliyor.
rcv = port.read(20)
time.sleep(1)

port.close()
