# Splitwise Python Application

This is a Python application to split expenses, provided the participating members and payments done by them. 

Steps to use the app:
(You may create a Python virtual env in and use the app inside the virtual env.)

1. Switch directory to base folder SplitwiseApp. 

2. Set env var PYTHONPATH to the application folder Splitwise.
```
export PYTHONPATH=`pwd`
```

3. To run the application, 
```
python src/main.py --input_file sample_inputs/sample_input.txt
```

4. To run tests, 
```
python tests/splitwise_test.py
```

# Algorithm:

Input: List of Members and List of expenses
Output: Transactions to settle expenses

Example:
INPUT
> A, B, C
>
> A 300 Snacks
> B 100 tickets

OUTPUT
> C -> A 133.33
> B -> A 33.33

1. Get share that everyone has to pay.
2. Find balance(what paid - share) for each member. 
3. Lenders are the ones with positive balances. Borrowers are the ones with negative balances.
4. For every borrower, 
    a. Get the absolute value of borrowed amount.
    b. Pay the absolute borrowed amount to lender(s). Note each transaction. See step 5. 
    (There can be many transactions and many lenders also.)
5. Pay the absolute borrowed amount(abs_borrower_amt):
    a. Get the lender who has lent most.
    b. Transaction amount = lender's balance, if abs_borrower_amt > lender's balance
        else Transaction amount = abs_borrowed_amt.
    c. Then, add Transaction amount to borrower's balance, remove it from lender's balance and abs_borrower_amt
    d. Record this transaction.
    e. Repeat till the abs_borrower_amt is greater than zero.
