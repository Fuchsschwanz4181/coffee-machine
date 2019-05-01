from coffee_machine import CoffeeMachine
from drinks import drinks

import unittest

class TestCoffeeMachine(unittest.TestCase):

    def test_coffee_machine(self):
        testMachine = CoffeeMachine()

        tested = [
                    testMachine.is_full(),
                    testMachine.can_brew(drinks.get("cappucino")),
                    testMachine.can_brew(drinks.get("latte")),
                    testMachine.can_brew(drinks.get("espresso")),
                    testMachine.brew(drinks.get("cappucino")),
                    testMachine.brew(drinks.get("latte")),
                    testMachine.brew(drinks.get("espresso")),
                    testMachine.is_full(),
                    testMachine.fill(),
                    testMachine.is_full(),
                    ]

        expected = [True, True, True, True,
                    "Beep beep! Your cappucino is ready!",
                    "Beep beep! Your latte is ready!",
                    "Beep beep! Your espresso is ready!",
                    False, None, True
                    ]
                    

        self.assertEqual(tested, expected)


if __name__ == '__main__':
    unittest.main()