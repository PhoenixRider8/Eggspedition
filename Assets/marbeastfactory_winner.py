import pygame
from Assets.player import Player
from Assets.magnus import Magnus
from Assets.sam import Sams
from Assets.mrbeast import MrBeast
from Assets.teleport import Teleport
from Assets.maps import *
from Assets.manageDialogues import manageDialogue
from Assets.pyramid_maze import PyramidMaze

class MrBeastFactoryWinner():

    map_obj=Maps()

    def __init__(self):
        self.WIDTH=1300
        self.HEIGHT=768
        self.win=pygame.display.set_mode((1300,768))
        self.WHITE=(0,0,0)
        self.local=3
        self.music=pygame.mixer.Sound(r'Assets\\sprites\\music\\mr beast.mp3')

        icon_img=r'Assets\sprites\icons\chocolate(5).png'
        self.icon=pygame.image.load(icon_img).convert_alpha()
        icon_surface = pygame.Surface((32, 32))
        icon_surface.blit(self.icon, (0, 0))

        self.clock=pygame.time.Clock()

    def load_factory(self,music):
        pygame.display.set_caption("Mr Beast Factory")
        self.map_obj.tmx_data=None
        pygame.display.set_icon(self.icon)

        run=True
        #characters
        self.duffy=Player(647,621,32,32,r'Assets\\sprites\\maps\\mr beast factory\\tmx\\mr beast factory.tmx')
        self.duffy.vel+=10

        self.magnus=Magnus(706,621,32,32)
        self.sams=Sams(586,621,32,32)
        self.mrbeast=MrBeast(638,514,100,100)
        self.nextLevel=Teleport(778,296,32,32)
        self.map_obj.check=2

        #other dialogues
        self.beastdialogue_open = True
        self.beast_dialogue=manageDialogue()
        self.beast_dialogue.factory_winner_dialogue_set()
        self.maze=PyramidMaze()
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

            #draw characters
            self.magnus.homeMovement(self.win)
            self.sams.homeMovement(self.win)
            self.mrbeast.factoryMovement(self.win)

            if self.local==4:
                self.nextLevel.draw(self.win)
                if self.nextLevel.isCollide(self.duffy):
                    self.map_obj.check=1
                    music.stop()
                    self.duffy.map=None

                    self.maze.load_maze()
                    pygame.display.quit()
                    sys.exit()
        
                # if self.nextLevel.isCollide(self.duffy):
                #     self.map_obj.check=1
                #     self.music.stop()
                #     self.factory.load_factory()
                #     sys.exit()

            #check collision with nextLevel
            self.duffy.draw(self.win)

            if self.local==3:
                if self.beast_dialogue.factory_winner_dialogue_play(self.duffy,self.magnus,self.sams,self.win):
                    self.nextLevel.isDraw=True
                    self.local=4
                    
            pygame.display.update()


