import pygame
class Sams(object):

    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.visible=True

        self.walkCount=0
        self.idleCount=0
        self.name="Sam"
        
        self.char1=[pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Idle_4\Layer 1_sprite_1.png'),
                    pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Idle_4\Layer 1_sprite_2.png'),
                    pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Idle_4\Layer 1_sprite_3.png'),
                    pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Idle_4\Layer 1_sprite_4.png')]
        
        self.char2=[pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Idle_4 (1)\Layer 1_sprite_1.png'),
                    pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Idle_4 (1)\Layer 1_sprite_2.png'),
                    pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Idle_4 (1)\Layer 1_sprite_3.png'),
                    pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Idle_4 (1)\Layer 1_sprite_4.png')]
        
        self.walkRight=[pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Run_6\Layer 1_sprite_1.png'),
                        pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Run_6\Layer 1_sprite_2.png'),
                        pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Run_6\Layer 1_sprite_3.png'),
                        pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Run_6\Layer 1_sprite_4.png')]
        
        self.walkLeft=[pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Run_6 (1)\Layer 1_sprite_1.png'),
                       pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Run_6 (1)\Layer 1_sprite_2.png'),
                       pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Run_6 (1)\Layer 1_sprite_3.png'),
                       pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Run_6 (1)\Layer 1_sprite_4.png')]
        
        self.walkUp=[pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Climb_4\Layer 1_sprite_1.png').convert_alpha(),
                     pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Climb_4\Layer 1_sprite_2.png').convert_alpha(),
                     pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Climb_4\Layer 1_sprite_3.png').convert_alpha(),
                     pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Climb_4\Layer 1_sprite_4.png').convert_alpha()]
        
        self.walkDown=[pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Run_6 (1)\Layer 1_sprite_1.png').convert_alpha(),
                       pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Run_6 (1)\Layer 1_sprite_2.png').convert_alpha(),
                       pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Run_6 (1)\Layer 1_sprite_3.png').convert_alpha(),
                       pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster_Run_6 (1)\Layer 1_sprite_4.png').convert_alpha()]
        
        self.rect=self.char1[0].get_rect()
        self.rect.x=x
        self.rect.y=y
        self.isplay=False

    def homeMovement(self,win):
        if self.visible and not(self.isplay):
            if self.walkCount+1>=7 or self.idleCount>=4:
                self.walkCount=0
                self.idleCount=0

            win.blit(self.walkUp[self.idleCount],(self.x,self.y))
            self.idleCount+=1

    def homeDialogue(self,player,win):
        #check for collision or interaction
        # pygame.draw.rect(win,(255,255,255),self.rect,2)
        if self.rect.colliderect(pygame.Rect(player.x, player.y, player.width, player.height)):
                return True
                
            