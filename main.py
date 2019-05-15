from coffee_machine import CoffeeMachine


def print_menu():
    """
    This function is for printing menu.

    Now it will print correct menu and options regardless
    of the number of drinks.
    It prints all "Make drink" positions, then everything
    from "options" list.
    """

    options = ["Check ingredients level.", "Refill machine.", "Exit."]

    for i in range(len(CoffeeMachine.available_drinks)):
        print(f"{i + 1}. Make {CoffeeMachine.available_drinks[i].name}.")

    for i, option in enumerate(options,
                               len(CoffeeMachine.available_drinks) + 1):
        print(f"{i}. {option}")


def main():

    machine = CoffeeMachine()

    machine.add_drink("espresso", 20, 30, 0)
    machine.add_drink("latte", 30, 180, 120)
    machine.add_drink("cappucino", 15, 120, 180)
    machine.add_drink("super strong coffee", 70, 180, 30)

    while True:
        print_menu()

        action = input("Choose an action. ")

        try:
            choice = int(action)

        except ValueError:
            print("Please input a number.")

        else:
            if 0 < choice <= len(CoffeeMachine.available_drinks):
                print(machine.brew(machine.available_drinks[choice - 1]))
                input("Press any key to continue...")
            elif choice == len(CoffeeMachine.available_drinks) + 1:
                machine.show_ingredients_lvl()
                input("Press any key to continue...")
            elif choice == len(CoffeeMachine.available_drinks) + 2:
                machine.fill()
                input("Press any key to continue...")
            elif choice == len(CoffeeMachine.available_drinks) + 3:
                print("Goodbye!")
                input("Press any key to continue...")
                break
            else:
                print("Please input correct number.")


if __name__ == '__main__':
    main()
