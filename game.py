###########
# Imports #
###########
import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

#############
# Variables #
#############
board_offset = (20, 20)
# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

init_board = [ # [val, isFresh]
    [[4, False], [2, False], [2, False], [4, False]], # col 1
    [[0, False], [0, False], [2, False], [2, False]], # col 2
    [[4, False], [0, False], [4, False], [2, False]], # col 3
    [[2, False], [2, False], [2, False], [2, False]] # col 4
]

##################
# Initialization #
##################
winHeight = 600 
winWidth = 800
WINDOW = pygame.display.set_mode((winWidth, winHeight), pygame.HWSURFACE|pygame.DOUBLEBUF)
# font = pygame.font.Font("PATHTOFONT", 20)
# pygame.display.set_caption("NAME")

###########
# Sprites #
###########
imgboard = pygame.image.load(os.path.join("resources","board.png")).convert_alpha()
img2 = pygame.image.load(os.path.join("resources", "2.png")).convert_alpha()
img4 = pygame.image.load(os.path.join("resources", "4.png")).convert_alpha()
img8 = pygame.image.load(os.path.join("resources", "8.png")).convert_alpha()
img16 = pygame.image.load(os.path.join("resources", "16.png")).convert_alpha()
img32 = pygame.image.load(os.path.join("resources", "32.png")).convert_alpha()
img64 = pygame.image.load(os.path.join("resources", "64.png")).convert_alpha()
img128 = pygame.image.load(os.path.join("resources", "128.png")).convert_alpha()
img256 = pygame.image.load(os.path.join("resources", "256.png")).convert_alpha()
img512 = pygame.image.load(os.path.join("resources", "512.png")).convert_alpha()
img1024 = pygame.image.load(os.path.join("resources", "1024.png")).convert_alpha()
img2048 = pygame.image.load(os.path.join("resources", "2048.png")).convert_alpha()

###########
# Classes #
###########
class Board():
    def __init__(self):
        self.board = init_board
        self.surf = imgboard
        self.rect = self.surf.get_rect(topleft=board_offset)

    def set_fresh(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j][1] = False

    def move(self, dir):
        if dir == "left":
            # move left
            for i, col in enumerate(self.board): # apply to each col
                for j in range(0, len(col), 1):
                    if self.board[i][j][0] > 0: # only move non-empty cells
                        curr = i
                        while curr-1 >= 0:
                            if self.board[curr-1][j][0] == 0: # if target cell empty
                                self.board[curr-1][j][0] = self.board[curr][j][0]
                                self.board[curr][j][0] = 0
                            elif self.board[curr][j][0] == self.board[curr-1][j][0] and not self.board[curr][j][1] and not self.board[curr-1][j][1]: # if target cell equal to current and neither have just been altered
                                # combine cells
                                self.board[curr-1][j][0] = self.board[curr][j][0] + self.board[curr-1][j][0]
                                self.board[curr-1][j][1] = True
                                self.board[curr][j][0] = 0
                            curr = curr-1
        elif dir == "right":
            for i, col in enumerate(self.board): # apply to each col
                # move right
                for j in range(len(col)-1, -1, -1): # -2 so bottom val is skipped
                    if self.board[i][j][0] > 0: # only move non-empty cells
                        curr = i
                        while curr+1 < 4:
                            if self.board[curr+1][j][0] == 0: # if target cell empty
                                self.board[curr+1][j][0] = self.board[curr][j][0]
                                self.board[curr][j][0] = 0
                            elif self.board[curr][j][0] == self.board[curr+1][j][0] and not self.board[curr][j][1] and not self.board[curr+1][j][1]: # if target cell equal to current and neither have just been altered
                                # combine cells
                                self.board[curr+1][j][0] = self.board[curr][j][0] + self.board[curr+1][j][0]
                                self.board[curr+1][j][1] = True
                                self.board[curr][j][0] = 0
                            curr = curr+1
        elif dir == "up":
            for i, col in enumerate(self.board): # apply to each col
                # move up
                for j in range(0, len(col), 1):
                    if self.board[i][j][0] > 0: # only move non-empty cells
                        curr = j # current index
                        while curr-1 >= 0:
                            if self.board[i][curr-1][0] == 0: # if target cell empty:
                                self.board[i][curr-1][0] = self.board[i][curr][0]
                                self.board[i][curr][0] = 0
                            elif self.board[i][curr][0] == self.board[i][curr-1][0] and not self.board[i][curr][1] and not self.board[i][curr-1][1]: # if target cell equal to current and neither have just been altered
                                # combine cells
                                self.board[i][curr-1][0] = self.board[i][curr][0] + self.board[i][curr-1][0]
                                self.board[i][curr-1][1] = True
                                self.board[i][curr][0] = 0
                            curr = curr-1             
        elif dir == "down":
            for i, col in enumerate(self.board): # apply to each col
                # move down
                for j in range(len(col)-2, -1, -1): # -2 so bottom val is skipped
                    if self.board[i][j][0] > 0: # only move non-empty cells
                        curr = j # current index
                        while curr+1 < 4:
                            if self.board[i][curr+1][0] == 0: # if target cell empty:
                                self.board[i][curr+1][0] = self.board[i][curr][0]
                                self.board[i][curr][0] = 0
                            elif self.board[i][curr][0] == self.board[i][curr+1][0] and not self.board[i][curr][1] and not self.board[i][curr+1][1]: # if target cell equal to current and neither have just been altered
                                # combine cells
                                self.board[i][curr+1][0] = self.board[i][curr][0] + self.board[i][curr+1][0]
                                self.board[i][curr+1][1] = True
                                self.board[i][curr][0] = 0
                            curr = curr+1
        self.set_fresh()

    def draw(self):
        WINDOW.blit(self.surf, self.rect)
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j][0] != 0:
                    x = self.rect.x + (12*(i+1)) + (128*i)
                    y = self.rect.y + (12*(j+1)) + (128*j)
                    img = globals()[f'img{self.board[i][j][0]}']
                    WINDOW.blit(img, (x, y))


####################
# Class References #
####################
board = Board()

#############
# Game Loop #
#############
while True:
    # fill screen every frame
    WINDOW.fill(WHITE)

    for event in pygame.event.get():
        #quit fuctionality
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # escape key to quit
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_a:
                board.move("left")
            if event.key == pygame.K_d:
                board.move("right")
            if event.key == pygame.K_w:
                board.move("up")
            if event.key == pygame.K_s:
                board.move("down")
    
    board.draw()
    pygame.display.update()