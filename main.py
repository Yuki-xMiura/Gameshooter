
import pygame

print("Setup Start")
pygame.init()
window = pygame.display.set_mode(size=(800, 600))
print("Setup End")

print('Loop Start')
while True:
# Check for all events
    for event in pygame.event.get():
        # If the event is QUIT then exit the program
        if event.type == pygame.QUIT:
            print('Loop End')
            pygame.quit()
            exit()