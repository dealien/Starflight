import os

hull = 100
shld = 100
shldstatus = 'Lowered'
engp = 3
weap = 3
shep = 3
auxp = 3
resp = 0
lines = []
engpa = ''
weapa = ''
shepa = ''
auxpa = ''
respa = ''


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_menu(lines, min_value, max_value):
    value = None
    while value is None:
        cls()
        for line in lines:
            print(line)
        try:
            value = int(input(': '))
            if value < min_value or value > max_value:
                value = None
        except ValueError:
            print('Please input a number')
    return value


def mainMenu():
    global engp, weap, shep, auxp, resp, engpa, weapa, shepa, auxpa, respa
    while True:
        cls()
        lines = []
        engpa = ''
        weapa = ''
        shepa = ''
        auxpa = ''
        respa = ''
        power_display()
        lines.append('USS Starflight')
        lines.append('')
        lines.append('')
        lines.append('Ship Status:')
        lines.append('Hull:      %s%%' % hull)
        lines.append('Shields:   %s%% (%s)' % (shld, shldstatus))
        lines.append('')
        lines.append('Power Levels:')
        lines.append('Engines:   %s' % engpa)
        lines.append('Weapons:   %s' % weapa)
        lines.append('Shields:   %s' % shepa)
        lines.append('Auxiliary: %s' % auxpa)
        lines.append('Reserve  : %s' % respa)
        lines.append('')
        lines.append('1: Power settings')
        if shldstatus is not 'Disabled':
            if shldstatus is 'Raised':
                i = 'Lower'
            else:
                i = 'Raise'
            lines.append('2: %s shields' % i)
        if shldstatus is not 'Disabled':
            c = print_menu(lines, 1, 2)
        else:
            c = print_menu(lines, 1, 1)
        if c is 1:
            powerMenu()
        elif c is 2:
            toggle_shields()


def power_display():
    global engp, weap, shep, auxp, resp, engpa, weapa, shepa, auxpa, respa
    for i in range(engp):
        engpa += '■'
    for i in range(weap):
        weapa += '■'
    for i in range(shep):
        shepa += '■'
    for i in range(auxp):
        auxpa += '■'
    for i in range(resp):
        respa += '■'


def toggle_shields():
    global shldstatus
    if shldstatus is 'Raised':
        shldstatus = 'Lowered'
    else:
        shldstatus = 'Raised'


def powerMenu():
    global engp, weap, shep, auxp, resp, engpa, weapa, shepa, auxpa, respa
    while True:
        cls()
        lines = []
        engpa = ''
        weapa = ''
        shepa = ''
        auxpa = ''
        power_display()
        lines.append('USS Starflight')
        lines.append('')
        lines.append('')
        lines.append('Power Levels:')
        lines.append('Engines:   %s' % engpa)
        lines.append('Weapons:   %s' % weapa)
        lines.append('Shields:   %s' % shepa)
        lines.append('Auxiliary: %s' % auxpa)
        lines.append('Reserve  : %s' % respa)
        lines.append('')
        lines.append('1: Increase power to Engines')
        lines.append('2: Increase power to Engines')
        lines.append('3: Increase power to Weapons')
        lines.append('4: Increase power to Weapons')
        lines.append('5: Increase power to Shields')
        lines.append('6: Increase power to Shields')
        lines.append('7: Increase power to Auxiliary')
        lines.append('8: Increase power to Auxiliary')
        lines.append('9: Exit menu')
        c = print_menu(lines, 1, 8)
        if c is 1:
            if resp > 0:
                engp += 1
                resp -= 1
        elif c is 2:
            if engp > 0:
                resp += 1
                engp -= 1
        elif c is 3:
            if resp > 0:
                weap += 1
                resp -= 1
        elif c is 4:
            if weap > 0:
                resp += 1
                weap -= 1
        elif c is 5:
            if resp > 0:
                shep += 1
                resp -= 1
        elif c is 6:
            if shep > 0:
                resp += 1
                shep -= 1
        elif c is 7:
            if resp > 0:
                auxp += 1
                resp -= 1
        elif c is 8:
            if auxp > 0:
                resp += 1
                auxp -= 1
        elif c is 9:
            return True


mainMenu()
