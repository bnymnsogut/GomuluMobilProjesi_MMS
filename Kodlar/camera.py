#!/usr/bin/python
import os
import pygame, sys

from pygame.locals import *
import pygame.camera
def TakePicture() :
  width = 480
  height = 320

  #Pygame init yapiliyor  
  pygame.init()
  pygame.camera.init()
  cam = pygame.camera.Camera("/dev/video0",(width,height))
  cam.start()

  #Windows kamera ekrani aciliyor
  windowSurfaceObj = pygame.display.set_mode((width,height),1,16)
  pygame.display.set_caption('Camera')

  #Fotograf cekme fonksiyonu
  image = cam.get_image()
  cam.stop()

  #Fotograf goruntuleme
  catSurfaceObj = image
  windowSurfaceObj.blit(catSurfaceObj,(0,0))
  pygame.display.update()

  #Fotograf kaydetme
  pygame.image.save(windowSurfaceObj,'/home/pi/Project/picture.jpg')
   
TakePicture()
