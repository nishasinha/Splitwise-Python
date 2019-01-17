class Splitwise:
    def __init__(self, members, expenses):
        self.members = members
        self.expenses = expenses

    def calculate_per_member_share(self):
        sum_of_expenses = float(sum([x[1] for x in self.expenses]))
        return sum_of_expenses/len(self.members)

    def calculate_per_member_balances(self):
        each_share = self.calculate_per_member_share()
        balances = {}
        for member in self.members:
            expense_of_member = sum([x[1] for x in self.expenses if x[0] == member])
            balances[member] = round(expense_of_member - each_share, 2)
        return balances

    def calculate_borrowers_and_lenders_balances(self):
        lenders = {}
        borrowers = {}
        member_balances = self.calculate_per_member_balances()
        for member, balance in member_balances.items():
            if balance > 0:
                lenders[member] = balance
            elif balance < 0:
                borrowers[member] = balance

        return borrowers, lenders

    def pay_borrowed_amount_to_lender(self, borrowed_amt, borrowers, borrower, lenders, lender):
        lenders_amt = lenders[lender]
        amount_to_pay = lenders_amt if borrowed_amt > lenders_amt else borrowed_amt

        borrowers[borrower] += amount_to_pay
        lenders[lender] -= amount_to_pay
        borrowed_amt -= amount_to_pay
        return [borrower, lender, amount_to_pay], borrowed_amt

    def split_expense(self):
        (borrowers, lenders) = self.calculate_borrowers_and_lenders_balances()
        transactions = []
        for borrower, borrowed_amt in borrowers.items():
            abs_borrowed_amt = round(abs(borrowed_amt), 2)
            while abs_borrowed_amt > 0:
                lender = max(lenders, key=lenders.get)
                transaction, abs_borrowed_amt = self.pay_borrowed_amount_to_lender(abs_borrowed_amt, borrowers, borrower, lenders, lender)
                transactions.append(transaction)
        return transactions
