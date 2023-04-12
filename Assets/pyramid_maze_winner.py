import pygame
from Assets.player import Player
from Assets.sam import Sams
from Assets.pharoah import Pharoah
from Assets.teleport import Teleport
from Assets.maps import *
from Assets.manageDialogues import manageDialogue
from Assets.home2 import Home2

class MazeWinner():

    map_obj=Maps()

    def __init__(self):
        self.WIDTH=1300
        self.HEIGHT=768
        self.win=pygame.display.set_mode((1300,768))
        self.WHITE=(0,0,0)
        self.local=3
        self.music=pygame.mixer.Sound(r'Assets\\sprites\\music\\Ruins of Alph - Pokémon HeartGold & SoulSilver Music Extended.mp3')

        icon_img=r'Assets\sprites\icons\treasure.png'
        self.icon=pygame.image.load(icon_img).convert_alpha()
        icon_surface = pygame.Surface((32, 32))
        icon_surface.blit(self.icon, (0, 0))

        self.clock=pygame.time.Clock()

    def load_factory(self,music):
        pygame.display.set_caption("Treasure Hunt")
        self.map_obj.tmx_data=None
        pygame.display.set_icon(self.icon)

        run=True
        #characters
        self.duffy=Player(851.44,580.77,32,32,r'Assets\sprites\maps\egypt map\tmx\egpyt.tmx')
        self.duffy.vel+=10

        self.sams=Sams(955.87,581.83,32,32)
        self.pharoah=Pharoah(907.91,511.50,64,67)
        self.nextLevel=Teleport(1190.31,733.15,32,32)
        self.map_obj.check=2
        self.finish=Home2()

        #other dialogues
        self.paroah_dialogue=manageDialogue()
        self.paroah_dialogue.maze_winner_dialogue_set()
        # Create a surface to render the map on               

        while run:
            self.clock.tick(27)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            #draw movement
            self.duffy.movement()
            
            #draw map
            self.map_obj.pyramidMazeMap(self.win)

            #draw characters
            self.sams.homeMovement(self.win)
            self.pharoah.pyramidMovement(self.win)

            if self.local==4:
                self.nextLevel.draw(self.win)
                if self.nextLevel.isCollide(self.duffy):
                    #self.map_obj.check=1
                    music.stop()
                    self.duffy.map=None
                    self.finish.load_home()
        
                # if self.nextLevel.isCollide(self.duffy):
                #     self.map_obj.check=1
                #     self.music.stop()
                #     self.factory.load_factory()
                #     sys.exit()

            #check collision with nextLevel
            self.duffy.draw(self.win)

            if self.local==3:
                if self.paroah_dialogue.maze_winner_dialogue_play(self.duffy,self.sams,self.win):
                    self.nextLevel.isDraw=True
                    self.local=4
                    
            pygame.display.update()


