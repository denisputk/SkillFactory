def greet():
    print('********************')
    print('   Tere tulemast')
    print('  trips-traps-trull')
    print('       mängule!')
    print('********************')
    print('Sisesta 2 arvu, kus')
    print('esimene - reanumber')
    print('teine - veerunumber')

def show():
    print()
    print('  | 0 | 1 | 2 |')
    print('---------------')
    for i, row in enumerate(field):
        row_str = f"{i} | {' | '. join(row)} |"
        print(row_str)
        print('---------------')

def ask():
    while True:
        cords = input('    Teie käik: \n').split()
        if len(cords) != 2:
            print('Sisesta 2 arvu!')
            continue
        x, y = cords
        if not(x.isdigit()) or not(y.isdigit()):
            print('Sisesta arve!')
            continue
        x, y = int(x), int(y)
        if 0 > x > 2 or 0 > y > 2:
            print('Vale arve!')
            continue
        if field[x][y] != ' ':
            print('Siin on kinni!')
            continue
        return x, y

def check_win():
    win_cord = [((0, 0), (0, 1), (0, 2)),
                ((1, 0), (1, 1), (1, 2)),
                ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)),
                ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)),
                ((0, 2), (1, 2), (2, 2))]
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ['X', 'X', 'X']:
            print('Rist võitis!')
            return True
        if symbols == ['0', '0', '0']:
            print('Ring võitis!')
            return True
    return False

greet()
field = [[' '] * 3 for i in range(3)]
num = 0
while True:
    num += 1
    show()
    if num % 2 == 1:
        print('Risti käib...')
    else:
        print('Ringi käib...')

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if check_win():
        show()
        break

    if num == 9:
        print('Viik!')
        show()
        break

print('********************')
print('  Mäng on lõppenud! ')
print('********************')