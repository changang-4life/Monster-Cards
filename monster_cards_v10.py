""" Program for a friend which creates a card catalogue for their game.
Jade Akinbo
v10 - Final Version
        - end user testing related changes made here (regarding print output)
        - main_routine() calling fixes
        - changed stat data type from string to int for simplicity's sake
        - more descriptive comments
        - added graphics
        - other minor fix-ups / illogical code / inconsistencies
"""

import easygui

catalogue = \
{
    'Blazegolem': {
        'Strength': 15,
        'Speed': 20,
        'Stealth': 23,
        'Cunning': 6
    },

    'Dawnmirage': {
        'Strength': 5,
        'Speed': 15,
        'Stealth': 18,
        'Cunning': 22
    },

    'Froststep': {
        'Strength': 14,
        'Speed': 14,
        'Stealth': 17,
        'Cunning': 4
    },

    'Moldvine': {
        'Strength': 21,
        'Speed': 18,
        'Stealth': 14,
        'Cunning': 5
    },

    'Rotthing': {
        'Strength': 16,
        'Speed': 7,
        'Stealth': 4,
        'Cunning': 12
    },

    'Stoneling': {
        'Strength': 7,
        'Speed': 1,
        'Stealth': 25,
        'Cunning': 15
    },

    'Vexscream': {
        'Strength': 1,
        'Speed': 6,
        'Stealth': 21,
        'Cunning': 19
    },

    'Vortexwing': {
        'Strength': 19,
        'Speed': 13,
        'Stealth': 19,
        'Cunning': 2
    },

    'Websnake': {
        'Strength': 7,
        'Speed': 15,
        'Stealth': 10,
        'Cunning': 5
    },

    'Wispghoul': {
        'Strength': 17,
        'Speed': 19,
        'Stealth': 3,
        'Cunning': 2
    }
}

def string_check(name):
    """ Only allows names with letters and spaces, must be at least 4
    characters long (excluding spaces) but not more than 15 characters long."""

    while True:
        if name is None: return None
        # if user chooses to cancel input, None is returned so parent
            # function can handle the rest
        else:
            name_stripped = name.replace(" ", "")
            if name_stripped.isalpha() and 4 <= len(name_stripped) <= 15:
            # character length checker that does not allow names under 4
                # characters and names over 15
                return name.title()
            else: # if the character length is invalid
                name = easygui.enterbox("Enter a valid name\n(Letters and"
                " spaces only, min 4 letters, max 15 letters)",
                "Invalid Name")

def add_card():
    """ Function which allows the user to add a card to the catalogue """
    while True:
        card_name = easygui.enterbox("Enter the name of your new card",
            "Card Name")
        card_name = string_check(card_name) # string error checking

        if card_name in catalogue.keys():
            # executes if the name the user enters is already on the catalogue
            add_choice = easygui.buttonbox(f"{card_name} is already on "
                "the catalogue!","Card Already on Catalogue",
                choices = ["Enter a new name", "Cancel"])
            if add_choice == "Enter a new name":
                continue
            else: break

        card_strength = easygui.integerbox("Enter the strength stat",
            "Strength Value", lowerbound = 1, upperbound = 25)
        if card_strength is None: break

        card_speed = easygui.integerbox("Enter the speed stat",
            "Speed Value", lowerbound = 1, upperbound = 25)
        if card_speed is None: break

        card_stealth = easygui.integerbox("Enter the stealth stat",
            "Stealth Value", lowerbound = 1, upperbound = 25)
        if card_stealth is None: break

        card_cunning = easygui.integerbox("Enter the cunning stat",
            "Cunning Value", lowerbound = 1, upperbound = 25)
        if card_cunning is None: break

        # ^^ allows the user to enter card strength, speed, stealth and cunning
            # stats

        new_card = { # creates new card (dictionary) for the user inputs to be
            # placed into
            'Strength': card_strength,
            'Speed': card_speed,
            'Stealth': card_stealth,
            'Cunning': card_cunning
        }

        catalogue[card_name] = new_card # adds the new card dictionary and
        # assigns its key to the name of the card the user wanted

        print(card_name + " Card")
        for key, value in new_card.items():
            print(f"    {key}: {value}") # displays card info in output

        results = "\n".join([f"  {key}: {value}" for key, value in
            new_card.items()])
        result_name = card_name + " Card"
        # ^^ formatting for easygui output

        add_choice = easygui.buttonbox("Would you like to confirm these "
            "changes?\n" + f"\n{result_name}\n {results}", "Confirmation",
            choices = ["Confirm", "Revert Changes", "Edit Card Name",
                "Edit Card Stat"])

        if add_choice == "Confirm":
            print_catalogue()
            break
        elif add_choice == "Revert Changes":
            del catalogue[card_name]
            break
        elif add_choice == "Edit Card Name":
            edit_card_name(card_name)
            break
        elif add_choice == "Edit Card Stat":
            edit_card_stat(card_name)
            break

def search_catalogue():
    """ Function for searching for an existing card within the catalogue """

    global search_choice
    while True:
        card_name = easygui.enterbox("Enter the name of the card you "
            "would like to search for", "Catalogue Search")
        card_name = string_check(card_name)

        if card_name is None: return # if the user decided to cancel on card
            # name input
        found = False # used for error checking if the card the user enters
            # is not on the catalogue
        search_term = card_name # variable reassigned to a different name
            # for simplicity

        for card, card_contents in catalogue.items():
            if card == search_term:
                print("search_catalogue(): name found")
                search_results = "\n".join([f"  {key}: {value}" for key,
                value in card_contents.items()]) # formatting for easygui

                easygui.msgbox(card_name + " Card" + "\n" +
                search_results,"Here are your search results")
                # ^^ displays search results

                search_choice = easygui.buttonbox("Would you like to edit"
                    " this card?", "Edit Searched Card", choices = [
                    "Edit Name", "Edit Stat", "Cancel"]) # gives the
                    # user the option to quickly edit the card that they
                    # searched for

                found = True # program registers that the search term is
                    # found so the if block below this for loop does not
                    # execute

                if search_choice == "Edit Name": # if edit name is chosen
                    edit_card_name(card_name)
                    break
                elif search_choice == "Edit Stat": # if edit stat is chosen
                    edit_card_stat(card_name)
                    break

        if search_choice == "Cancel": break # else, function ends if user
        # chose to cancel

        if not found: # executes if card name not found
            print("search_catalogue(): name not found")
            easygui.msgbox(f"Sorry, {card_name} could not be"
            f" found.","Not Found")

            choice = easygui.buttonbox("Would you like to enter "
                "another card to search for?", "Search Again", choices =
                ["Search for another card", "Cancel"])
                # ^^ gives the user the option to either re-enter a card or
                    # cancel

            if choice == "Search for another card": continue # if user chooses
            # to re-enter another card, function restarts
            else: break # else function end

def delete_card(card_name):
    """ Function which allows the user to delete a card from the catalogue """

    while True:
        card_name = string_check(card_name)
        if card_name in catalogue:
            print(f"\ndelete_card(): {card_name} is being deleted")
            # print check

            confirm = easygui.buttonbox("Confirm the deletion of "
                f"the {card_name} card?", "Confirm Deletion",
                choices=["Yes", "Cancel"]) # allows the user to choose
                # whether they want to confirm deletion

            if confirm == "Yes": # if they want to confirm changes
                del catalogue[card_name]
                print_catalogue()

            else: break # if the user does not want to confirm changes

        else: # executes if the card the user entered is not on the catalogue
            print(f"delete_card(): {card_name} is not on catalogue")
            delete_choice = easygui.buttonbox(f"{card_name} is not on "
                f"the catalogue.", "The card you want to delete is not"
                " on the catalogue",choices = ["Enter a new name", "Cancel"])
                # gives user the choice to either enter a new name

            if delete_choice == "Enter a new name":
                card_name = easygui.enterbox("Please enter the name of "
                    "the card you would like to delete","Delete Card")
                continue

            else: break # or exit

def print_catalogue():
    """ Function which allows the user to show the full catalogue """

    for key, value in catalogue.items():
        print(f"  {key}: {value}") # prints catalogue out to console

    full_catalogue = "\n\n".join([f"{card_name}\n" + "\n".join([f" {key}: "
        f"{value}" for key, value in card_info.items()]) for card_name,
        card_info in catalogue.items()]) # formatting for easygui

    easygui.textbox("Here is the full card catalogue",
        "Full Card Catalogue", full_catalogue)

def edit_card_name(card_name):
    while True:
        new_name = easygui.enterbox("Please enter a new name for"
          f" the {card_name} card","New Name")
        new_name = string_check(new_name)

        if new_name is None: # if user selected cancel upon input,
            break # function quits

        if new_name in catalogue.keys(): # if the name they want to change
            # their card to is already in use, program warns them
            easygui.msgbox(f"{new_name} is already in use!",
                "Card Name in Use")
            continue # loop goes back to the beginning

        confirm = easygui.buttonbox(f"Confirm changing the"
            f" {card_name} card to {new_name}",
            "Confirmation",
            choices=["OK", "Re-enter", "Cancel"]) # gives the user the option
                # to confirm, re-enter, or cancel changes

        if confirm == "OK":
            catalogue[new_name] = catalogue[card_name] # creates copy of the
            # old card they wanted to edit, but uses the new name
            del catalogue[card_name] # deletes the old card from catalogue

            results = "\n".join([f"  {key}: {value}" for key, value in
                catalogue[new_name].items()])
            result_name = new_name + " Card" # formatting for easygui

            easygui.msgbox(result_name + "\n" + results,"New Edited Card")
            # prints out changed card to user
            break
        elif confirm == "Re-enter": # if user chose to re-enter,
            continue # the loop goes back to the beginning
        else: break # if the user chose to cancel changes

def edit_card_stat(card_name):
    while True:
        stat_choice = easygui.buttonbox("Choose which stat of the "
            f"{card_name} you would like to edit", "Stat Choice",
            choices=["Strength", "Speed", "Stealth", "Cunning", "Cancel"])
            # ^^ gives the user the chance to choose which stat they would like
                # to edit, or cancel

        if stat_choice == "Cancel": break # if the user wishes to cancel

        value_choice = easygui.integerbox("Enter the value you would "
            f"like to change the {stat_choice.lower()} stat to",
            "Enter a Value", lowerbound=1, upperbound=25)

        if value_choice is None: break # if the user cancels while entering
            # a value

        old_value = catalogue[card_name][stat_choice]

        if value_choice == old_value: # if the user enters the same value
            # the stat already has, error checking loop executes
            while True:
                edit_choice = easygui.buttonbox(f"{card_name} "
                    f"{stat_choice.lower()} already has this value! Please "
                    f"enter another value", "Invalid Stat Value Entered",
                    choices = ["Re-enter", "Cancel"])

                if edit_choice == "Re-enter": # if the chooses to re-enter
                    # value
                    value_choice = easygui.integerbox("Enter the value "
                        f"you would like to change the {stat_choice.lower()} "
                        "stat to", "Enter a Value",
                         lowerbound=1, upperbound=25)

                    if value_choice != old_value: break # if user enters a
                    # valid value
                    else: continue # else error check loop restarts

                else: return # if the user chooses to cancel

        confirm = easygui.buttonbox("Confirm changing the "
            f"{stat_choice.lower()} for the {card_name} card from {old_value} "
            f"to {value_choice}?", "Confirmation",
            choices=["Confirm", "Revert Changes"]) # user can confirm or
            # revert changes made to card

        if confirm == "Confirm": # if user chooses to confirm
            catalogue[card_name][stat_choice] = value_choice # finds
            # position of value choice

            print(f"\nedit_card: changes made to {card_name} card\n")
            for key, value in catalogue[card_name].items():
                print(f"  {key}: {value}")
            # ^^ prints changes to output

            edit_result = card_name + "\n" + "\n".join([f"  {key}: {value}"
                for key, value in catalogue[card_name].items()])
            result_name = "Updated " + card_name + " Card"
            # ^^ formatting for easygui

            easygui.msgbox(edit_result, result_name)

            edit_choice = easygui.buttonbox("Would you like to make "
                "another edit with this card?",
                "Edit Again", choices = ["Edit a Stat", "Edit Name",
                "Finish"])
            # ^^ gives the user the chance to make another edit or finish

            if edit_choice == "Edit a Stat": continue
                # if user wants to make another stat edit within the card
            elif edit_choice == "Edit Name":
                # if the user wants to edit the card name
                edit_card_name(card_name)
                break
            else: break # user selects finish, function quits

def main_routine():
    """ Function which holds the main functionality of the program """

    while True:
        main_choice = easygui.buttonbox("Welcome to the Dungeons & "
            "Monsters card database\nChoose an action", "Dungeons & "
            "Monsters Card Database", choices = ['Add a Card',
            "Search for a Card", "Edit Card", "Print the Catalogue",
            "Delete (Warning)", "Exit"])
            # ^^ user can select to use one of the functions

        if main_choice == "Add a Card": # if add card is chosen, function is
            # called
            add_card()
            continue

        elif main_choice == "Search for a Card": # if search card is chosen
            if catalogue == {}: # error checker for if catalogue is empty
                easygui.msgbox("There is nothing on the catalogue yet.",
                "Empty Catalogue")
                continue

            search_catalogue() # else program calls search card function
            continue

        elif main_choice == "Delete (Warning)": # delete is chosen
            if catalogue == {}:
                easygui.msgbox("There is nothing on the catalogue yet.",
                "Empty Catalogue")
                continue

            delete_choice = easygui.buttonbox("What would you like to "
                "delete?","Delete",
                choices = ["Card", "Catalogue (Warning)", "Cancel"])
            # ^^ gives the user the choice to choose between deleting
                # catalogue, a card, or cancelling

            if delete_choice == "Catalogue (Warning)": # if user chooses to
                # wipe the  catalogue
                confirm = easygui.buttonbox("Are you sure you want to "
                    "delete the whole card catalogue?", "Confirm",
                    choices = ["Proceed","Cancel"])
                    # ^^ gives user last chance to cancel, otherwise proceed

                if confirm == "Proceed": # if user chose to proceed
                    catalogue.clear()
                    print_catalogue()
                    continue
                else: continue # if user chose to cancel instead of proceed

            elif delete_choice == "Card": # executes if user wanted to
                # delete a card
                name = easygui.enterbox("Enter the name of the card you"
                " would like to delete", "Delete Card")
                delete_card(name)
                continue

            else: continue # if user chose to cancel instead of delete an item

        elif main_choice == "Print the Catalogue": # user chooses to print
            if catalogue == {}:
                easygui.msgbox("There is nothing on the catalogue yet.",
                "Empty Catalogue")
                continue
            else:
                print_catalogue() # print function called when error check
                # successful
                continue

        elif main_choice == "Edit Card": # user chooses to edit
            if catalogue == {}:
                easygui.msgbox("There is nothing on the catalogue yet.",
                "Empty Catalogue")
                continue

            else:
                name = easygui.enterbox("Enter the name of the card you "
                "want to edit", "Card Name")
                name = string_check(name)

                if name not in catalogue.keys():
                    # checking code block below for if the card name
                    # the user entered is in the catalogue or not
                    while name not in catalogue.keys() or None == name:

                        easygui.msgbox(f"{name} is not a card on the"
                            f" catalogue!", "Invalid Name Chosen")
                            # program alerts user of error

                        print("edit card: invalid - card entered not on "
                        "catalogue\n") # print check to output

                        name = easygui.enterbox("Enter the name of the "
                            "card you want to edit", "Card Name")
                        # program makes the user enter a new card name

                        if name is None: break # check if user selected
                        # cancel while entering a new card name

                        if name in catalogue.keys(): # card name is now
                            # valid if the name they entered is in the
                            # catalogue

                            print("edit card: valid - name on catalogue ")
                            # print check to output
                        else: continue # else the while loop restarts

                if name is None: continue

                component_choice = easygui.buttonbox("Please select which"
                    f" part of the {name} card you would like to edit",
                    "Component Choice", choices=["Name", "Stat"])
                    # ^^ after the error check, program allows the user to
                        # choose whether they want to edit the card name or
                        # stat

                if component_choice == "Name":
                    edit_card_name(name)
                    continue
                else:
                    edit_card_stat(name)
                    continue
                # ^^ depending on whether the user wants to edit the card
                    # name or a stat, the corresponding function is called

main_routine()