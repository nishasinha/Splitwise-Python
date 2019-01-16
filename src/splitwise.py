class Splitwise:
    def __init__(self, members, expenses):
        self.members = members
        self.expenses = expenses

    def find_per_member_share(self):
        num_of_members = len(self.members)
        sum_of_expenses = 0.0
        for expense in self.expenses:
            sum_of_expenses += expense[1]
        return sum_of_expenses/num_of_members

    def find_balances_of_every_member(self):
        balances = []
        each_share = self.find_per_member_share()
        for member in self.members:
            balances.append([member, round(self.get_expense_of_member(member) - each_share, 2)])
        return balances

    def get_expense_of_member(self, member):
        m_expense = 0
        for expense in self.expenses:
            if expense[0] == member:
                m_expense += expense[1]
        return m_expense

    def calculate_borrowers_and_lenders_balances(self):
        lenders = []
        borrowers = []
        member_balances = self.find_balances_of_every_member()
        for member_balance in member_balances:
            if member_balance[1] > 0:
                lenders.append(member_balance)
            elif member_balance[1] < 0:
                borrowers.append(member_balance)

        return borrowers, lenders

    def pay_borrowed_amount_to_lender(self, borrowed_amt, borrower, lender):
        lenders_amt = lender[1]
        amount_to_pay = lenders_amt if borrowed_amt > lenders_amt else borrowed_amt

        borrower[1] += amount_to_pay
        lender[1] -= amount_to_pay
        borrowed_amt = borrowed_amt - amount_to_pay
        return [borrower[0], lender[0], amount_to_pay], borrowed_amt

    def split_expense(self):
        (borrowers, lenders) = self.calculate_borrowers_and_lenders_balances()
        transactions = []
        for borrower in borrowers:
            borrowed_amt = round(abs(borrower[1]), 2)
            while borrowed_amt > 0:
                lender = sorted(lenders, key=lambda x: x[1], reverse=True)[0]
                transaction, borrowed_amt = self.pay_borrowed_amount_to_lender(borrowed_amt, borrower, lender)
                transactions.append(transaction)
        return transactions
