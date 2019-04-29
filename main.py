from coffee_machine import CoffeeMachine
from drinks import drinks

machine = CoffeeMachine()

# Indicators of the maximum level of ingredients.
# Needed to make check_ingredients method give better info about ingredients.
beans_lvl = machine.beans
water_lvl = machine.water
milk_lvl = machine.milk
cups_lvl = machine.cups

def print_menu():
    print("1. Make espresso.")
    print("2. Make latte.")
    print("3. Make cappucino.")
    print("4. Check ingredients.")
    print("5. Refill machine.")
    print("6. Exit.")

def check_ingredients():
    print(f"The machine currently has\n \
            {machine.beans}\\{beans_lvl} beans,\n \
            {machine.water}\\{water_lvl} water,\n \
            {machine.milk}\\{milk_lvl} milk, and\n \
            {machine.cups}\\{cups_lvl} cups." 
    )

while True:
    print_menu()

    try:
        choice = int(input("Choose an action. "))

        if choice in range(1, 7):
            if choice == 1:
                print(machine.brew(drinks[choice-1]))
                input("Press any key to continue...")
            elif choice == 2:
                print(machine.brew(drinks[choice-1]))
                input("Press any key to continue...")
            elif choice == 3:
                print(machine.brew(drinks[choice-1]))
                input("Press any key to continue...")
            elif choice == 4:
                check_ingredients()
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