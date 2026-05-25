import re
import os

class Chesspiece:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    def show_info(self):
        print(self.horizontal + str(self.vertical), self.color, self.type)

class Pawn(Chesspiece):

    def __init__(self, horizontal, vertical, color):
        super().__init__(horizontal, vertical, color)
        self.type = 'pawn'

    def move(self):
        if (self.color == 'white' and self.vertical < 8):
            if self.vertical == 2:
                while True:
                    movement = int(input('O ile pól chcesz porzuszyć tego pionka? '))
                    if movement < 3:
                        self.vertical += movement
                        break
                    else:
                        print('Możesz poruszyć tego pionka o maksymalnie 2 pola!')
            else:
                self.vertical += 1

class Rook(Chesspiece):

    def __init__(self, horizontal, vertical, color):
        super().__init__(horizontal, vertical, color)
        self.type = 'rook'

    def move(self):
        while True:
            movement_type = input('Pionowo czy poziomo? ')
            if movement_type == 'pionowo':
                movement = input('Gdzie chcesz się poruszyć? (1-8) ')
                if int(movement) < 9:
                    self.vertical = int(movement)
                    for each in horizontal:
                        for inner_each in list(range(1,3)) + list(range(7,9)):
                            if globals()[each+str(inner_each)].color != self.color and globals()[each+str(inner_each)].vertical == self.vertical and globals()[each+str(inner_each)].horizontal == self.horizontal:
                                globals()[each+str(inner_each)].vertical = 420
                    break
                else:
                    print('Nie możesz wyjść poza plansze!')
            elif movement_type == 'poziomo':
                movement = input('Gdzie chcesz się poruszyć? (a-h) ')
                if re.match(r'[a-h]', movement) is not None:
                    self.horizontal = movement
                    break
                else:
                    print('Nie możesz wyjść poza plansze!')
            else:
                print('Możesz poruszać się tylko pionowo lub poziomo')

class Knight(Chesspiece):

    def __init__(self, horizontal, vertical, color):
        super().__init__(horizontal, vertical, color)
        self.type = 'knight'

class Bishop(Chesspiece):

    def __init__(self, horizontal, vertical, color):
        super().__init__(horizontal, vertical, color)
        self.type = 'bishop'

class King(Chesspiece):

    def __init__(self, horizontal, vertical, color):
        super().__init__(horizontal, vertical, color)
        self.type = 'king'

class Queen(Chesspiece):

    def __init__(self, horizontal, vertical, color):
        super().__init__(horizontal, vertical, color)
        self.type = 'queen'

horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for each in horizontal:
    if re.match(r'a|h', each):
        globals()[each+str(1)] = Rook(each, 1, 'white')
        globals()[each+str(8)] = Rook(each, 8, 'black')
    if re.match(r'b|g', each):
        globals()[each+str(1)] = Knight(each, 1, 'white')
        globals()[each+str(8)] = Knight(each, 8, 'black')
    if re.match(r'c|f', each):
        globals()[each+str(1)] = Bishop(each, 1, 'white')
        globals()[each+str(8)] = Bishop(each, 8, 'black')
    if each == 'd':
        globals()[each+str(1)] = King(each, 1, 'white')
        globals()[each+str(8)] = King(each, 8, 'black')
    if each == 'e':
        globals()[each+str(1)] = Queen(each, 1, 'white')
        globals()[each+str(8)] = Queen(each, 8, 'black')
    globals()[each+str(2)] = Pawn(each, 2, 'white')
    globals()[each+str(7)] = Pawn(each, 7, 'black')

def show_piece_info_all():
    for each in horizontal:
        for inner_each in list(range(1,3)) + list(range(7,9)):
            globals()[each+str(inner_each)].show_info()

def print_chessboard():
    for each in range(8,0,-1):
        line = ''
        for inner_each in horizontal:
            space = '-'
            for inner_inner_each in horizontal:
                for inner_inner_inner_each in list(range(1,3)) + list(range(7,9)):
                    if (globals()[inner_inner_each+str(inner_inner_inner_each)].horizontal == inner_each and globals()[inner_inner_each+str(inner_inner_inner_each)].vertical == each):
                        if globals()[inner_inner_each+str(inner_inner_inner_each)].type == 'pawn':
                            space = 'p'
                        elif globals()[inner_inner_each+str(inner_inner_inner_each)].type == 'rook':
                            space = 'r'
                        elif globals()[inner_inner_each+str(inner_inner_inner_each)].type == 'knight':
                            space = 'k'
                        elif globals()[inner_inner_each+str(inner_inner_inner_each)].type == 'bishop':
                            space = 'b'
                        elif globals()[inner_inner_each+str(inner_inner_inner_each)].type == 'king':
                            space = 'K'
                        elif globals()[inner_inner_each+str(inner_inner_inner_each)].type == 'queen':
                            space = 'Q'
            line += space
        print(line)

os.system('cls' if os.name == 'nt' else 'clear')
print_chessboard()
while True:
    piece = input('Ktorego pionka chcesz ruszyć? (a1-h8) ')
    if re.match(r'[a-h]+[1-2]|[7-8]', piece):
        globals()[piece].move()
        os.system('cls' if os.name == 'nt' else 'clear')
        print_chessboard()
    else:
        print('Wybierz istniejącego pionka')