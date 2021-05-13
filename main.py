# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import pygame
import MAGIC_sudoku

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)


class Button:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, text, pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = 3
        else:
            self.feedback = feedback
        self.change_text(text, bg)

    def change_text(self, text, bg="white"):
        """Change the text whe you click"""
        self.text = self.font.render(text, 1, pygame.Color("white"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    #self.change_text(self.feedback, bg="red")
                    pygame.quit()
                    SIZE = self.feedback
                    MAGIC_sudoku.sudoku(SIZE)


def mainloop():
    #prints the text that is not a button
    blue = (0, 0, 128)
    white = (255, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', 40)
    text = font.render('Would you like to play a', True, blue, white)
    textRect = text.get_rect()
    textRect.center = (250,100)
    text2 = font.render('Sudoku game', True, blue, white)
    textRect2 = text.get_rect()
    textRect2.center = (350,450)
    """ The infinite loop where things happen """
    while True:
        screen.fill(white)
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            button1.click(event)
            button2.click(event)
        button1.show()
        button2.show()
        clock.tick(30)
        pygame.display.update()


button1 = Button(
    "9x9",
    (50,200),
    font=100,
    bg="navy",
    feedback=3)
button2 = Button(
    "4x4",
    (300,200),
    font=100,
    bg="navy",
    feedback=2)

mainloop()
