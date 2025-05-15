""" Program for a friend which creates a card catalogue for their game.
Jade Akinbo
v2 - add_card()
    - upperbound, lowerbound functionality
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

def add_card():
    card_name = easygui.enterbox("Enter the name for your new card",
        "Card Name")
    card_name = card_name.title()
    card_strength = easygui.integerbox("Enter the strength stat",
        "Strength Value", lowerbound = 1, upperbound = 25)
    card_speed = easygui.integerbox("Enter the speed stat",
        "Speed Value", lowerbound = 1, upperbound = 25)
    card_stealth = easygui.integerbox("Enter the stealth stat",
        "Stealth Value", lowerbound = 1, upperbound = 25)
    card_cunning = easygui.integerbox("Enter the cunning stat",
        "Cunning Value", lowerbound = 1, upperbound = 25)

    new_card = {
        'Strength': str(card_strength),
        'Speed': str(card_speed),
        'Stealth': str(card_stealth),
        'Cunning': str(card_cunning)
    }

    catalogue[card_name] = new_card

    print(card_name + " Card")
    for key, value in new_card.items():
        print(f"    {key}: {value}")

    results = "\n".join([f"  {key}: {value}" for key, value in
        new_card.items()])

    result_name = card_name.title() + " Card"

    easygui.msgbox(result_name + "\n" + results,
        "Card Successfully Added!")

def main_routine():
    choice = easygui.buttonbox("Welcome to the Dungeons & Monsters card "
        "database.\n\nChoose an action", choices = ['Add a Card', 'Exit'])

    if choice == 'Add a Card':
        add_card()
        main_routine()

    else: quit()

main_routine()































