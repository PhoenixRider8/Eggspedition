import pygame
from Assets.player import Player
from Assets.dialogue_box import DialogueBox
from Assets.magnus import Magnus
from Assets.sam import Sams
from Assets.enemy import Enemy
from Assets.teleport import Teleport
from Assets.maps import *
from Assets.manageDialogues import manageDialogue
from Assets.mrbeastfactory import MrBeastFactory

class Home(object):

    map_obj=Maps()

    def __init__(self):
        self.WIDTH=1300
        self.HEIGHT=768
        self.win=pygame.display.set_mode((1300,768))
        self.WHITE=(0,0,0)
        self.local=1
        # self.clock=pygame.time.Clock()


    def load_home(self,music):
        pygame.display.set_caption("Easter Valley")
        run=True
        self.local=1
        #characters
        self.duffy=Player(255,480,32,32,r'Assets\\sprites\\maps\\home\\tmx\\home.tmx')
        self.duffy.vel+=5
        self.magnus=Magnus(692,374,32,32)
        self.sams=Sams(634,374,32,32)
        self.rabbit=Enemy(654,299,32,32)
        self.nextLevel=Teleport(778,296,32,32)
        self.map_obj.homeMap(self.win)
        
        self.factory=MrBeastFactory()
        #text 
        self.player_dialogue=DialogueBox(0,700,1300,68,20,(0,0,0),5)
        self.player_dialogue.set_text("Duffy: Yaayyyyy!! Its the long awaited easter day. I am so excited to start my journey. The sun is shining and it is indeed a perfect day with the perfect weather.")
        self.playdialogue_open = True

        #other dialogues
        self.rabbitdialogue_open = False
        self.rabbit_dialogue=manageDialogue()
        self.rabbit_dialogue.home_dialogue_set()
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


            #draw dialogue
            if self.playdialogue_open:
                self.player_dialogue.draw(self.win,self.duffy.char1[0])
                self.player_dialogue.update(1000)
                
            
            keys=pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                self.playdialogue_open=False
                self.rabbitdialogue_open=True

            if self.local==2:
                self.nextLevel.draw(self.win)
                if self.nextLevel.isCollide(self.duffy):
                    self.map_obj.check=1
                    music.stop()
                    # Set the "Invisible Object" to be invisible
                    invisible_object = self.map_obj.tmx_data.get_object_by_name("call")
                    invisible_object.visible = False

                    # Set the "Invisible Layer" to be invisible
                    invisible_layer = self.map_obj.tmx_data.get_layer_by_name("Tile Layer 1")
                    invisible_layer.visible = False
                    self.duffy.map=None
                    self.factory.load_factory()
                    pygame.display.quit()
                    sys.exit()

            #check collision with nextLevel
            self.duffy.draw(self.win)

            if (self.magnus.homeDialogue(self.duffy,self.win) or self.sams.homeDialogue(self.duffy,self.win)) and self.rabbitdialogue_open and self.local==1:
                if self.rabbit_dialogue.home_dialogue_play(self.duffy,self.magnus,self.sams,self.win):
                    self.local+=1
                    self.nextLevel.isDraw=True  
            pygame.display.update()

    