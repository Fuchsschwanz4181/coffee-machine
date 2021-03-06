from coffee_machine import CoffeeMachine
import unittest


class TestCoffeeMachine(unittest.TestCase):

    def setUp(self):
        self.testMachine = CoffeeMachine()

    def test_adding_drinks(self):
        self.testMachine.add_drink("possible_drink", 100, 100, 100)
        self.testMachine.add_drink("impossible_drink", 9999, 9999, 9999)

        coffees = len(self.testMachine.available_drinks)

        self.assertEqual(coffees, 2,
                         "Something went wrong while adding drinks!")

    def test_can_brew(self):
        tested = [
            self.testMachine.can_brew(self.testMachine.available_drinks[0]),
            self.testMachine.can_brew(self.testMachine.available_drinks[1])
        ]

        expected = [True, False]

        self.assertEqual(tested, expected,
                         "Machine can't check if it is able to brew a drink!")

    def test_brewing(self):
        tested = [
            self.testMachine.brew(self.testMachine.available_drinks[0]),
            self.testMachine.brew(self.testMachine.available_drinks[1])
        ]

        expected = [
            "Beep beep! Your {} is ready!"
                .format(self.testMachine.available_drinks[0].name),
            "Not enough ingredients. Refill the machine!"
        ]
        self.assertEqual(tested, expected, "Error while brewing a drink!")

    def test_filling(self):
        self.assertEqual(self.testMachine.fill(), "Machine refilled.",
                         "Error while refilling the machine!")


if __name__ == '__main__':
    unittest.main()
