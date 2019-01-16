import argparse
import re
from splitwise import Splitwise

def main():
    (members, expenses) = parse_input_file(args.input_file)
    splitwise = Splitwise(members, expenses)
    transactions = splitwise.split_expense()
    print_output(transactions)

def parse_input_file(input_file):
    with open(input_file, 'r') as f:
        read_data = f.readlines()
        members = read_data[0]
        members_list = re.sub('[,\n]', '', members).split()

        expenses = []
        for line in read_data[2:]:
            expenses.append(line)
        expenses_list_temp = [re.sub('[\n]', '', x).split() for x in expenses]
        expenses_list = [(x[0], float(x[1]), x[2]) for x in expenses_list_temp]

        print("=================================================")
        print("INPUT")
        print "Reading input file", args.input_file
        print "Input Members", members_list
        print "Input Expenses", expenses_list
        print("=================================================")

        return members_list, expenses_list

def print_output(transactions):
    print("=================================================")
    print("OUTPUT")
    for x in transactions:
        print x[0], '->', x[1], x[2]
    print("=================================================")

if __name__ == '__main__':
    print("*************************************************")
    print("SPLITWISE EXPENSE DISTRIBUTION")

    parser = argparse.ArgumentParser(description=
            'Split expenses between memebrs. Read input file from command line.')
    parser.add_argument(
        "--input_file", type=str, help='File name of input file.')
    args = parser.parse_args()

    if args.input_file:
        main()
    else:
        print("No input file provided! Please see usages. Hence, exiting.")

    print("*************************************************")

