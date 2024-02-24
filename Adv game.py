import time

def make_choice(options):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        choice = input("Type the number corresponding to your choice: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        else:
            print("Invalid choice. Please enter a valid number.")

def enter_forest():
    print("You find yourself at the edge of an enchanted forest.")
    time.sleep(1)

    choice = make_choice(["Enter the forest cautiously", "Turn back and leave"])

    if choice == 1:
        explore_forest()
    else:
        print("You decide to turn back and leave. The adventure ends.")

def explore_forest():
    print("You enter the forest cautiously and come across a fork in the path.")
    time.sleep(1)

    choice = make_choice(["Take the left path", "Take the right path"])

    if choice == 1:
        left_path()
    else:
        right_path()

def left_path():
    print("You take the left path and find a clearing with a mystical pool.")
    time.sleep(1)

    choice = make_choice(["Approach the figure", "Ignore the figure and continue exploring"])

    if choice == 1:
        approach_figure()
    else:
        print("You ignore the figure and continue exploring.")

def approach_figure():
    print("The figure reveals itself to be a wise old wizard.")
    time.sleep(1)

    choice = make_choice(["Accept the amulet", "Decline the amulet"])

    if choice == 1:
        accept_amulet()
    else:
        decline_amulet()

def accept_amulet():
    print("The wizard gives you a magical amulet.")
    time.sleep(1)
    print("As you continue through the forest, you encounter a talking squirrel.")
    time.sleep(1)

    choice = make_choice(["Ask the squirrel for guidance", "Ignore the squirrel and forge your own path"])

    if choice == 1:
        ask_squirrel_for_guidance()
    else:
        ignore_squirrel()

def ask_squirrel_for_guidance():
    print("The squirrel warns you of a treacherous path ahead.")
    time.sleep(1)

    choice = make_choice(["Follow the squirrel's advice", "Thank the squirrel and continue on your original path"])

    if choice == 1:
        follow_squirrel_advice()
    else:
        thank_squirrel()

def follow_squirrel_advice():
    print("You avoid danger and find a hidden glade with a magical portal.")
    time.sleep(1)

    choice = make_choice(["Enter the portal", "Ignore the portal and continue exploring"])

    if choice == 1:
        enter_portal()
    else:
        ignore_portal()

def enter_portal():
    print("The portal transports you to a realm of wonders. Your adventures continue.")

if __name__ == "__main__":
    enter_forest()
