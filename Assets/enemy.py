import pygame
class Enemy(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.visible=True
        self.name="Olive"

        self.char=pygame.image.load(r'Assets\sprites\Enemy\hi\hi.png').convert_alpha()
        self.rect=self.char.get_rect()
        self.rect.x=x
        self.rect.y=y

    def homeMovement(self,win):
        if self.visible:
            win.blit(self.char,(self.x,self.y))

    def homeDialogue(self,player,win):
        #check for collision or interaction
        pygame.draw.rect(win,(255,255,255),self.rect,2)
        if self.rect.colliderect(pygame.Rect(player.x, player.y, player.width, player.height)):
                print("collided with olive")
            