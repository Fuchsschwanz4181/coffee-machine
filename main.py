from coffee_machine import CoffeeMachine


def print_menu():

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

            for i in range(len(CoffeeMachine.available_drinks)):
                if choice == i + 1:
                    print(machine.brew(machine.available_drinks[i]))
                    input("Press any key to continue...")
                    break

            if choice == len(CoffeeMachine.available_drinks) + 1:
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

        except ValueError:
            print("Please input a number.")


if __name__ == '__main__':
    main()
