###########
# Imports #
###########
import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import random

pygame.init()

#############
# Variables #
#############
board_offset = (20, 20)
# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

##################
# Initialization #
##################
winHeight = 600 
winWidth = 800
WINDOW = pygame.display.set_mode((winWidth, winHeight), pygame.HWSURFACE|pygame.DOUBLEBUF)
font = pygame.font.Font("resources/arial.ttf", 20)
pygame.display.set_caption("2048 AI")

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
        self.board = [[]]
        self.surf = imgboard
        self.rect = self.surf.get_rect(topleft=board_offset)
        self.score = 0
        self.sum = 0
        self.board_collapsed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.reset()

    def reset(self):
        self.board = [ # [val, isFresh]
            [[0, False], [0, False], [0, False], [0, False]], # col 1
            [[0, False], [0, False], [0, False], [0, False]], # col 2
            [[0, False], [0, False], [0, False], [0, False]], # col 3
            [[0, False], [0, False], [0, False], [0, False]] # col 4
        ]
        self.score = 0
        self.sum = 0
        self.board_collapsed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.gen_num()

    def set_fresh(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j][1] = False

    def gen_num(self):
        # generate a 2 or a 4 in a random empty spot on the board
        randx, randy = -1, -1
        attempts = 0
        while True: # brute force process of finding an open space, break if found or none empty
            randx = random.randint(0, 3)
            randy = random.randint(0, 3)
            attempts = attempts+1
            if self.board[randx][randy][0] == 0 or attempts >= 16:
                break
        if attempts >= 16:
            return 0
        num = random.choices([2, 4], weights=(9, 1), k=1)[0]
        self.board[randx][randy][0] = num
        

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
                                self.score += self.board[curr-1][j][0]
                                self.board[curr-1][j][1] = True
                                self.board[curr][j][0] = 0
                            curr = curr-1
        elif dir == "right":
            for j, col in enumerate(self.board): # apply to each col
                # move right
                for i in range(len(col)-1, -1, -1):
                    if self.board[i][j][0] > 0: # only move non-empty cells
                        curr = i # current index
                        while curr+1 < 4:
                            if self.board[curr+1][j][0] == 0: # if target cell empty:
                                self.board[curr+1][j][0] = self.board[curr][j][0]
                                self.board[curr][j][0] = 0
                            elif self.board[curr][j][0] == self.board[curr+1][j][0] and not self.board[curr][j][1] and not self.board[curr+1][j][1]: # if target cell equal to current and neither have just been altered:
                                # combine cells
                                self.board[curr+1][j][0] = self.board[curr][j][0] + self.board[curr+1][j][0]
                                self.score += self.board[curr+1][j][0]
                                self.board[curr+1][j][1] = True
                                self.board[curr][j][0] = 0
                            curr = curr+1
                pass
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
                                self.score += self.board[i][curr-1][0]
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
                                self.score += self.board[i][curr+1][0]
                                self.board[i][curr+1][1] = True
                                self.board[i][curr][0] = 0
                            curr = curr+1
        self.set_fresh()
        self.gen_num()

    def draw(self):
        WINDOW.blit(self.surf, self.rect)
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j][0] != 0:
                    x = self.rect.x + (12*(i+1)) + (128*i)
                    y = self.rect.y + (12*(j+1)) + (128*j)
                    img = globals()[f'img{self.board[i][j][0]}']
                    WINDOW.blit(img, (x, y))

    def check_status(self):
        # check if any adjacent cells of same number (legal move available)
        # returns True if no legal moves available (game over)
        for i in range(4):
            for j in range(4-1):
                curr = self.board[i][j][0]
                if curr == self.board[i][j+1][0]:
                    return False
        for j in range(4):
            for i in range(4-1):
                curr = self.board[i][j][0]
                if curr == self.board[i+1][j][0]:
                    return False
        for i in range(4):
            for j in range(4):
                curr = self.board[i][j][0]
                if curr == 0:
                    return False
        return True

    def update_stats(self):
        n = 0 # update sum
        b = [] # update collapsed board
        for i in range(4):
            for j in range(4):
                n += self.board[i][j][0]
                b.append(self.board[i][j][0])
        self.sum = n
        self.board_collapsed = b

def main():
    ####################
    # Class References #
    ####################
    board = Board()

    #############
    # Game Loop #
    #############
    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
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
                if event.key == pygame.K_0:
                    board.reset()
                if event.key == pygame.K_a:
                    board.move("left")
                if event.key == pygame.K_d:
                    board.move("right")
                if event.key == pygame.K_w:
                    board.move("up")
                if event.key == pygame.K_s:
                    board.move("down")
        
        dispScore = font.render("Score: " +str(int(board.score)), True, BLACK)        
        dispSum = font.render("Sum: " +str(int(board.sum)), True, BLACK)        

        WINDOW.blit(dispScore, (600, 15))
        WINDOW.blit(dispSum, (600, 40))

        board.update_stats()
        board.draw()
        pygame.display.update()

if __name__ == "__main__":
    main()