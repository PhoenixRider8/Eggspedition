import pygame
class Pharoah():

    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.name="Pharoah"
        self.visible=True

        self.walkCount=0
        self.idleCount=0

        self.walkRight=[pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_100.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_101.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_102.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_103.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_104.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_105.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_106.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_107.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_108.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_109.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_110.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_112.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_113.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_114.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_115.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_116.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_117.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_118.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_119.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_120.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_121.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_122.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_123.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_124.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_125.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_126.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_127.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_128.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_129.png').convert_alpha()]



        self.rect=self.walkRight[0].get_rect()
        self.rect.x=x
        self.rect.y=y
        self.isplay=False



    def pyramidMovement(self,win):
        if self.visible and not(self.isplay):
            if self.idleCount>=29:
                self.walkCount=0
                self.idleCount=0

            win.blit(self.walkRight[self.idleCount],(self.x,self.y))
            self.idleCount+=1

    def isCollide(self,player):
        if self.rect.colliderect(pygame.Rect(player.x,player.y,player.width,player.height)):
            return True