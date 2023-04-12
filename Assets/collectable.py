import pygame
class Collected(object):
    def __init__(self,img,val,i):
        self.img=img
        self.val=val #no. of easter eggs to be collected
        self.i=i #no. of collected easter eggs
        self.font=pygame.font.SysFont('comicsans',20,True,True) #SysFont('name of font',size of font,bold,italic)

    def draw(self,win,x,y):
        self.text=self.font.render('Collected    :'+str(self.i),2,(255,0,0)) #font.render('text to be displayed',1,(color))
        
        win.blit(self.text,(x+32,y))
        win.blit(self.img,(x+120,y))
