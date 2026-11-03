import unittest
from game import advance, new_game
from reference_calculator import reference, ORDERS


class ReferenceTests(unittest.TestCase):
    def test_eight_periods_each_role_against_separate_ledger(self):
        for role in range(4):
            with self.subTest(role=role):
                state = new_game(role)
                expected = reference(role)
                for period, quantity in enumerate(ORDERS):
                    state = advance(state, quantity, period, f'reference-{period}')
                    self.assertEqual(state['history'][-1], expected[period])


if __name__ == '__main__':
    unittest.main()
