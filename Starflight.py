import console
import os

hull = 100
shld = 100
shldstatus = 'Lowered'
engp = 3
weap = 3
shep = 3
auxp = 3
lines = []
engpa = ''
weapa = ''
shepa = ''
auxpa = ''


def print_menu(lines, min_value, max_value):
    value = None
    while value is None:
        for line in lines:
            print(line)
        try:
            value = int(input(': '))
            if value < min_value or value > max_value:
                value = None
        except ValueError:
            print('Please input a number')
    return value


def menuMain():
    global engp, weap, shep, auxp, engpa, weapa, shepa, auxpa
    while True:
        console.clear()
        lines = []
        engpa = ''
        weapa = ''
        shepa = ''
        auxpa = ''
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
            menuPower()
        if c is 2:
            toggle_shields()


def power_display():
    global engp, weap, shep, auxp, engpa, weapa, shepa, auxpa
    for i in range(engp):
        engpa += '■'
    for i in range(weap):
        weapa += '■'
    for i in range(shep):
        shepa += '■'
    for i in range(auxp):
        auxpa += '■'


def toggle_shields():
    global shldstatus
    if shldstatus is 'Raised':
        shldstatus = 'Lowered'
    else:
        shldstatus = 'Raised'


menuMain()
