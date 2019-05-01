from coffee_machine import CoffeeMachine
from drinks import drinks

def print_menu():
    print("1. Make espresso.")
    print("2. Make latte.")
    print("3. Make cappucino.")
    print("4. Check ingredients.")
    print("5. Refill machine.")
    print("6. Exit.")

def main():

    machine = CoffeeMachine()

    while True:
        print_menu()

        action = input("Choose an action. ")

        try:
            choice = int(action)

            if choice in range(1, 7):
                if choice == 1:
                    print(machine.brew(drinks.get('espresso')))
                    input("Press any key to continue...")
                elif choice == 2:
                    print(machine.brew(drinks.get('latte')))
                    input("Press any key to continue...")
                elif choice == 3:
                    print(machine.brew(drinks.get('cappucino')))
                    input("Press any key to continue...")
                elif choice == 4:
                    machine.check_ingredients()
                    input("Press any key to continue...")
                elif choice == 5:
                    machine.fill()
                    input("Press any key to continue...")
                elif choice == 6:
                    print("Goodbye!")
                    input("Press any key to continue...")
                    break
            else:
                print("Please try again.")

        except ValueError:
            print("Please try again.")

if __name__=='__main__':
    main()
