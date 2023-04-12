import pygame,sys
from pytmx.util_pygame import load_pygame

class Tile(pygame.sprite.Sprite):

    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image=surf
        self.rect=self.image.get_rect(topleft=pos)
        

class Maps(object):

    def __init__(self):
        self.check=1
        self.tmx_data=None
        self.loading=True

    def slide_animation(self,screen, image, start_pos, speed,sprite_group):
        # set up initial position
        image_x, image_y = start_pos

        # set up initial movement direction
        direction = "down"

        # set up game loop
        while True:
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit()
        
            # move image up or down
            if direction == "down":
                image_y += speed
                if image_y > 200:
                    direction = "up"
            else:
                image_y -= speed
                if image_y < -91:
                    self.check=0
                    direction = "down"
                    break
            
            # draw image on screen
            sprite_group.draw(screen)
            screen.blit(image, (image_x, image_y))
            
            
            # update display
            pygame.display.flip()
            
            # set frame rate
            pygame.time.Clock().tick(60)


    def handle_collisions(self,player, tmx_data):
        collisions_layer = tmx_data.get_object_group("objects")
        if collisions_layer is None:
            return False

        for obj in collisions_layer:
            if obj.type == "collidable":
                obj_rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                if player.rect.colliderect(obj_rect):
                    if player.vel_x > 0:
                        player.rect.right = obj_rect.left
                    elif player.vel_x < 0:
                        player.rect.left = obj_rect.right
                    if player.vel_y > 0:
                        player.rect.bottom = obj_rect.top
                    elif player.vel_y < 0:
                        player.rect.top = obj_rect.bottom
                    

    def check_collision_with_objects(self,player_rect, tmx_data,win):
        # Get the "collisions" object layer
        collisions_layer = tmx_data.get_layer_by_name('objects')

        # Iterate over the objects in the layer
        for obj in collisions_layer:
            if obj.type == "collidable":
                # Create a rect for the object
                obj_rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                # pygame.draw.rect(win,(255,255,255),obj_rect,2)
                # pygame.display.update()

                # Check if the player collides with the object
                if player_rect.colliderect(obj_rect):
                    return True


        # If we haven't returned yet, there's no collision
        return False

    def load_tmx_file(self,txt):
        tmx_data = load_pygame(txt)
        return tmx_data

    def homeMap(self,win):
        self.tmx_data = self.load_tmx_file(r'Assets\\sprites\\maps\\home\\tmx\\home.tmx')

        self.sprite_group=pygame.sprite.Group() #group of sprites

        home_board=pygame.image.load(r'Assets\\sprites\\main menu\\easter valley\\easter_valley(final).jpg')

        # Cycle through all layers
        layer_size=16
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer,'data'): #get tiled layers
                # print(layer)
                for x,y,surf in layer.tiles():
                    pos = (x*layer_size,y*layer_size)
                    Tile(pos=pos,surf=surf,groups=self.sprite_group)

        for obj in self.tmx_data.objects:
            pos=(obj.x,obj.y)
            if obj.image:
                Tile(pos=pos,surf=obj.image,groups=self.sprite_group)

        self.sprite_group.draw(win)
        start_pos=(390,0)
        if self.check==1:
            self.slide_animation(win,home_board,start_pos,5,self.sprite_group)

    def mrbeastFactoryMap(self,win):
        self.tmx_data=load_pygame(r'Assets\\sprites\\maps\\mr beast factory\\tmx\\mr beast factory.tmx')
        self.sprite_group1=pygame.sprite.Group() #group of sprites

        factory_board=pygame.image.load(r'Assets\\sprites\\main menu\\mr beast factory\\mr beast factory(full).png').convert_alpha()

        # Cycle through all layers
        layer_size=16
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer,'data'): #get tiled layers
                # print(layer)
                for x,y,surf in layer.tiles():
                    pos = (x*layer_size,y*layer_size)
                    Tile(pos=pos,surf=surf,groups=self.sprite_group1)

        for obj in self.tmx_data.objects:
            pos=(obj.x,obj.y)
            if obj.image:
                Tile(pos=pos,surf=obj.image,groups=self.sprite_group1)

        self.sprite_group1.draw(win)
        start_pos=(390,0)
        if self.check==1:
            self.slide_animation(win,factory_board,start_pos,10,self.sprite_group1)

    def pyramidMazeMap(self,win):
        self.tmx_data=load_pygame(r'Assets\sprites\maps\egypt map\tmx\egpyt.tmx')
        self.sprite_group1=pygame.sprite.Group() #group of sprites

        factory_board=pygame.image.load(r'Assets\sprites\main menu\maze\treasure hunt(final).png').convert_alpha()

        # Cycle through all layers
        layer_size=16
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer,'data'): #get tiled layers
                # print(layer)
                for x,y,surf in layer.tiles():
                    pos = (x*layer_size,y*layer_size)
                    Tile(pos=pos,surf=surf,groups=self.sprite_group1)

        for obj in self.tmx_data.objects:
            pos=(obj.x,obj.y)
            if obj.image:
                Tile(pos=pos,surf=obj.image,groups=self.sprite_group1)

        self.sprite_group1.draw(win)
        start_pos=(390,0)
        if self.check==1:
            self.slide_animation(win,factory_board,start_pos,5,self.sprite_group1)
