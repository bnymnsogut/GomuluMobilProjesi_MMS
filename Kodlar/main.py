import RPi.GPIO as GPIO
import time
import os
import camera

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 23
ECHO = 24

print "HC-SR04 mesafe sensoru"
camera.TakePicture()
os.system('python mmsconf.py') #MMS init islemi yapiliyor.

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
flagcontrol=0
while True:
	GPIO.output(TRIG, False)
	print "Olculuyor..."
	time.sleep(2)

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
		pulse_start = time.time()

	while GPIO.input(ECHO)==1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150
	distance = round(distance, 2)

	if distance > 2 and distance <= 30:

		print "Kapi Acildi. Mesafe:",distance - 0.5,"cm"
		if flagcontrol==1:
			flagcontrol=0
			print "Resim gonderiliyor..."
			camera.TakePicture() #Fotograf cekiliyor
			os.system('python mmssend.py') #MMS mesaji gonderiliyor.
	elif distance > 30:
		flagcontrol=1    
		print "Ortam sakin Mesafe",distance-0.5,"cm"
	else:
		flagcontrol=1
		print "Menzil asildi"
