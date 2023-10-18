import pygame

class Slider():
    def __init__(self, pos, size, initial_val, min, max, color):
        self.pos = pos
        self.size = size

        self.slider_left_pos = self.pos[0] - (size[0]//2)
        self.slider_right_pos = self.pos[0] + (size[0] // 2)
        self.slider_top_pos = self.pos[1] - (size[1] // 2)

        self.min = min
        self.max = max

        self.color = color

        self.initial_val = (self.slider_right_pos - self.slider_left_pos) * initial_val

        self.font = pygame.font.Font(None, 14)

        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
        self.button_rect = pygame.Rect(self.slider_left_pos + self.initial_val - 5, self.slider_top_pos, 10, self.size[1])


    def move_slider(self, mouse_pos):
        self.button_rect.centerx = mouse_pos[0]

    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos
        button_val = self.button_rect.centerx - self.slider_left_pos
        val = (button_val / val_range) * (self.max + self.min - self.min)
        self.val = (2 * (val - 1)) / 1
        return self.val

    def calculate_button_centerx(self, val):
        normalized_val = ((val/2) + 1) / 2  # Normalize val to the range [0, 1]
        val_range = self.slider_right_pos - self.slider_left_pos
        button_val = normalized_val * val_range
        self.button_rect.centerx = button_val + self.slider_left_pos



    def draw(self, screen):
        pygame.draw.rect(screen, 'darkgrey', self.container_rect)
        pygame.draw.rect(screen, self.color, self.button_rect)


        text_value = self.font.render(str(self.val), True, 'white')


        screen.blit(text_value, self.pos)


class Button():
    def __init__(self, pos, size, text):
        self.pos = pos
        self.size = size


        self.font = pygame.font.Font(None, 24)
        self.text = self.font.render(text, True, 'black')
        self.button_rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

        self.pressed = False


    def draw(self, screen):

        pygame.draw.rect(screen,'grey', self.button_rect)
        screen.blit(self.text, self.pos)


class TextBox():
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.font = pygame.font.Font(None, 16)

        self.text = ''
        self.text_to_render = self.font.render(str(self.text), True, 'white')

        self.active = False

        self.box_rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])


    def input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

            self.text_to_render = self.font.render(str(self.text), True, 'black')

    def draw(self, screen):
        pygame.draw.rect(screen, 'white', self.box_rect)
        screen.blit(self.text_to_render, self.pos)






