from random import randint

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return f'({self.x}, {self.y})'

class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return ('Üritad väljapoole tulistada!')

class BoardUsedException(BoardException):
    def __str__(self):
        return ('Juba tulistad siia!')

class BoardWrongShipException(BoardException):
    pass

class Ship:
    def __init__(self, bow, length, orient):
        self.bow = bow
        self.length = length
        self.orient = orient
        self.lives = length

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.length):
            cur_x = self.bow.x
            cur_y = self.bow.y
            if self.orient == 0:
                cur_x += i
            elif self.orient == 1:
                cur_y += i
            ship_dots.append(Dot(cur_x, cur_y))
        return ship_dots

    def shots(self, shot):
        return shot in self.dots

class Board:
    def __init__(self, hid = False, size = 6):
        self.size = size
        self.hid = hid
        self.count = 0
        self.field = [ ['0'] * size for _ in range(size) ]
        self.busy = []
        self.ships =[]

    def add_ship(self, ship):
        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.dots:
            self.field[d.x][d.y] = '□'
            self.busy.append(d)
        self.ships.append(ship)
        self.contour(ship)

    def contour(self, ship, verb = False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                if not(self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = '.'
                    self.busy.append(cur)

    def __str__(self):
        res = ''
        res += '  | 1 | 2 | 3 | 4 | 5 | 6 |'
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"
        if self.hid:
            res = res.replace('□', '0')
        return res

    def out(self, d):
        return not((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def shot(self, d):
        if self.out(d):
            raise BoardOutException
        if d in self.busy:
            raise BoardUsedException
        self.busy.append(d)

        for ship in self.ships:
            if ship.shots(d):
                ship.lives -= 1
                self.field[d.x][d.y] = 'X'
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb = True)
                    print('Laev hukkus! 💀')
                    return False
                else:
                    print('Laev on haavatud! 🤕')
                    return True
        self.field[d.x][d.y] = '.'
        print('Mööda ⛔')
        return False

    def begin(self):
        self.busy = []

class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy
    def ask(self):
        raise NotImplementedError
    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)

class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        print(f'Arvuti käib 🖳: {d.x + 1} {d.y + 1}')
        return d

class User(Player):
    def ask(self):
        while True:
            cords = input('Sinu käik: ').split()
            if len(cords) != 2:
                print('Sisesta 2 koordinaati! ')
                continue
            x, y = cords
            if not(x.isdigit()) or not(y.isdigit()):
                print('Sisesta arvu! ')
                continue
            x, y = int(x), int(y)
            return Dot(x - 1, y - 1)
class Game:
    def __init__(self, size = 6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid = True
        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
            return board

    def try_board(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size = self.size)
        attempts = 0
        for length in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), length, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def greet(self):
        print('***************************')
        print('      Tere tulemast')
        print('        MERELAHING')
        print('         mängule!')
        print('***************************')
        print('Sisesta 2 arvu, kus')
        print('esimene - reanumber')
        print('teine - veerunumber')

    def print_board(self):
        print('***************************')
        print('Kasutaja mängulaud:')
        print(self.us.board)
        print('***************************')
        print('Arvuti mängulaud:')
        print(self.ai.board)
        print('***************************')

    def loop(self):
        num = 0
        while True:
            self.print_board()
            if num % 2 == 0:
                print('Kasutaja käib!')
                repeat = self.us.move()
            else:
                print('Arvuri käib!')
                repeat = self.ai.move()
            if repeat:
                num -= 1
            if self.ai.board.count == 7:
                self.print_board()
                print('********************')
                print('Kasutaja võitis!')
                break
            if self.us.board.count == 7:
                self.print_board()
                print('********************')
                print('Arvuti võitis!')
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()

g = Game()
g.start()










