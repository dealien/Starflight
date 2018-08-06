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
        for i in range(pship.power.engines):
            engpa += '■'
        for i in range(pship.power.weapons):
            weapa += '■'
        for i in range(pship.power.shields):
            shepa += '■'
        for i in range(pship.power.auxiliary):
            auxpa += '■'
        for i in range(pship.power.reserve):
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


class Captain:
    """Ship objects contain information about a person,
    whether it's the player, an enemy, or an NPC."""

    def __init__(self, name, **kwargs):
        self.name = name
        self.credits = None
        self.reputation = {}


def save_game(name, data):
    with open('saves/' + name + '.txt', 'w') as outfile:
        json.dump(data, outfile, indent=4)


def load_game(name):
    with open('saves/' + name + '.txt') as json_file:
        data = json.load(json_file)
        pship.load(data)


def shipmenu():
    log('Switched to ship menu')
    log('Player ship status: ' + pformat(pship.dump))
    while True:
        cls()
        engpa, weapa, shepa, auxpa, respa = pship.power_display()
        print(pship.name + ' - Main Menu')
        print('')
        print('')
        print('Ship Status:')
        print('Hull      : %s%%' % pship.hull)
        print('Shields   : %s%% (%s)' % (pship.shields, pship.shieldstatus))
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
        if pship.shieldstatus is not 'Disabled':
            if pship.shieldstatus is 'Raised':
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
        elif c is 2 and pship.shieldstatus is not 'Disabled':
            pship.toggle_shields()


def powermenu():
    log('Switched to power management menu')
    log('Player ship status: ' + pformat(pship.dump))
    while True:
        cls()
        engpa, weapa, shepa, auxpa, respa = pship.power_display()
        print(pship.name + ' - Power Management')
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
            if pship.power.reserve > 0:
                pship.power.engines += 1
                pship.power.reserve -= 1
        elif c is 5:
            if pship.power.engines > 0:
                pship.power.reserve += 1
                pship.power.engines -= 1
        elif c is 2:
            if pship.power.reserve > 0:
                pship.power.weapons += 1
                pship.power.reserve -= 1
        elif c is 6:
            if pship.power.weapons > 0:
                pship.power.reserve += 1
                pship.power.weapons -= 1
        elif c is 3:
            if pship.power.reserve > 0:
                pship.power.shields += 1
                pship.power.reserve -= 1
        elif c is 7:
            if pship.power.shields > 0:
                pship.power.reserve += 1
                pship.power.shields -= 1
        elif c is 4:
            if pship.power.reserve > 0:
                pship.power.auxiliary += 1
                pship.power.reserve -= 1
        elif c is 8:
            if pship.power.auxiliary > 0:
                pship.power.reserve += 1
                pship.power.auxiliary -= 1
        elif c is 9:
            return


def stationmenu(locname):
    log('Switched to station menu')
    log('Player ship status: ' + pformat(pship.dump))
    while True:
        cls()
        print(locname + ' - Station Menu')
        print('')
        print('')
        print('Player Status:')
        print('Credits               : %s' % None)
        print('Local Reputation      : %s' % None)
        print('')
        print('Current Station:')
        print('Name                  : %s' % None)
        print('System                : %s' % None)
        print('Controlling Faction   : %s' % None)
        print('Features              : %s' % None)
        print('')
        print('Available Missions    : %s' % None)
        print('')
        print('')
        print('')
        print('1: Captain menu')
        print('2: Ship manager')
        print('3: Trading')
        print('4: Missions')

        c = 0
        try:
            c = int(msvcrt.getch())
        except ValueError:
            pass
        if c is 1:
            captainmenu()
        elif c is 2:
            shipmenu()
        elif c is 3:
            pass
        elif c is 4:
            pass


pship = Ship(username, 'Player', power=Power())
stationmenu('Ikanam Orbital Hub')
