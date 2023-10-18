import pygame
from particle_life import ParticleLife



class UserInterface():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((900, 600), pygame.RESIZABLE)
        pygame.display.set_caption('Tanks 3000')


        self.game_mode = ParticleLife()


        self.clock = pygame.time.Clock()
        self.running = True


    def run(self):
        while self.running:

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.game_mode.run(self.screen, events)

            # Update display
            pygame.display.update()
            # print(self.clock.get_fps())
            self.clock.tick(60)


user_interface = UserInterface()
user_interface.run()

