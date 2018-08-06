import json
import msvcrt
import os
from datetime import datetime
from pprint import pformat

username = 'USS Starflight'


def createfolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def log(c):
    logfilename = './logs/' + datetime.now().strftime('log_%H_%M_%d_%m_%Y.log')
    f = open(logfilename, 'a')
    f.write(str(c) + '\n')
    f.close()


createfolder('./logs/')
createfolder('./saves/')
log('Log beginning ' + str(datetime.now()))


def cls():
    # os.system('cls' if os.name == 'nt' else 'clear')
    print('\n' * 20)


class Power:
    def __init__(self, **kwargs):
        self.engines = 3
        self.weapons = 3
        self.shields = 3
        self.auxiliary = 3
        self.reserve = 3


class Ship:
    """Ship objects contain information about a ship,
    whether it's the player, an enemy, or an NPC."""

    def __init__(self, name, owner, **kwargs):
        self.name = str(name)
        self.model = None
        self.owner = str(owner)
        self.hull = 100
        self.shields = 100
        self.power = Power()
        self.shieldstatus = 'Lowered'

    def toggle_shields(self):
        if self.shieldstatus is 'Raised':
            self.shieldstatus = 'Lowered'
        else:
            self.shieldstatus = 'Raised'

    def power_display(self):
        engpa = ''
        weapa = ''
        shepa = ''
        auxpa = ''
        respa = ''
        for i in range(pShip.power.engines):
            engpa += '■'
        for i in range(pShip.power.weapons):
            weapa += '■'
        for i in range(pShip.power.shields):
            shepa += '■'
        for i in range(pShip.power.auxiliary):
            auxpa += '■'
        for i in range(pShip.power.reserve):
            respa += '■'
        return engpa, weapa, shepa, auxpa, respa

    @property
    def dump(self):
        return {
            'name': self.name,
            'model': self.model,
            'owner': self.owner,
            'hull': self.hull,
            'shields': self.shields,
            'power': self.power.__dict__,
            'shieldstatus': self.shieldstatus
        }

    def load(self, data):
        self.name = data['name']
        self.model = data['model']
        self.owner = data['owner']
        self.hull = data['hull']
        self.shields = data['shields']
        self.power.engines = 3
        self.power.weapons = 3
        self.power.shields = 3
        self.power.auxiliary = 3
        self.power.reserve = 3
        self.shieldstatus = data['shieldstatus']


def save_game(name, data):
    with open('saves/' + name + '.txt', 'w') as outfile:
        json.dump(data, outfile)


def load_game(name):
    with open('saves/' + name + '.txt') as json_file:
        data = json.load(json_file)
        pShip.load(data)


def mainmenu():
    log('Switched to main menu')
    log('Player ship status: ' + pformat(pShip))
    while True:
        cls()
        engpa, weapa, shepa, auxpa, respa = pShip.power_display()
        print(pShip.name + ' - Main Menu')
        print('')
        print('')
        print('Ship Status:')
        print('Hull:      %s%%' % pShip.hull)
        print('Shields:   %s%% (%s)' % (pShip.shields, pShip.shieldstatus))
        print('')
        print('Power Levels:')
        print('Engines   : %s' % engpa)
        print('Weapons   : %s' % weapa)
        print('Shields   : %s' % shepa)
        print('Auxiliary : %s' % auxpa)
        print('')
        print('Reserve   : %s' % respa)
        print('')
        print('')
        print('')
        print('1: Power settings')
        if pShip.shieldstatus is not 'Disabled':
            if pShip.shieldstatus is 'Raised':
                i = 'Lower'
            else:
                i = 'Raise'
            print('2: %s shields' % i)

        c = 0
        try:
            c = int(msvcrt.getch())
        except ValueError:
            pass
        if c is 1:
            powermenu()
        elif c is 2 and pShip.shieldstatus is not 'Disabled':
            pShip.toggle_shields()


def powermenu():
    log('Switched to power management menu')
    log('Player ship status: ' + pformat(pShip))
    while True:
        cls()
        engpa, weapa, shepa, auxpa, respa = pShip.power_display()
        print(pShip.name + ' - Power Management')
        print('')
        print('')
        print('Power Levels:')
        print('Engines   : %s' % engpa)
        print('Weapons   : %s' % weapa)
        print('Shields   : %s' % shepa)
        print('Auxiliary : %s' % auxpa)
        print('')
        print('Reserve   : %s' % respa)
        print('')
        print('')
        print('')
        print('1: Increase power to Engines')
        print('2: Increase power to Weapons')
        print('3: Increase power to Shields')
        print('4: Increase power to Auxiliary')
        print('')
        print('5: Decrease power to Engines')
        print('6: Decrease power to Weapons')
        print('7: Decrease power to Shields')
        print('8: Decrease power to Auxiliary')
        print('')
        print('9: Exit menu')

        c = 0
        try:
            c = int(msvcrt.getch())
        except ValueError:
            pass

        if c is 1:
            if pShip.power.reserve > 0:
                pShip.power.engines += 1
                pShip.power.reserve -= 1
        elif c is 5:
            if pShip.power.engines > 0:
                pShip.power.reserve += 1
                pShip.power.engines -= 1
        elif c is 2:
            if pShip.power.reserve > 0:
                pShip.power.weapons += 1
                pShip.power.reserve -= 1
        elif c is 6:
            if pShip.power.weapons > 0:
                pShip.power.reserve += 1
                pShip.power.weapons -= 1
        elif c is 3:
            if pShip.power.reserve > 0:
                pShip.power.shields += 1
                pShip.power.reserve -= 1
        elif c is 7:
            if pShip.power.shields > 0:
                pShip.power.reserve += 1
                pShip.power.shields -= 1
        elif c is 4:
            if pShip.power.reserve > 0:
                pShip.power.auxiliary += 1
                pShip.power.reserve -= 1
        elif c is 8:
            if pShip.power.auxiliary > 0:
                pShip.power.reserve += 1
                pShip.power.auxiliary -= 1
        elif c is 9:
            return


p = Power()
pShip = Ship('USS Starflight', 'Player', power=p)
print(pShip.dump)
save_game(username, pShip.dump)
load_game(username)
print(pShip.dump)
mainmenu()
