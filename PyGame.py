import pygame
FPS= pygame.time.Clock()
pygame.init()


#global variables
running = True
MainGame = True
FirstTimeRunning = True
WordButton = None
WordButton1 = None
WordList= {'word1', 'word2', 'word3', 'word4', 'word5'}
W= 485
H= 1000
font = pygame.font.SysFont('Cambria', 20, 'black')
y= 90

#configuration maybe, idk
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('An app')


#images and related stuff
ButtonFirst = pygame.image.load("StartButton.png").convert_alpha()
WordHolderButton= pygame.image.load("WordsHolder.png").convert_alpha()
Bg= pygame.image.load("BackgroundA.png")
Exit= pygame.image.load("YetAnotherButton.jpg").convert_alpha()
Exit= pygame.transform.scale(Exit,(150,50))


def RandomWord(): #привязывает случаенное слово из множества к кнопке
    global WordList
    try:
        Word= WordList.pop()
        if Word != None:
            return Word
    except Exception:
            return 'out of words :('


class Buttons(): #Класс для кнопок
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = font.render(self.text_input, True, 'black')
        self.text_rect = self.text.get_rect(center=(self.x_pos,self.y_pos))

    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def CheckForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

#кнопки
StartButton = Buttons(ButtonFirst, W//2, H//2, None)
ExitButton = Buttons(Exit, 400, 940, "Exit")

def WordButton2(): ##Тут я пытался сделать что бы при каждом входе-выходе слово на кнопке менялось но у меня не очень получилось :(
    global FirstTimeRunning
    global WordButton
    if FirstTimeRunning == True:
        WordButton = Buttons(WordHolderButton, W // 2, y + 90, RandomWord())
        FirstTimeRunning= False
    return WordButton
def TheGameItselfOrSmthLikeThat(): #меню игры
    global running
    global MainGame
    global FirstTimeRunning
    screen.blit(Bg, (0, 0))
    while MainGame:
        FPS.tick(40)
        pygame.display.update()
        for event in pygame.event.get():
            WordButton2().update()
            ExitButton.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ExitButton.CheckForInput(pygame.mouse.get_pos()):
                    running = True
                    MainMenu()
                    MainGame= False
                    FirstTimeRunning = True
            if event.type == pygame.QUIT:
                running = False
                MainGame = False
                pygame.quit()

def MainMenu(): #главное меню
    global FirstTimeRunning
    global running
    screen.blit(Bg, (0, 0))
    while running:
        FPS.tick(40)
        pygame.display.update()
        for event in pygame.event.get():
            StartButton.update()
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if StartButton.CheckForInput(pygame.mouse.get_pos()):
                    TheGameItselfOrSmthLikeThat()
                    running= False
MainMenu()
