import pygame
class EasterEggs():
    def __init__(self,x,y,width,height,egg):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.egg=egg

        self.rect=self.egg.get_rect()
        self.rect.x=x
        self.rect.y=y
        
        self.visible=True

    def draw(self,win):
        if self.visible==True:
            win.blit(self.egg,(self.x,self.y))
            # pygame.draw.rect(win,(255,255,255),self.rect,2)