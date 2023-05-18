import random

class Game:
    def __init__(self, dimension, bombs):
        self.dimension = dimension
        self.bombs = bombs
        self.bomb_loc = []
        self.dug_loc = []
        self.visible_board = [['-' for _ in range(self.dimension)] for _ in range(self.dimension)]
        self.board = self.create_board()

    def create_board(self):
        b = [[0 for _ in range(self.dimension)] for _ in range(self.dimension)]
        while self.bombs:
            x = random.randint(0, self.dimension - 1)
            y = random.randint(0, self.dimension - 1)
            if b[x][y] != -1:
                b[x][y] = -1
                self.bomb_loc.append((x, y))
                self.bombs -= 1
                for i in range(max(0, x - 1), min(self.dimension - 1, x + 2)):
                    for j in range(max(0, y - 1), min(self.dimension - 1, y + 2)):
                        if b[i][j] != -1:
                            b[i][j] += 1
        return b

    def print_board(self):
        for row in self.visible_board:
            print(' '.join(str(cell) for cell in row))

    def dig(self, x, y):
        if (x, y) in self.dug_loc:
            return 0
        if x < 0 or x >= self.dimension or y < 0 or y >= self.dimension:
            return 1
        if self.board[x][y] == -1:
            return 2

        self.dug_loc.append((x, y))
        self.visible_board[x][y] = self.board[x][y]
        if self.board[x][y] == 0:
            for i in range(max(0, x - 1), min(self.dimension - 1, x + 2)):
                for j in range(max(0, y - 1), min(self.dimension - 1, y + 2)):
                    self.dig(i, j)
        return True

    def check_win(self):
        dug_count = sum([row.count('-') for row in self.visible_board])
        return dug_count == self.dimension**2 - self.bombs

def play():
    bombs = 10
    dimension = 10
    g = Game(dimension, bombs)
    while True:
        g.print_board()
        x = int(input("Enter x coordinate: "))
        y = int(input("Enter y coordinate: "))
        if g.dig(x, y)==0:
            print("Alreadt dug dig again")
        if(g.dig(x,y)==1):
            print("Invalid Location Dig again")
        if(g.dig(x,y)==2):
            print("Game Over you dig a bomb")
            for k in g.board:
                print(k)
            break
        if g.check_win():
            print("You Win!")
            break

play()
