import pygame
from Assets.player import Player
from Assets.dialogue_box import DialogueBox
from Assets.magnus import Magnus
from Assets.sam import Sams
from Assets.enemy import Enemy
from Assets.maps import *
from Assets.manageDialogues import manageDialogue

class Home2(object):

    map_obj=Maps()

    def __init__(self):
        self.WIDTH=1300
        self.HEIGHT=768
        self.win=pygame.display.set_mode((1300,768))
        self.WHITE=(0,0,0)
        self.local=1
        bgSound1=r'Assets\\sprites\\music\\main menu.mp3'
        self.music=pygame.mixer.Sound(bgSound1)
        
        # self.clock=pygame.time.Clock()


    def load_home(self):
        self.music.play()
        pygame.display.set_caption("Easter Valley")
        run=True
        self.local=1
        #characters
        self.duffy=Player(650,374,32,32,r'Assets\\sprites\\maps\\home\\tmx\\home.tmx')
        self.duffy.vel+=5
        self.magnus=Magnus(692,374,32,32)
        self.sams=Sams(634,374,32,32)
        self.rabbit=Enemy(654,299,32,32)
        self.map_obj.homeMap(self.win)

        #other dialogues
        self.rabbitdialogue_open = True
        self.rabbit_dialogue=manageDialogue()
        self.rabbit_dialogue.home_dialogue_set1()
        # Create a surface to render the map on               

        while run:
            # self.clock.tick(27)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # clear the screen
            #draw movement
            self.duffy.movement()
            
            #draw map
            self.map_obj.homeMap(self.win)

            #draw characters
            self.magnus.homeMovement(self.win)
            self.sams.homeMovement(self.win)
            self.rabbit.homeMovement(self.win)

            if self.local==2:
                sys.exit()

            #check collision with nextLevel
            self.duffy.draw(self.win)

            if self.rabbit_dialogue.home_dialogue_play1(self.duffy,self.magnus,self.sams,self.win):
                self.local+=1
            pygame.display.update()

    