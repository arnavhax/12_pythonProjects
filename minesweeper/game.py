import random
class board():
    bombs=[]
    def __init__(self, size,no_of_Bombs):
        self.size = size
        self.no_of_Bombs=no_of_Bombs
    
    def populate( self):
        self.board = [['-' for x in range(self.size)] for y in range(self.size)]
        while(self.no_of_Bombs>=0):
            x = random.randint(0,self.size**2-1)
            if(x not in self.bombs):
                self.bombs.append(x)
            self.no_of_Bombs-=1
b=board(10,15)
print(b.bombs)
b.populate()
for k in b.board:
    print(k)
print(b.bombs)