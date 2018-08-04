import os
import msvcrt
from datetime import datetime

hull = 100
shld = 100
shldstatus = 'Lowered'
engp = 3
weap = 3
shep = 3
auxp = 3
resp = 0
engpa = ''
weapa = ''
shepa = ''
auxpa = ''
respa = ''


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def log(c):
    global logfilename
    f = open(logfilename, 'a')
    f.write(str(c) + '\n')
    f.close()


createFolder('./logs/')
logfilename = './logs/' + datetime.now().strftime('log_%H_%M_%d_%m_%Y.log')
log('Log beginning ' + str(datetime.now()))


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_menu(lines, min_value, max_value):
    value = None
    while value is None:
        cls()
        for line in lines:
            print(line)
        try:
            value = int(msvcrt.getch())
            if value < min_value or value > max_value:
                value = None
        except ValueError:
            print('Please input a number')
    return value


def mainMenu():
    global engp, weap, shep, auxp, resp, engpa, weapa, shepa, auxpa, respa
    while True:
        cls()
        power_display()
        print('USS Starflight')
        print('')
        print('')
        print('Ship Status:')
        print('Hull:      %s%%' % hull)
        print('Shields:   %s%% (%s)' % (shld, shldstatus))
        print('')
        print('Power Levels:')
        print('Engines:   %s' % engpa)
        print('Weapons:   %s' % weapa)
        print('Shields:   %s' % shepa)
        print('Auxiliary: %s' % auxpa)
        print('Reserve  : %s' % respa)
        print('')
        print('1: Power settings')
        if shldstatus is not 'Disabled':
            if shldstatus is 'Raised':
                i = 'Lower'
            else:
                i = 'Raise'
            print('2: %s shields' % i)
        # TODO: Add ValueError catch to handle non-numeric keypresses
        c = int(msvcrt.getch())
        log(c)
        if c is 1:
            powerMenu()
        elif c is 2 and shldstatus is not 'Disabled':
            toggle_shields()


def power_display():
    global engp, weap, shep, auxp, resp, engpa, weapa, shepa, auxpa, respa
    engpa = ''
    weapa = ''
    shepa = ''
    auxpa = ''
    respa=''
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
        power_display()
        print('USS Starflight')
        print('')
        print('')
        print('Power Levels:')
        print('Engines:   %s' % engpa)
        print('Weapons:   %s' % weapa)
        print('Shields:   %s' % shepa)
        print('Auxiliary: %s' % auxpa)
        print('Reserve  : %s' % respa)
        print('')
        print('1: Increase power to Engines')
        print('2: Increase power to Engines')
        print('3: Increase power to Weapons')
        print('4: Increase power to Weapons')
        print('5: Increase power to Shields')
        print('6: Increase power to Shields')
        print('7: Increase power to Auxiliary')
        print('8: Increase power to Auxiliary')
        print('9: Exit menu')
        c = int(msvcrt.getch())
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
            return


mainMenu()
