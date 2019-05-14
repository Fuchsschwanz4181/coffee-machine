from drinks import Drinks


class CoffeeMachine:
    COFFEE_BEANS = 300
    WATER_AMOUNT = 2000
    MILK_AMOUNT = 1000
    CUPS_AMOUNT = 50

    available_drinks = []

    def __init__(self):
        self.beans = self.COFFEE_BEANS
        self.water = self.WATER_AMOUNT
        self.milk = self.MILK_AMOUNT
        self.cups = self.CUPS_AMOUNT

    def add_drink(self, drink_name, beans_cost, water_cost, milk_cost):
        """
        This method adds a drink to the list of available drinks.

        Method creates an Drinks class object and adds it to the list.
        """
        self.available_drinks.append(Drinks(drink_name,
                                            beans_cost,
                                            water_cost,
                                            milk_cost
                                            ))

    def fill(self):
        """
        This method refills the machine if it's not full.

        Method checks if the machine is full,
        and either fill it and show proper message,
        or inform user that the machine is full.
        """

        self.beans = self.COFFEE_BEANS
        self.water = self.WATER_AMOUNT
        self.milk = self.MILK_AMOUNT
        self.cups = self.CUPS_AMOUNT
        return "Machine refilled."

    def show_ingredients_lvl(self):
        """This method shows amount of ingredients in the machine."""

        print(f"The machine currently has\n \
            {self.beans}/{self.COFFEE_BEANS} beans,\n \
            {self.water}/{self.WATER_AMOUNT} water,\n \
            {self.milk}/{self.MILK_AMOUNT} milk, and\n \
            {self.cups}/{self.CUPS_AMOUNT} cups."
              )

    def can_brew(self, drink):
        """
        This method checks if the machine can make your drink.

        Method checks if the machine has enough ingredients to brew
        a drink of your choice and returns True if so.
        """

        return (
                self.beans >= drink.coffee_beans
                and self.water >= drink.water
                and self.milk >= drink.milk
                and self.cups > 0
        )

    def brew(self, drink):
        """
        This method brews chosen drink if the machine is able to do so.

        Method checks if all the requirements are met.
        If so, the machine will brew your coffee and return message
        informing you that drink is ready. 

        If not, the machine will just return proper message
        informing you about it.
        """

        if self.can_brew(drink):
            print("Brewing...")
            self.beans -= drink.coffee_beans
            self.water -= drink.water
            self.milk -= drink.milk
            self.cups -= 1
            return "Beep beep! Your {} is ready!".format(drink.name)
        else:
            return "Not enough ingredients. Refill the machine!"
