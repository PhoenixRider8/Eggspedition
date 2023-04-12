import pygame
from Assets.dialogue_box import DialogueBox
class manageDialogue():

    def __init__(self):
        self.text_array=[]
        self.img_array=[]
        self.dialogues=[]
        self.i=0

    #home dialogues

    def home_dialogue_set(self):
        self.text_array=['Duffy: Hey Magnus, are you ready?',
                         'Magnus: Hey Duffy, yes i am excited to play. What about you?',
                         'Duffy: yes me too. Hey Sam, how do you feel?',
                         'Sam: Hey Duffy, i am so thrilled to participate in this competition.',
                         
                         'Olive: A very good morning to all the brave players. The mission is simple,',
                         'Olive: You will be taken to different timelines and you all have to collect the hidden easter eggs.',
                         'Olive: You May Start!!!']
        
        self.img_array=[pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster.png'),
                        pygame.image.load(r'Assets\sprites\Player\2 Owlet_Monster\Owlet_Monster.png'),
                        pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster.png'),
                        pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster.png'),
                        pygame.image.load(r'Assets\sprites\Enemy\hi\hi.png'),
                        pygame.image.load(r'Assets\sprites\Enemy\hi\hi.png'),
                        pygame.image.load(r'Assets\sprites\Enemy\hi\hi.png')]
        
        self.dialogues=[DialogueBox(0,700,1300,68,20,(0,0,0),5),
                        DialogueBox(0,700,1300,68,20,(0,0,0),5),
                        DialogueBox(0,700,1300,68,20,(0,0,0),5),
                        DialogueBox(0,700,1300,68,20,(0,0,0),5),
                        DialogueBox(0,700,1300,68,20,(0,0,0),5),
                        DialogueBox(0,700,1300,68,20,(0,0,0),5),
                        DialogueBox(0,700,1300,68,20,(0,0,0),5)]
        
        for i in range(7):
            self.dialogues[i].set_text(self.text_array[i])
            # print(self.dialogues[i].text)
        
    def home_dialogue_play(self,duffy,magnus,sam,win):
        #set isplay to True
        duffy.isplay=True
        magnus.isplay=True
        sam.isplay=True

        # isContinue=False
        
        
        if self.i>=7:
            duffy.isplay=False
            magnus.isplay=False
            sam.isplay=False
            # isContinue=False
            self.dialogues[self.i-1].close()
            return True
        
        if not(self.dialogues[self.i].finish) and duffy.isplay:
            self.dialogues[self.i].draw(win,self.img_array[self.i])

            self.dialogues[self.i].update(1000)
        else:
            # isContinue=True
            self.i+=1

                

        #still animation
        if self.i<=3:
            win.blit(duffy.char1[0],(duffy.x,duffy.y))
            win.blit(magnus.char2[0],(magnus.x,magnus.y))
            win.blit(sam.char2[0],(sam.x,sam.y))
        else:
            win.blit(duffy.walkUp[0],(duffy.x,duffy.y))
            win.blit(magnus.walkUp[0],(magnus.x,magnus.y))
            win.blit(sam.walkUp[0],(sam.x,sam.y))

    #mr beast dialogues
    def factory_dialogue_set(self):
        self.text_array=['Fake mr Beast : HELLOOO!!! I am THE ONE AND ONLY MR BEAST FROM OHIO !! ',
                         'Sam: OMG! THE REAL MR BEAST! I am a HUGE FAN!',

                         'Fake Mr Beast : So, how are you guys?',
                         'Duffy,Sam,Magnus : GREAT!!',
                         
                         'Fake Mr beast : Yes that’s the spirit i am already impressed. So, my amazing contestants you will have to collect the feastible chocolates ',
                         'Fake Mr beast :  and anyone who fails to do so will get disqualified.',
                         'Fake Mr beast : So guys ARE YOU READY??!!',
                         'Duffy,Sam,Magnus : YESSS!!!!! LETS GOOOOO!!']
        
        self.img_array=[pygame.image.load(r'Assets\sprites\Mr beast\mr beast\Layer 1_sprite_1.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster.png').convert_alpha(),

                        pygame.image.load(r'Assets\sprites\Mr beast\mr beast\Layer 1_sprite_1.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Player\players.png').convert_alpha(),

                        pygame.image.load(r'Assets\sprites\Mr beast\mr beast\Layer 1_sprite_1.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Mr beast\mr beast\Layer 1_sprite_1.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Mr beast\mr beast\Layer 1_sprite_1.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Player\players.png').convert_alpha()]
        
        self.dialogues=[DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50)]
        
        for i in range(8):
            self.dialogues[i].set_text(self.text_array[i])
            # print(self.dialogues[i].text)

    def factory_dialogue_play(self,duffy,magnus,sam,win):
        #set isplay to True
        duffy.isplay=True
        magnus.isplay=True
        sam.isplay=True

        # isContinue=False
        
        
        if self.i>=8:
            duffy.isplay=False
            magnus.isplay=False
            sam.isplay=False
            # isContinue=False
            self.dialogues[self.i-1].close()
            return True
        
        if not(self.dialogues[self.i].finish) and duffy.isplay:
            self.dialogues[self.i].draw(win,self.img_array[self.i])

            self.dialogues[self.i].update(6000)
        else:
            # isContinue=True
            self.i+=1

        #still animation
    
        win.blit(duffy.walkUp[0],(duffy.x,duffy.y))
        win.blit(magnus.walkUp[0],(magnus.x,magnus.y))
        win.blit(sam.walkUp[0],(sam.x,sam.y))

    def factory_winner_dialogue_set(self):
        self.text_array=['Fake Mr Beast: Congratulations players, all of you did an outstanding job completing the mission.',
                         'Fake Mr Beast: However one of you failed to collect all the chocolates.',

                         'Sam: oh i wonder who it is.',
                         'Fake Mr Beast: Magnus, you have been disqualified. The rest of you may continue.',
                         
                         'Sam: Magnus, remember this is just the beginning. Don’t let this get you down. I believe in you.',
                         'Duffy: Nice try buddy. Better luck next time',
                         'Magnus: *groans* all the best guys .. . cya. . . .',
                         'Fake Mr Beast: Alrighty then qualifiers, now you shall enter the portal to move to the next level. ALL THE BEST!!']
        
        self.img_array=[pygame.image.load(r'Assets\sprites\Mr beast\mr beast\Layer 1_sprite_1.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Mr beast\mr beast\Layer 1_sprite_1.png').convert_alpha(),

                        pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Mr beast\mr beast\Layer 1_sprite_1.png').convert_alpha(),

                        pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Player\2 Owlet_Monster\Owlet_Monster.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Mr beast\mr beast\Layer 1_sprite_1.png').convert_alpha()]
        
        self.dialogues=[DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50)]
        
        for i in range(8):
            self.dialogues[i].set_text(self.text_array[i])
            # print(self.dialogues[i].text)

    def factory_winner_dialogue_play(self,duffy,magnus,sam,win):
        #set isplay to True
        duffy.isplay=True
        magnus.isplay=True
        sam.isplay=True

        # isContinue=False
        
        
        if self.i>=8:
            duffy.isplay=False
            magnus.isplay=False
            sam.isplay=False
            # isContinue=False
            self.dialogues[self.i-1].close()
            return True
        
        if not(self.dialogues[self.i].finish) and duffy.isplay:
            self.dialogues[self.i].draw(win,self.img_array[self.i])

            self.dialogues[self.i].update(6000)
        else:
            # isContinue=True
            self.i+=1

        #still animation
        if self.i<=3:
            win.blit(duffy.walkUp[0],(duffy.x,duffy.y))
            win.blit(magnus.walkUp[0],(magnus.x,magnus.y))
            win.blit(sam.walkUp[0],(sam.x,sam.y))
        else:
            win.blit(duffy.walkRight[0],(duffy.x,duffy.y))
            win.blit(magnus.walkLeft[0],(magnus.x,magnus.y))
            win.blit(sam.walkRight[0],(sam.x,sam.y))

    
    #pharoah dialogues
    def maze_dialogue_set(self):
        self.text_array=['Pharaoh : i, the great pharaoh, welcome you to the monumental and splendid land of Egypt. ',
                         'Sam:omg this is so amazing. I am so excited.',

                         'Pharaoh: thou shall collect gems which lies in the deadly maze, which is feared by all and return it to the pharaoh undamaged.',
                         'Duffy: i am so ready!',
                         
                         'Pharaoh: with the grace of the almighty osiris and isis may you be protected. YOU MAY BEGIN!!!',
                         'Sam:YESSSS!!!']
        
        self.img_array=[pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_100.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster.png').convert_alpha(),

                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_100.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster.png').convert_alpha(),

                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_100.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster.png').convert_alpha()]
        
        self.dialogues=[DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50)]
        
        for i in range(6):
            self.dialogues[i].set_text(self.text_array[i])
            # print(self.dialogues[i].text)

    def maze_dialogue_play(self,duffy,sam,win):
        #set isplay to True
        duffy.isplay=True
        sam.isplay=True

        # isContinue=False
        
        
        if self.i>=6:
            duffy.isplay=False
            sam.isplay=False
            # isContinue=False
            self.dialogues[self.i-1].close()
            return True
        
        if not(self.dialogues[self.i].finish) and duffy.isplay:
            self.dialogues[self.i].draw(win,self.img_array[self.i])

            self.dialogues[self.i].update(6000)
        else:
            # isContinue=True
            self.i+=1

        #still animation
    
        win.blit(duffy.walkUp[0],(duffy.x,duffy.y))
        win.blit(sam.walkUp[0],(sam.x,sam.y))

    def maze_winner_dialogue_set(self):
        self.text_array=['Pharaoh : CONGRATULATIONS PLAYERS!! You did a fantastic job!! However Sam you have been disqualified. ',
                         'Pharaoh : Farewell Sam, i wish you all the best for your next adventures.',
                         'Sam : Aww man.. its over already?',

                         'Pharaoh:And to Duffy you are THE WINNER!! The gods have been impressed.',
                         'Duffy: YAYYYYY!!! I WON!!',
                         
                         'Pharaoh: pass through the portal to go back to Easter Valley to claim your prize']
        
        self.img_array=[pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_100.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_100.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster.png').convert_alpha(),

                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_100.png').convert_alpha(),
                        pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster.png').convert_alpha(),

                        pygame.image.load(r'Assets\sprites\Pharoah\idle animation\pharoah_100.png').convert_alpha()]
        
        self.dialogues=[DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50),
                        DialogueBox(0,662,1300,100,20,(0,0,0),50)]
        
        for i in range(6):
            self.dialogues[i].set_text(self.text_array[i])
            # print(self.dialogues[i].text)

    def maze_winner_dialogue_play(self,duffy,sam,win):
        #set isplay to True
        duffy.isplay=True
        sam.isplay=True

        # isContinue=False
        
        
        if self.i>=6:
            duffy.isplay=False
            sam.isplay=False
            # isContinue=False
            self.dialogues[self.i-1].close()
            return True
        
        if not(self.dialogues[self.i].finish) and duffy.isplay:
            self.dialogues[self.i].draw(win,self.img_array[self.i])

            self.dialogues[self.i].update(6000)
        else:
            # isContinue=True
            self.i+=1

        #still animation
        if self.i<=2:
            win.blit(duffy.walkUp[0],(duffy.x,duffy.y))
            win.blit(sam.walkUp[0],(sam.x,sam.y))
        else:
            win.blit(duffy.walkRight[0],(duffy.x,duffy.y))
            win.blit(sam.walkLeft[0],(sam.x,sam.y))

    #winner announcement
    def home_dialogue_set1(self):
        self.text_array=['Olive :  congratulations duffy!!! You were so clever and cautious the entire time. ',
                         'Olive : You deserve to be the winner. Congrats again buddy.',

                         'Sam : HEY DUFFY! Congratulations',
                         'Magnus : congrats bud i already had a feeling that you were gonna win.',
                         
                         'Duffy : Thank you so much guys. It was such an amazing journey with you guys. It was so fun. ',
                         'Duffy : Sam and magnus you made my journey even better.',
                         'Duffy : Thank you so much for accompanying me on this journey.',

                         'Olive : With this we conclude our easter hunt competition. ',
                         'Duffy,Sam,Magnus : WISHING EVERYONE A VERY HAPPY EASTER.']
        
        self.img_array=[pygame.image.load(r'Assets\sprites\Enemy\hi\hi.png'),
                        pygame.image.load(r'Assets\sprites\Enemy\hi\hi.png'),

                        pygame.image.load(r'Assets\sprites\Player\3 Dude_Monster\Dude_Monster.png'),
                        pygame.image.load(r'Assets\sprites\Player\2 Owlet_Monster\Owlet_Monster.png'),
                        
                        pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster.png'),
                        pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster.png'),
                        pygame.image.load(r'Assets\sprites\Player\1 Pink_Monster\Pink_Monster.png'),

                        pygame.image.load(r'Assets\sprites\Enemy\hi\hi.png'),
                        pygame.image.load(r'Assets\sprites\Player\players.png')]
        
        self.dialogues=[DialogueBox(0,700,1300,100,20,(0,0,0),5),
                        DialogueBox(0,700,1300,100,20,(0,0,0),5),
                        DialogueBox(0,700,1300,100,20,(0,0,0),5),
                        DialogueBox(0,700,1300,100,20,(0,0,0),5),
                        DialogueBox(0,700,1300,100,20,(0,0,0),5),
                        DialogueBox(0,700,1300,100,20,(0,0,0),5),
                        DialogueBox(0,700,1300,100,20,(0,0,0),5),
                        DialogueBox(0,700,1300,100,20,(0,0,0),5),
                        DialogueBox(0,700,1300,100,20,(0,0,0),5)]
        
        for i in range(9):
            self.dialogues[i].set_text(self.text_array[i])
            # print(self.dialogues[i].text)
        
    def home_dialogue_play1(self,duffy,magnus,sam,win):
        #set isplay to True
        duffy.isplay=True
        magnus.isplay=True
        sam.isplay=True

        # isContinue=False
        
        
        if self.i>=9:
            duffy.isplay=False
            magnus.isplay=False
            sam.isplay=False
            # isContinue=False
            self.dialogues[self.i-1].close()
            return True
        
        if not(self.dialogues[self.i].finish) and duffy.isplay:
            self.dialogues[self.i].draw(win,self.img_array[self.i])

            self.dialogues[self.i].update(1000)
        else:
            # isContinue=True
            self.i+=1

                

        #still animation
        if self.i<=1:
            win.blit(duffy.walkUp[0],(duffy.x,duffy.y))
            win.blit(magnus.walkUp[0],(magnus.x,magnus.y))
            win.blit(sam.walkUp[0],(sam.x,sam.y))
        elif self.i==2:
            win.blit(duffy.walkLeft[0],(duffy.x,duffy.y))
            win.blit(magnus.walkLeft[0],(magnus.x,magnus.y))
            win.blit(sam.walkRight[0],(sam.x,sam.y))
        elif self.i==3:
            win.blit(duffy.walkRight[0],(duffy.x,duffy.y))
            win.blit(magnus.walkLeft[0],(magnus.x,magnus.y))
            win.blit(sam.walkRight[0],(sam.x,sam.y))
        elif self.i>3 and self.i<=6:
            win.blit(duffy.walkRight[0],(duffy.x,duffy.y))
            win.blit(magnus.walkLeft[0],(magnus.x,magnus.y))
            win.blit(sam.walkRight[0],(sam.x,sam.y))
        else:
            win.blit(duffy.walkRight[0],(duffy.x,duffy.y))
            win.blit(magnus.walkRight[0],(magnus.x,magnus.y))
            win.blit(sam.walkRight[0],(sam.x,sam.y))

    