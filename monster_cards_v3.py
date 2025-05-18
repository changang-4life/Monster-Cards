""" Program for a friend which creates a card catalogue for their game.
Jade Akinbo
v3 - search_catalogue()
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

def search_catalogue(card_name):
    """ Function for searching for an existing card within the catalogue """
    while True:
        found = False
        search_term = card_name.title()
        for card, card_contents in catalogue.items():
            if card == search_term:
                print("search_card(): name found")
                search_results = "\n".join([f"  {key}: {value}" for key,
                value in card_contents.items()])

                easygui.msgbox(card_name.title() + " Card" + "\n" +
                search_results,"Here are your search results")
                found = True

                break  # Exit the loop once found
        if not found:
            print("search_card(): name not found")
            easygui.msgbox(f"Sorry, {card_name.title()} could not be"
            f" found.","Not Found")
            break
        else:
            main_routine()
            break

def main_routine():
    choice = easygui.buttonbox("Welcome to the Dungeons & Monsters card "
        "database\nChoose an action", "Dungeons & Monsters Card Database",
        choices = ['Add a Card', 'Search for a Card', 'Exit'])

    if choice == 'Add a Card':
        add_card()
        main_routine()

    elif choice == 'Search for a Card':
        name = easygui.enterbox("Enter the name of the card you would like "
            "to search for", "Catalogue Search")
        search_catalogue(name.title())
        main_routine()

    else: quit()

main_routine()































