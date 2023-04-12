import pygame
class Teleport():
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.isDraw=False
        self.walkCount=0
        
        self.swirl=[pygame.image.load(r'Assets\sprites\teleport\swirl\Layer 1_sprite_1.png').convert_alpha(),
                    pygame.image.load(r'Assets\sprites\teleport\swirl\Layer 1_sprite_2.png').convert_alpha(),
                    pygame.image.load(r'Assets\sprites\teleport\swirl\Layer 1_sprite_3.png').convert_alpha(),
                    pygame.image.load(r'Assets\sprites\teleport\swirl\Layer 1_sprite_4.png').convert_alpha()]
        
        self.rect=self.swirl[0].get_rect()
        self.rect.x=x
        self.rect.y=y
        self.rect.width=self.rect.width//2
        self.rect.height=self.rect.height//2

    def draw(self,win):
        if self.isDraw:
            if self.walkCount>=4:
                self.walkCount=0

            win.blit(self.swirl[self.walkCount],(self.x,self.y))
            self.walkCount+=1

    def isCollide(self,player):
        if self.rect.colliderect(pygame.Rect(player.x,player.y,player.width,player.height)):
            self.isDraw=False
            return True