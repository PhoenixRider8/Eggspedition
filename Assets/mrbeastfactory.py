import pygame,sys
from Assets.player import Player
from Assets.marbeastfactory_winner import MrBeastFactoryWinner
from Assets.magnus import Magnus
from Assets.sam import Sams
from Assets.mrbeast import MrBeast
from Assets.maps import *
from Assets.manageDialogues import manageDialogue
from Assets.collectable import Collected
from Assets.easterEggs import EasterEggs

class MrBeastFactory():

    map_obj=Maps()

    def __init__(self):
        self.WIDTH=1300
        self.HEIGHT=768
        self.win=pygame.display.set_mode((1300,768))
        self.WHITE=(0,0,0)
        self.local=2
        self.music=pygame.mixer.Sound(r'Assets\\sprites\\music\\mr beast.mp3')

        icon_img=r'Assets\sprites\icons\chocolate(5).png'
        self.icon=pygame.image.load(icon_img).convert_alpha()
        icon_surface = pygame.Surface((32, 32))
        icon_surface.blit(self.icon, (0, 0))

        self.clock=pygame.time.Clock()

    def load_factory(self):
        pygame.display.set_caption("Mr Beast Factory")
        self.music.play()
        self.map_obj.tmx_data=None
        pygame.display.set_icon(self.icon)

        run=True
        #characters
        self.duffy=Player(647,621,32,32,r'Assets\\sprites\\maps\\mr beast factory\\tmx\\mr beast factory.tmx')
        self.duffy.vel+=10

        self.magnus=Magnus(706,621,32,32)
        self.sams=Sams(586,621,32,32)
        self.mrbeast=MrBeast(638,514,100,100)
        self.map_obj.mrbeastFactoryMap(self.win)
        self.winner=MrBeastFactoryWinner()

        #collectables
        self.feastables=[pygame.image.load(r'Assets\sprites\easter eggs\feastables\chocolates\1.png').convert_alpha(),
                         pygame.image.load(r'Assets\sprites\easter eggs\feastables\chocolates\2.png').convert_alpha(),
                         pygame.image.load(r'Assets\sprites\easter eggs\feastables\chocolates\3.png').convert_alpha(),
                         pygame.image.load(r'Assets\sprites\easter eggs\feastables\chocolates\4.png').convert_alpha(),
                         pygame.image.load(r'Assets\sprites\easter eggs\feastables\chocolates\5.png').convert_alpha()]
        self.collect=Collected(self.feastables[0],len(self.feastables),0)

        #set easter eggs
        self.easter_eggs=[EasterEggs(54,654,32,47,self.feastables[0]),
                          EasterEggs(806,380,32,55,self.feastables[1]),
                          EasterEggs(1265.96,245.09,32,65,self.feastables[2]),
                          EasterEggs(1256.37,668.15,32,60,self.feastables[3]),
                          EasterEggs(54,187,32,54,self.feastables[4])]

        #other dialogues
        self.beastdialogue_open = True
        self.beast_dialogue=manageDialogue()
        self.beast_dialogue.factory_dialogue_set()
        # Create a surface to render the map on               

        while run:
            self.clock.tick(27)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            #draw movement
            self.duffy.movement()
            
            #draw map
            self.map_obj.mrbeastFactoryMap(self.win)

            # show collected
            self.collect.draw(self.win,59,37)

            #draw characters
            self.magnus.homeMovement(self.win)
            self.sams.homeMovement(self.win)
            self.mrbeast.factoryMovement(self.win)

            #check if all easter eggs are collected
            if self.collect.val==0:
                self.local=3
            
            if self.local==3:
                if self.mrbeast.isCollide(self.duffy):
                    self.duffy.x=647
                    self.duffy.y=700
                    self.duffy.rect.x=self.duffy.x
                    self.duffy.rect.y=self.duffy.y
                    self.local=4
                    self.winner.load_factory(self.music)
                    sys.exit()
                # if self.nextLevel.isCollide(self.duffy):
                #     self.map_obj.check=1
                #     self.music.stop()
                #     self.factory.load_factory()
                #     sys.exit()

            #check collision with nextLevel
            self.duffy.draw(self.win)

            if self.local==2:
                if self.beast_dialogue.factory_dialogue_play(self.duffy,self.magnus,self.sams,self.win):
                    for i in range(len(self.easter_eggs)):
                        self.easter_eggs[i].draw(self.win)
                        if self.duffy.check_collision_with_easter_eggs(self.easter_eggs[i]):
                            self.collect.val-=1
                            self.collect.i+=1
                            self.easter_eggs.pop(i)
                            break
                    
            pygame.display.update()


