class CoffeeMachine:
    def __init__(self):
        self.beans = 300
        self.water = 2000
        self.milk = 1000
        self.cups = 50

    # This method returns True 
    # if all variables are equal to corresponding numbers.
    # It's like logical expression.
    def is_full(self):
        return(
            self.beans == 300
            and self.water == 2000
            and self.milk == 1000
            and self.cups == 50
        )

    
    def fill(self):
        # If the machine is full (is_full() returns True), 
        # then we will see this message.
        if self.is_full():
            print("The machine is already full!")
        else:
            self.beans = 300
            self.water = 2000
            self.milk = 1000
            self.cups = 50
            print("Machine refilled.")

    
    def can_brew(self, drink):
        # This method returns True 
        # if the machine can brew drink of your choice.
        return (
            self.beans >= drink["beans"]
            and self.water >= drink["water"]
            and self.milk >= drink["milk"]
            and self.cups > 0
        )

    
    def brew(self, drink):
        if self.can_brew(drink):
            print("Brewing...")
            self.beans -= drink["beans"]
            self.water -= drink["water"]
            self.milk -= drink["milk"]
            self.cups -= 1
            return "Beep beep! Your {} is ready!".format(drink["name"])
        else:
            return "Not enough ingredients. Refill the machine!"