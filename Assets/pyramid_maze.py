import pygame,sys
from Assets.player import Player
from Assets.pyramid_maze_winner import MazeWinner
from Assets.sam import Sams
from Assets.pharoah import Pharoah
from Assets.maps import *
from Assets.manageDialogues import manageDialogue
from Assets.collectable import Collected
from Assets.easterEggs import EasterEggs

class PyramidMaze():

    map_obj=Maps()

    def __init__(self):
        self.WIDTH=1300
        self.HEIGHT=768
        self.win=pygame.display.set_mode((1300,768))
        self.WHITE=(0,0,0)
        self.local=2
        self.music=pygame.mixer.Sound(r'Assets\sprites\music\Ruins of Alph - Pokémon HeartGold & SoulSilver Music Extended.mp3')

        icon_img=r'Assets\sprites\icons\treasure.png'
        self.icon=pygame.image.load(icon_img).convert_alpha()
        icon_surface = pygame.Surface((32, 32))
        icon_surface.blit(self.icon, (0, 0))

        self.clock=pygame.time.Clock()

    def load_maze(self):
        pygame.display.set_caption("Treasure Hunt")
        self.music.play()
        self.map_obj.tmx_data=None
        pygame.display.set_icon(self.icon)

        run=True
        #characters
        self.duffy=Player(101.23,125.74,32,32,r'Assets\sprites\maps\egypt map\tmx\egpyt.tmx')
        self.duffy.vel+=10

        self.sams=Sams(181.16,126.81,32,32)
        self.pharoah=Pharoah(136.40,58.61,64,67)
        self.map_obj.pyramidMazeMap(self.win)
        self.winner=MazeWinner()

        #collectables
        self.gems=[pygame.image.load(r'Assets\sprites\easter eggs\gems\1.png').convert_alpha(),
                   pygame.image.load(r'Assets\sprites\easter eggs\gems\2.png').convert_alpha(),
                   pygame.image.load(r'Assets\sprites\easter eggs\gems\3.png').convert_alpha(),
                   pygame.image.load(r'Assets\sprites\easter eggs\gems\4.png').convert_alpha(),
                   pygame.image.load(r'Assets\sprites\easter eggs\gems\5.png').convert_alpha()]
        
        self.collect=Collected(self.gems[0],len(self.gems),0)

        #set easter eggs
        self.easter_eggs=[EasterEggs(424.00,372.00,32,21,self.gems[0]),
                          EasterEggs(74.00,706.00,32,24,self.gems[1]),
                          EasterEggs(506.00,698.00,32,25,self.gems[2]),
                          EasterEggs(840.00,362.00,32,27,self.gems[3]),
                          EasterEggs(1136.00,354.00,32,28,self.gems[4])]

        #other dialogues
        self.beastdialogue_open = True
        self.beast_dialogue=manageDialogue()
        self.beast_dialogue.maze_dialogue_set()
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

            # show collected
            self.collect.draw(self.win,59,37)

            #draw characters
            self.sams.homeMovement(self.win)
            self.pharoah.pyramidMovement(self.win)

            #check if all easter eggs are collected
            if self.collect.val==0:
                self.local=3
            
            if self.local==3:
                if self.pharoah.isCollide(self.duffy):
                    self.duffy.x=851.44
                    self.duffy.y=580.77
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
                if self.beast_dialogue.maze_dialogue_play(self.duffy,self.sams,self.win):
                    for i in range(len(self.easter_eggs)):
                        self.easter_eggs[i].draw(self.win)
                        if self.duffy.check_collision_with_easter_eggs(self.easter_eggs[i]):
                            self.collect.val-=1
                            self.collect.i+=1
                            self.easter_eggs.pop(i)
                            break
                    
            pygame.display.update()


