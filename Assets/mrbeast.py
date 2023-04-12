import pygame
class MrBeast():

    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.name="Mr. Beast"
        self.visible=True

        self.walkCount=0
        self.idleCount=0

        self.walkRight=[pygame.image.load(r'Assets\sprites\Mr beast\mr beast\Layer 1_sprite_1.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Mr beast\mr beast\Layer 1_sprite_2.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Mr beast\mr beast\Layer 1_sprite_3.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Mr beast\mr beast\Layer 1_sprite_4.png').convert_alpha()]



        self.rect=self.walkRight[0].get_rect()
        self.rect.x=x
        self.rect.y=y
        self.isplay=False



    def factoryMovement(self,win):
        if self.visible and not(self.isplay):
            if self.walkCount+1>=7 or self.idleCount>=4:
                self.walkCount=0
                self.idleCount=0

            win.blit(self.walkRight[self.idleCount],(self.x,self.y))
            self.idleCount+=1

    def isCollide(self,player):
        if self.rect.colliderect(pygame.Rect(player.x,player.y,player.width,player.height)):
            return True