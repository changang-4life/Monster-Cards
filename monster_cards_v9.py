""" Program for a friend which creates a card catalogue for their game.
Jade Akinbo
v9  - trialling: delete_card()
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

def string_check(name):
    """ Only allows names with letters and spaces, must be at least 4
    characters long (excluding spaces) but not more than 30 characters long."""

    while True:
        if name is None: # executes if user hits cancel while string checking
            main_routine() # goes back to start screen
            break
        else:
            name_stripped = name.replace(" ", "")
            if name_stripped.isalpha() and 4 <= len(name_stripped) <= 15:
                # character length checker that does not allow names under 4
                    # characters and names over 15
                return name.title()
            else:
                name = easygui.enterbox("Enter a valid name\n(Letters and"
                " spaces only, min 4 letters, max 15 letters)",
                "Invalid Name")

def add_card():
    """ Function which allows the user to add a card to the catalogue """

    card_name = easygui.enterbox("Enter the name of your new card",
        "Card Name")
    card_name = string_check(card_name) # string error checking

    if card_name in catalogue.keys():
        # executes if the name the user enters is not on the catalogue
        choice = easygui.buttonbox(f"{card_name} is already on the "
            f"catalogue!","Card Already on Catalogue",
            choices = ["Enter a new name", "Cancel"])
        if choice == "Enter a new name":
            add_card()
            main_routine()
        else:
            main_routine()

    card_strength = easygui.integerbox("Enter the strength stat",
        "Strength Value", lowerbound = 1, upperbound = 25)
    if card_strength is None:
        main_routine()
    card_speed = easygui.integerbox("Enter the speed stat",
        "Speed Value", lowerbound = 1, upperbound = 25)
    if card_speed is None:
        main_routine()
    card_stealth = easygui.integerbox("Enter the stealth stat",
        "Stealth Value", lowerbound = 1, upperbound = 25)
    if card_stealth is None:
        main_routine()
    card_cunning = easygui.integerbox("Enter the cunning stat",
        "Cunning Value", lowerbound = 1, upperbound = 25)
    if card_cunning is None:
        main_routine()

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

def search_catalogue():
    """ Function for searching for an existing card within the catalogue """
    card_name = easygui.enterbox("Enter the name of the card you would "
        "like to search for", "Catalogue Search")
    card_name = string_check(card_name)
    while True:
        found = False
        search_term = card_name.title()
        for card, card_contents in catalogue.items():
            if card == search_term:
                print("search_catalogue(): name found")
                search_results = "\n".join([f"  {key}: {value}" for key,
                value in card_contents.items()])

                easygui.msgbox(card_name.title() + " Card" + "\n" +
                search_results,"Here are your search results")
                found = True

                break  # Exit the loop once found
        if not found:
            print("search_catalogue(): name not found")
            easygui.msgbox(f"Sorry, {card_name.title()} could not be"
            f" found.","Not Found")
            break
        else:
            main_routine()
            break

def delete_card(card_name):
    """ Function which allows the user to delete a card from the catalogue """
    card_name = string_check(card_name)
    if card_name in catalogue:
        print(f"\ndelete_card(): {card_name} is being deleted")
        # print check
        confirm = easygui.buttonbox("Confirm the deletion of "
            f"the {card_name.title()} card?", "Confirm Deletion",
                choices=["Yes", "Cancel"])

        if confirm == "Yes":
            del catalogue[card_name]

            full_list = "\n\n".join([card_name + " Card\n" + "\n".join([
                f"  {key}: {value}" for key, value in card_info.items()])
                for card, card_info in catalogue.items()])

            easygui.msgbox("Here is the new catalogue\n\n" + full_list,
                "Updated Catalogue")
        else: return

    else:
        print(f"delete_card(): {card_name} is not on catalogue")
        choice = easygui.buttonbox(f"{card_name.title()} is not on "
            f"the catalogue.", "The card you want to delete is not"
            " on the catalogue",choices = ["Enter a new name", "Cancel"])

        if choice == "Enter a new name":
            card_name = easygui.enterbox("Please enter the name of "
                "the card you would like to delete","Delete Card")
            delete_card(card_name)
        else: return

def print_catalogue():
    """ Function which allows the user to show the full catalogue """

    for key, value in catalogue.items():
        print(f"  {key}: {value}")

    full_catalogue = "\n\n".join(
        [f"{card_name}\n" + "\n".join(
        [f" {key}: {value}" for key, value in card_info.items()])
         for card_name, card_info in catalogue.items()])

    easygui.msgbox(full_catalogue, "Full Card Catalogue")

def edit_card_name(card_name):
    while True:
        new_name = easygui.enterbox("Please enter a new name for"
          f" the {card_name.title()} card","New Name")
        new_name = string_check(new_name)

        if new_name in catalogue.keys():
            easygui.msgbox(f"{new_name} is already in use!",
                "Card Name in Use")
            continue

        confirm = easygui.buttonbox(f"Confirm changing the"
            f" {card_name.title()} card to {new_name}",
            "Confirmation",
            choices=["OK", "Re-enter","Cancel"])

        if confirm == "OK":
            catalogue[new_name] = catalogue[card_name]
            del catalogue[card_name]
            break
        elif confirm == "Re-enter":
            continue
        else:
            break

def edit_card_stat(card_name):
    global old_value
    while True:
        stat_choice = easygui.buttonbox("Choose which stat of the "
            f"{card_name} you would like to edit", "Stat Choice",
            choices=["Strength", "Speed", "Stealth", "Cunning"])

        value_input = easygui.integerbox("Enter the value you would "
            f"like to change the {stat_choice.lower()} stat to",
            "Enter a Value", lowerbound=1, upperbound=25)

        if value_input is None:
            break

        og_card = catalogue[card_name]
        items = list(og_card.items())

        if stat_choice == "Strength":
            old_value = items[0][1]
        elif stat_choice == "Speed":
            old_value = items[1][1]
        elif stat_choice == "Stealth":
            old_value = items[2][1]
        elif stat_choice == "Cunning":
            old_value = items[3][1]

        updated_card = {}

        items_list = []
        for key, value in og_card.items():
            items_list.append(key)
            items_list.append(value)

        for key, value in og_card.items():
            if key == stat_choice and value == old_value:
                print(f"key: {key}")
                print(f"old value: {value}")  # print checks

                updated_card[key] = value_input  # notes: instead of
                # th, the new main course
                # name
                # is added, along with its regular value/price
            else:
                updated_card[key] = value
                # key value pair that the iteration is up to gets added as
                # normal to the empty updated_card dictionary

        confirm = easygui.buttonbox("Confirm changing the "
            f"{stat_choice.lower()} for the {card_name} card from {old_value} "
            f"to {value_input}?", "Confirmation",
            choices=["Confirm", "Revert Changes"])

        if confirm == "Confirm":
            updated_card[stat_choice] = value_input
            catalogue[card_name] = updated_card

            print(f"\nedit_card: changes made to {card_name} card\n")
            for key, value in updated_card.items():
                print(f"  {key}: {value}")

            edit_result = card_name + "\n" + "\n".join([f"  {key}: {value}"
                for key, value in updated_card.items()])
            result_name = "Updated " + card_name.title() + " Card"

            easygui.msgbox(edit_result, result_name)
            break
        else:
            break

def main_routine():
    choice = easygui.buttonbox("Welcome to the Dungeons & Monsters card "
        "database\nChoose an action", "Dungeons & Monsters Card Database",
        choices = ['Add a Card', 'Search for a Card',
        'Edit Card', 'Print the Catalogue', 'Delete (Warning)', 'Exit'])

    if choice == 'Add a Card':
        add_card()
        main_routine()

    elif choice == 'Search for a Card':
        if catalogue == {}:
            easygui.msgbox("There is nothing on the catalogue yet.",
            "Empty Catalogue")
            main_routine()
        search_catalogue()
        main_routine()

    elif choice == 'Delete (Warning)':
        if catalogue == {}:
            easygui.msgbox("There is nothing on the catalogue yet.",
            "Empty Catalogue")
            main_routine()

        delete_choice = easygui.buttonbox("What would you like to delete?"
            ,"Delete", choices = ["Card", "Catalogue (Warning)",
            "Cancel"])

        if delete_choice == "Catalogue (Warning)":
            confirm = easygui.buttonbox("Are you sure you want to delete "
                "the whole card catalogue?", "Confirm",
                choices = ["Proceed","Cancel"])

            if confirm == "Proceed":
                catalogue.clear()
                main_routine()
            else: main_routine()

        elif delete_choice == "Card":
            name = easygui.enterbox("Enter the name of the card you would"
                " like to delete", "Delete Card")
            delete_card(name)
            main_routine()

        else: main_routine()

    elif choice == 'Print the Catalogue':
        if catalogue == {}:
            easygui.msgbox("There is nothing on the catalogue yet.",
            "Empty Catalogue")
            main_routine()
        else:
            print_catalogue()
            main_routine()

    elif choice == 'Edit Card':
        if catalogue == {}:
            easygui.msgbox("There is nothing on the catalogue yet.",
            "Empty Catalogue")
            main_routine()

        else:
            name = easygui.enterbox("Enter the name of the card you "
            "want to edit", "Card Name")
            name = string_check(name)
            if name not in catalogue.keys():
                while (name.title() not in catalogue.keys() or None
                       == name):
                    """ Loop to check whether the name the user chose 
                    for their new card is already on the catalogue """

                    card_name = name.title()

                    easygui.msgbox(f"{card_name} is not a card on the"
                        f" catalogue!", "Invalid Name Chosen")
                    print(
                        "edit card: invalid - card entered not on catalogue\n")
                    # print check

                    name = easygui.enterbox("Enter the name of the card"
                        " you want to edit", "Card Name")

                    if name is None:
                        main_routine()
                    name = name.title()

                    if name in catalogue.keys():
                        print("edit card: valid - name on catalogue ")
                        # print check
                        name = name.title()
                    else:
                        continue

            component_choice = easygui.buttonbox("Please select which "
                f"part of the {name.title()} card you would like to edit",
                "Component Choice", choices=["Name", "Stat"])

            if component_choice == "Name":
                edit_card_name(name)
            else:
                edit_card_stat(name)

            main_routine()

    else: quit()

main_routine()