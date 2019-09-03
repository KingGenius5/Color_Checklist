#This is a really useful module and will be helpful for the MadLibs project (stretch challenge)
from termcolor import colored
import random

checklist = []

def color_picker():
    color_list = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
    return random.choice(color_list)

def create(item):
    checklist.append(colored(item, color_picker()))

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = colored(item, color_picker())
    print(checklist)

def destroy(index):
    checklist.pop(index)
    return checklist

def mark_completed(index):
    placeholder = checklist[index]
    checklist[index]= "√"+ placeholder
    return checklist

def mark_notcompleted(index):
    placeholder = checklist[index]
    checklist[index]= placeholder[1:len(placeholder)]
    return checklist

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def select(inputted_letter):
    # Create item
    if inputted_letter == "a":#create item code here
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif inputted_letter == "r":#read code here
        item_index = int(user_input("Index Number: "))
        print("\n" + read(item_index))

    #This lists all the items, as the function states
    elif inputted_letter == "l":
        list_all_items()

    # Update item
    elif inputted_letter == "u":#update code here
        item_index = int(user_input("Index Number: "))
        update_item = user_input("Input item: ")
        print(update(item_index, update_item))

    # Destroy item
    elif inputted_letter == "d":#destroy code here
        item_index = int(user_input("Index Number: "))
        print(destroy(item_index))

    # Mark Complete/Incomplete
    elif inputted_letter == "m":
        complete_incomplete = user_input("Mark as Complete or Incomplete?(Enter C/I): ").upper()

        if complete_incomplete == "c":
            item_index = int(user_input("Index Number: "))
            print(mark_completed(item_index))

        elif complete_incomplete == "i":
            item_index = int(user_input("Index Number: "))
            print(mark_notcompleted(item_index))

        else:
            print("Invalid Option")

    elif inputted_letter == "q":#for quitting
        return False

    #For all other options not available
    else:
        print("That's not one of the available options! Try Again!")
        return False

    return True

def test():#add testing code here
    create("Batmobile")
    create("Batarang")

    print(read(0))
    print(read(1))

    update(0, "Batmobile")
    destroy(1)
    print(read(0))
    list_all_items()
test()

running = True
while running:
    selection = user_input(
        "Press A to Add to list, R to Read from list, L to Display list, U to Update item, D to Destroy item, M to Mark as Complete/Incomplete, and Q to quit: ")
    selection_both_cases = selection.lower()
    running = select(selection_both_cases)
