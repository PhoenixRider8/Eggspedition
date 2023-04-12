import pygame

class DialogueBox:
    def __init__(self, x, y, width, height, font_size, font_color, text_speed):
        # set up font
        pygame.font.init()
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), font_size)

        # set up dialogue box properties
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 255, 255)
        self.alpha = 200

        # set up text properties
        self.text =""
        self.font_color = font_color
        self.text_speed = text_speed
        self.text_surface = None
        self.box_surface = None
        self.text_rect = None
        self.text_index = 0
        self.text_timer = 0
        self.finish=False

        self.clock=pygame.time.Clock()

    def set_text(self, text):
        self.text = text
        self.text_surface = self.font.render("", True, self.font_color)
        self.text_rect = pygame.Rect(self.x + 10, self.y + 10, self.width - 20, self.height - 20)
        self.text_index = 0
        self.text_timer = 0

    def update(self, delta_time):
        if self.text_index < len(self.text):
            self.text_timer += delta_time
            if self.text_timer > self.text_speed:
                self.text_timer -= self.text_speed
                self.text_index += 1
                self.text_surface = self.font.render(self.text[:self.text_index], True, self.font_color)
        elif self.text_index == len(self.text):
            self.finish=True

    def draw(self, surface,img):
        # draw dialogue box background
        self.box_surface = pygame.Surface((self.width, self.height))
        self.box_surface.fill((self.color[0], self.color[1], self.color[2], self.alpha))
        surface.blit(self.box_surface, (self.x, self.y))
        # pygame.time.delay(10)
        self.clock.tick(27)
        surface.blit(img,(self.x,self.y))

        # draw text
        if self.text_surface is not None:
            surface.blit(self.text_surface, (self.text_rect.x+img.get_width(), self.text_rect.y))

    def close(self):
        self.box_surface.set_alpha(0)
        self.text_surface.set_alpha(0)
