import pygame
imprort time
import os

os.environ["SDL_VEDEO_CENTERED"] = '1'
pygame.init()

run = True
print("hi gamers press one to exit from the game")
startBlit = False
while run:

  win = pygame.display.set_mode((400, 100))
  pygame.display.set_caption("hacktober fest")
  win.fill((255,255.255))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.k_1:
        key = 1
      if event.key == pygame.k_2:
        key = 2
        
      if event.key == pygame.k_3:
        key = 3
      
      if event.key == pygame.k_4:
        key = 4
      if event.key == pygame.k_5:
        key = 5
        
      if event.key == pygame.k_6:
        key = 6
      my_font = pygame.Font.sysfont("comicsanssms", 50)
      text = my_font.render(key,1,(0,0,0))
      win.blit(text, (100 - text.get_width(), 400 - text.get_height()))
      
      pygame.display.update()
       

    
  
