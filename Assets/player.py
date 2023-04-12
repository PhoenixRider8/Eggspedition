import pygame
from pytmx.util_pygame import load_pygame

#from Assets.collectable import Collected
class Player(object):
    
    def __init__(self,x,y,width,height,map):
        self.reset(x,y,width,height)
        self.HEIGHT=1300
        self.WIDTH=1300
        self.tmx_data=load_pygame(map)
        self.bumpIntoSound=pygame.mixer.Sound(r'Assets\sprites\sound effect\bumpintowall_X5CNQPB.mp3')
        self.camera=None
        self.isplay=False

    def apply_offset(self, offset):
        self.rect.x += offset[0]
        self.rect.y += offset[1]
    
    def check_collision_with_objects(self):
        collisions_layer = self.tmx_data.get_layer_by_name("objects")
        for obj in collisions_layer:
            if obj.type == "collidable":
                if self.rect.colliderect(pygame.Rect(obj.x, obj.y, obj.width, obj.height)):
                    return True
        return False

    def movement(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x>self.vel and self.x+self.width<self.WIDTH and not(self.isplay): 
            self.x-=self.vel
            self.rect.x-=self.vel
            self.left=True
            self.right=False
            self.standing=False
            self.direc=-1
            if self.check_collision_with_objects():
                self.x+=1.3*self.vel
                self.rect.x=self.x
                self.bumpIntoSound.play()
            
        elif keys[pygame.K_RIGHT] and self.x<self.WIDTH-self.width-self.vel and self.x+self.width<self.WIDTH and not(self.isplay):
            self.x+=self.vel
            self.rect.x+=self.vel
            self.left=False
            self.right=True
            self.up=False
            self.down=False
            self.standing=False
            self.direc=1
            if self.check_collision_with_objects():
                self.x-=1.3*self.vel
                self.rect.x=self.x
                self.bumpIntoSound.play()

        elif keys[pygame.K_UP] and self.y>self.vel and self.y+self.height<self.HEIGHT and not(self.isplay):
            self.y-=self.vel
            self.rect.y-=self.vel
            self.left=False
            self.right=False
            self.up=True
            self.down=False
            self.standing=False
            self.walkCount=0
            if self.check_collision_with_objects():
                self.y+=1.3*self.vel
                self.rect.y=self.y
                self.bumpIntoSound.play()

        elif keys[pygame.K_DOWN] and self.y>self.vel and self.y+self.height<self.HEIGHT and not(self.isplay):
            self.y+=self.vel
            self.rect.y+=self.vel
            self.left=False
            self.right=False
            self.up=False
            self.down=True
            self.standing=False
            self.idleCount=0
            if self.check_collision_with_objects():
                self.y-=1.3*self.vel
                self.rect.y=self.y
                self.bumpIntoSound.play()
            
        else:
            self.walkCount=0
            if not(self.isplay):
                self.standing=True
            else:
                self.standing=False
            self.isCollide=False
            self.moving=False

    
            
            
    def draw(self,win):
        pygame.time.delay(50)
        
        if self.visible:
            if self.walkCount+1>=7 or self.idleCount>=4:
                self.walkCount=0
                self.idleCount=0

            if not(self.standing):
                if self.left:
                    win.blit(self.walkLeft[self.walkCount],(self.x,self.y))
                    self.walkCount+=1
                elif self.right:
                    win.blit(self.walkRight[self.walkCount],(self.x,self.y))
                    self.walkCount+=1
                elif self.up:
                    win.blit(self.walkUp[self.idleCount],(self.x,self.y))
                    self.idleCount+=1
                elif self.down:
                    win.blit(self.walkDown[self.walkCount],(self.x,self.y))
                    self.walkCount+=1
            else:
                if self.right:
                    win.blit(self.char1[self.idleCount],(self.x,self.y))
                    self.idleCount+=1
                elif self.left:
                    win.blit(self.char2[self.idleCount],(self.x,self.y))
                    self.idleCount+=1
                elif self.up:
                    win.blit(self.walkUp[self.idleCount],(self.x,self.y))
                    self.idleCount+=1
                elif self.down:
                    win.blit(self.walkDown[self.walkCount],(self.x,self.y))
                    self.walkCount+=1
                else:
                    if self.direc==1:
                            win.blit(self.char1[self.idleCount], (self.x, self.y))
                            self.idleCount+=1
                    elif self.direc==-1:
                        win.blit(self.char2[self.idleCount], (self.x, self.y))
                        self.idleCount+=1
                    else:
                        win.blit(self.char1[self.idleCount], (self.x, self.y))
                        self.idleCount+=1

        #self.hitbox=(self.x+17,self.y+11,29,52) #set position every movement
        # pygame.draw.rect(win,(255,255,255),self.rect,2)

    def reset(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5

        self.isJump=False
        self.jumpCount=10
        self.left=False
        self.right=False
        self.up=False
        self.down=False
        self.isCollide=False
        self.moving=False
        self.isAttack=False

        self.walkCount=0
        self.standing=True
        self.direc=0 #direction at which player is facing before jumping
        self.hitbox=(self.x+17,self.y+11,29,52) #rectangle of 28x60
        self.cosVal=0 #number of items collected

        #fps of animation
        self.idleCount=0

        #Player animations
        self.char1=[pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Idle_4\Layer 1_sprite_1.png').convert_alpha(),
                    pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Idle_4\Layer 1_sprite_2.png').convert_alpha(),
                    pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Idle_4\Layer 1_sprite_3.png').convert_alpha(),
                    pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Idle_4\Layer 1_sprite_4.png').convert_alpha()]
        
        self.char2=[pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Idle_4 (1)\Layer 1_sprite_1.png').convert_alpha(),
                    pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Idle_4 (1)\Layer 1_sprite_2.png').convert_alpha(),
                    pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Idle_4 (1)\Layer 1_sprite_3.png').convert_alpha(),
                    pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Idle_4 (1)\Layer 1_sprite_4.png').convert_alpha()]

        self.walkRight=[pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Walk_6\Layer 1_sprite_1.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Walk_6\Layer 1_sprite_2.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Walk_6\Layer 1_sprite_3.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Walk_6\Layer 1_sprite_4.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Walk_6\Layer 1_sprite_5.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Walk_6\Layer 1_sprite_6.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Walk_6\Layer 1_sprite_7.png').convert_alpha()]
        
        self.walkLeft=[pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Walk_6 (1)\Layer 1_sprite_1.png').convert_alpha(),
                       pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Walk_6 (1)\Layer 1_sprite_2.png').convert_alpha(),
                       pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Walk_6 (1)\Layer 1_sprite_3.png').convert_alpha(),
                       pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Walk_6 (1)\Layer 1_sprite_4.png').convert_alpha(),
                       pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Walk_6 (1)\Layer 1_sprite_5.png').convert_alpha(),
                       pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Walk_6 (1)\Layer 1_sprite_6.png').convert_alpha(),
                       pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Walk_6 (1)\Layer 1_sprite_7.png').convert_alpha()]
        
        self.walkUp=[pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Climb_4\Layer 1_sprite_1.png').convert_alpha(),
                     pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Climb_4\Layer 1_sprite_2.png').convert_alpha(),
                     pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Climb_4\Layer 1_sprite_3.png').convert_alpha(),
                     pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Climb_4\Layer 1_sprite_4.png').convert_alpha()]
        
        self.walkDown=[pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Walk_6\Layer 1_sprite_1.png').convert_alpha(),
                       pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Walk_6\Layer 1_sprite_2.png').convert_alpha(),
                       pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Walk_6\Layer 1_sprite_3.png').convert_alpha(),
                       pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Walk_6\Layer 1_sprite_4.png').convert_alpha(),
                       pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Walk_6\Layer 1_sprite_5.png').convert_alpha(),
                       pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Walk_6\Layer 1_sprite_6.png').convert_alpha(),
                       pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Walk_6\Layer 1_sprite_7.png').convert_alpha()]
        
        self.attack1=[pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Attack1_4\Layer 1_sprite_1.png').convert_alpha(),
                      pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Attack1_4\Layer 1_sprite_2.png').convert_alpha(),
                      pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Attack1_4\Layer 1_sprite_1.png').convert_alpha(),
                      pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster_Attack1_4\Layer 1_sprite_4.png').convert_alpha()]


        # self.carrotImg=pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\carrot\\carrot.png')
        # self.collectable=Collected(self.carrotImg,self.cosVal)

        # self.img=pygame.image.load(r'D:\\Python\\my projects\\pygame\\Wild Hare Run A Quest for Carrots\\sprites\\health\\heart.png')
        #health bar

        self.visible=True

        self.rect=self.char1[0].get_rect()
        self.rect.x=x
        self.rect.y=y

            
    def check_collision_with_easter_eggs(self,easter_eggs):
        if self.rect.colliderect(pygame.Rect(easter_eggs.x,easter_eggs.y,easter_eggs.width,easter_eggs.height)):
            easter_eggs.visible=False
            return True

