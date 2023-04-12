import pygame,sys
from Assets.home import Home

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH=1300
HEIGHT=768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eggspedition")

icon_img=r'Assets\\sprites\\icons\\icon.png'
icon=pygame.image.load(icon_img)
icon_surface = pygame.Surface((32, 32))
icon_surface.blit(icon, (0, 0))
pygame.display.set_icon(icon)

clock=pygame.time.Clock()


# Set up the fonts
title_font = pygame.font.Font(None, 80)
button_font = pygame.font.Font(None, 40)

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

# Set up music
bgSound1=r'Assets\\sprites\\music\\main menu.mp3'
music=pygame.mixer.Sound(bgSound1)
music.play()

# Set up background
bg=pygame.transform.scale(pygame.image.load(r'Assets\\sprites\\main menu\\mainmenu.png'), (WIDTH, HEIGHT))
title=pygame.transform.scale(pygame.image.load(r'Assets\\sprites\\main menu\\title(1).png'),(1300,150))
pos=(0,0)

# Set up the buttons
button_image = pygame.image.load(r'Assets\\sprites\\main menu\\blue_button00.png')
font = pygame.font.Font(None, 24)
text_surface = font.render("Start", True, (255, 255, 255))
start_button = pygame.Rect(190, 380, 190,49)
button_surface = pygame.Surface((190, 50))
button_surface.set_colorkey(pygame.Color('gray'))
button_surface.blit(button_image, (0, 0))
button_surface.blit(text_surface, (75, 15))

text_surface1 = font.render("Quit", True, (255, 255, 255))
quit_button = pygame.Rect(190, 480, 190,49)
button_surface1 = pygame.Surface((190, 50))
button_surface1.set_colorkey(pygame.Color('gray'))
button_surface1.blit(button_image, (0, 0))
button_surface1.blit(text_surface1, (75, 15))

# Set up objects
home=Home()
# Set up the game loop
running = True
while running:
    clock.tick(27)
    # Handle events
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
                home.load_home(music)
                pygame.display.quit()
                sys.exit()
                #print("Starting game...")
            elif quit_button.collidepoint(event.pos):
                # Quit game
                print("Quit clicked")
                running = False

    # Clear the screen
    screen.blit(bg,(0,0))

    # Draw the title
    screen.blit(title,pos)

    # Draw the buttons
    screen.blit(button_surface, start_button)
    screen.blit(button_surface1, quit_button)

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
