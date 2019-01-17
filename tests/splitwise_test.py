import unittest
from src.splitwise import Splitwise

class TestSplitwise(unittest.TestCase):

    def test_calculate_per_member_share(self):
        members = ['A', 'B']
        expenses = [('A', 300, 'snacks'), ('B', 100, 'tickets')]
        splitwise = Splitwise(members, expenses)
        self.assertEquals(200, splitwise.calculate_per_member_share())

    def test_calculate_per_member_balances(self):
        members = ['A', 'B', 'C']
        expenses = [('A', 200, 'snacks'), ('B', 100, 'tickets')]
        splitwise = Splitwise(members, expenses)

        expected = {'A': 100, 'B': 0.0, 'C': -100.0}
        self.assertEquals(expected, splitwise.calculate_per_member_balances())

    def test_get_borrowers_and_lenders_and_balanced(self):
        members = ['A', 'B', 'C']
        expenses = [('A', 200, 'snacks'), ('B', 100, 'tickets')]
        splitwise = Splitwise(members, expenses)

        borrowers = {'C': -100.0}
        lenders = {'A': 100}
        self.assertDictEqual(borrowers, splitwise.calculate_borrowers_and_lenders_balances()[0])
        self.assertDictEqual(lenders, splitwise.calculate_borrowers_and_lenders_balances()[1])

    def test_split_expense_for_one_borrower_one_lender(self):
        members = ['A', 'B']
        expenses = [('A', 200, 'snacks')]
        splitwise = Splitwise(members, expenses)

        expected = [['B', 'A', 100]]
        self.assertListEqual(expected, splitwise.split_expense())

    def test_split_expense_for_one_lender_many_borrowers(self):
        members = ['A', 'B', 'C']
        expenses = [('A', 300, 'snacks')]
        splitwise = Splitwise(members, expenses)

        expected = [['B', 'A', 100.0], ['C', 'A', 100.0]]
        self.assertItemsEqual(expected, splitwise.split_expense())

    def test_split_expense_for_one_lender_repeated_lends_many_borrowers(self):
        members = ['A', 'B', 'C']
        expenses = [('A', 450, 'snacks'), ('A', 450, 'snacks')]
        splitwise = Splitwise(members, expenses)

        expected = [['B', 'A', 300.0], ['C', 'A', 300.0]]
        self.assertItemsEqual(expected, splitwise.split_expense())

    def test_split_expense_for_many_lenders_one_borrower(self):
        members = ['A', 'B', 'C']
        expenses = [('A', 450, 'snacks'), ('B', 450, 'snacks_1')]
        splitwise = Splitwise(members, expenses)

        expected = [['C', 'A', 150], ['C', 'B', 150]]
        self.assertListEqual(expected, splitwise.split_expense())

    def test_split_expense_for_many_lenders_repeated_lends_one_borrower(self):
        members = ['A', 'B', 'C']
        expenses = [('A', 450, 'snacks'), ('A', 450, 'snacks'), ('B', 450, 'snacks'), ('B', 450, 'snacks')]
        splitwise = Splitwise(members, expenses)

        expected = [['C', 'A', 300], ['C', 'B', 300]]
        self.assertListEqual(expected, splitwise.split_expense())

    def test_split_expense_for_many_lenders_many_borrowers(self):
        members = ['A', 'B', 'C']
        expenses = [('A', 450, 'snacks'), ('B', 150, 'snacks')]
        splitwise = Splitwise(members, expenses)

        expected = [['B', 'A', 50.0], ['C', 'A', 200.0]]
        self.assertItemsEqual(expected, splitwise.split_expense())

    def test_split_expense_for_many_lenders_repeated_lends_many_borrowers(self):
        members = ['A', 'B', 'C']
        expenses = [('A', 500, 'snacks'), ('A', 200, 'snacks_1'), ('B', 150, 'snacks'), ('B', 50, 'snacks_1')]
        splitwise = Splitwise(members, expenses)

        expected = [['B', 'A', 100.0], ['C', 'A', 300.0]]
        self.assertItemsEqual(expected, splitwise.split_expense())

    def test_split_expense_for_many_lenders_repeated_lends_many_borrowers_floats(self):
        members = ['A', 'B', 'C']
        expenses = [('A', 500, 'snacks'), ('A', 200, 'snacks_1'), ('B', 150, 'snacks'), ('B', 150, 'snacks_1')]
        splitwise = Splitwise(members, expenses)

        expected = [['B', 'A', round(1000/3.0 - 300, 2)], ['C', 'A', round(1000/3.0, 2)]]
        self.assertItemsEqual(expected, splitwise.split_expense())


if __name__ == '__main__':
    unittest.main()
