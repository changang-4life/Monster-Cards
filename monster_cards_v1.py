""" Program for a friend which creates a card catalogue for their game.
Jade Akinbo
v1 - Store Details and Main Routine Setup
"""

import easygui

catalogue = \
{
    'Blazegolem': {
        'Strength': '15',
        'Speed': '20',
        'Stealth': '23',
        'Cunning': '6'
    },

    'Dawnmirage': {
        'Strength': '5',
        'Speed': '15',
        'Stealth': '18',
        'Cunning': '22'
    },

    'Froststep': {
        'Strength': '14',
        'Speed': '14',
        'Stealth': '17',
        'Cunning': '4'
    },

    'Moldvine': {
        'Strength': '21',
        'Speed': '18',
        'Stealth': '14',
        'Cunning': '5'

    },

    'Rotthing': {
        'Strength': '16',
        'Speed': '7',
        'Stealth': '4',
        'Cunning': '12'
    },

    'Stoneling': {
        'Strength': '7',
        'Speed': '1',
        'Stealth': '25',
        'Cunning': '15'
    },

    'Vexscream': {
        'Strength': '1',
        'Speed': '6',
        'Stealth': '21',
        'Cunning': '19'
    },

    'Vortexwing': {
        'Strength': '19',
        'Speed': '13',
        'Stealth': '19',
        'Cunning': '2'
    },

    'Websnake': {
        'Strength': '7',
        'Speed': '15',
        'Stealth': '10',
        'Cunning': '5'
    },

    'Wispghoul': {
        'Strength': '17',
        'Speed': '19',
        'Stealth': '3',
        'Cunning': '2'
    }
}

def main_routine():
    easygui.buttonbox("Welcome to the Dungeons & Monsters card "
        "database\nPick an action", choices = ['Exit'])
main_routine()































