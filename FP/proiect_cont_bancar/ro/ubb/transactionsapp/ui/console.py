from ro.ubb.transactionsapp.operations.transactionoperations import validate_date, date_exist, delete_transaction_date, \
    period_exist, delete_transaction_period, id_index, validate_sum, validate_is_in, update_transaction, id_unique, \
    add_transaction, is_in_exist, delete_transaction_type, print_all_transactions_with_bigger_sums, \
    print_bigger_sum_and_smaller_date, print_all_transactions_with_type, calculate_total_sum_type, \
    filter_all_transactions_type, filter_all_transactions_type_and_sum, \
    calculate_account_balance_date, transactions_sorted_sum, exist_list


def print_all_options():
    print("1 - Add transaction. \n"
          "2 - Print all transactions. \n"
          "3 - Update transaction. \n"
          "4 - Delete transactions from a given date. \n"
          "5 - Delete transactions from a given period. \n"
          "6 - Delete transactions that have a specific type. \n"
          "7 - Print all transactions with a sum bigger than a specific one. \n"
          "8 - Print all transactions with a sum bigger than a specific one and before a given date. \n"
          "9 - Print all transactions of a certain type. \n"
          "10 - Print the total sum of the transactions which have a specific type. \n"
          "11 - Print the account balance for a given date. \n"
          "12 - Print all transactions of a certain type ordered by sum. \n"
          "13 - Filter all transactions of a certain type. \n"
          "14 - Filter all transactions smaller than a given sum that have a specified type. \n"
          "x - Exit.")


def ui_delete_transaction_date(all_transactions):
    date = int(input("The date of the transactions that we want to delete is: "))

    while not validate_date(date):
        print("The date is not valid")
        date = int(input("The date of the transactions that we want to delete is: "))

    if not date_exist(all_transactions, date):
        print("There is no transaction that has that date")
    else:
        delete_transaction_date(all_transactions, date)


def ui_delete_transaction_period(all_transactions):
    first_date = int(input("The first date of the transactions that we want to delete is: "))
    while not validate_date(first_date):
        print("The date " + str(first_date) + " is not valid.")
        first_date = int(input("The first date of the transactions that we want to delete is: "))

    last_date = int(input("The last date of the transactions that we want to delete is: "))
    while not validate_date(last_date):
        print("The date " + str(last_date) + " is not valid.")
        last_date = int(input("The last date of the transactions that we want to delete is: "))

    if first_date > last_date:
        print("The dates are not in chronological order")
    elif not period_exist(all_transactions, first_date, last_date):
        print("There is no transaction in that given period")
    else:
        delete_transaction_period(all_transactions, first_date, last_date)


def ui_update_transaction(all_transactions):
    id = int(input("The id of the transaction that we want to update is: "))
    if id_index(all_transactions, id) == -1:
        print("This transaction does not exist")
    else:
        date = int(input("The date is: "))
        while not validate_date(date):
            print("The date " + str(date) + " is not valid.")
            date = int(input("The date is: "))

        sum = float(input("The sum is: "))
        while not validate_sum(sum):
            print("The sum " + str(sum) + " is not valid.")
            sum = float(input("The sum is:"))

        is_in = input("Is in (y/n)? ")
        while not validate_is_in(is_in):
            print("The type is not valid.")
            is_in = input("Is in (y/n)? ")

        update_transaction(all_transactions, id, date, sum, is_in)


def ui_add_transaction(all_transactions):
    print("Add transaction")

    id = int(input("The id is: "))
    while not id_unique(all_transactions, id):
        print("The id " + str(id) + " is not unique")
        id = int(input("The id is: "))

    date = int(input("The date is: "))
    while not validate_date(date):
        print("The date " + str(date) + " is not valid.")
        date = int(input("The date is: "))

    sum = float(input("The sum is: "))
    while not validate_sum(sum):
        print("The sum " + str(sum) + " is not valid.")
        sum = float(input("The sum is:"))

    is_in = input("Is in (y/n)? ")
    while not validate_is_in(is_in):
        print("The type is not valid.")
        is_in = input("Is in (y/n)? ")

    add_transaction(all_transactions, id, date, sum, is_in)


def ui_print_all_transaction(all_transactions):
    if not exist_list(all_transactions):
        print("!!!The list has no transactions!!!")
    for transaction in all_transactions:
        print(transaction)


def ui_delete_transaction_type(all_transactions):
    is_in = input("The type of all the transactions that we to print is: (y/n) ")
    while not validate_is_in(is_in):
        print("That is not a valid type")
        is_in = input("The type of all the transactions that we to print is: (y/n) ")

    if not is_in_exist(all_transactions, is_in):
        print("There is no transaction with that type")
    else:
        delete_transaction_type(all_transactions, is_in)


def ui_print_all_transactions_with_bigger_sums(all_transactions):
    sum = float(input("The sum we want to compare the transactions is: "))
    while not validate_sum(sum):
        print("The sum " + str(sum) + " is not valid.")
        sum = float(input("The sum we want to compare the transactions is: "))
    print("The transactions that have a bigger sum: ")
    ui_print_all_transaction(print_all_transactions_with_bigger_sums(all_transactions, sum))


def ui_print_bigger_sum_and_smaller_date(all_transactions):
    sum = float(input("The sum we want to compare the transactions is: "))
    while not validate_sum(sum):
        print("The sum " + str(sum) + " is not valid.")
        sum = float(input("The sum we want to compare the transactions is: "))
    date = int(input("The date we want to compare the transactions is: "))
    while not validate_date(date):
        print("The date " + str(date) + " is not valid.")
        date = int(input("The date we want to compare the transactions is: "))
    print("The transactions that have a bigger sum and a smaller date: ")
    ui_print_all_transaction(print_bigger_sum_and_smaller_date(all_transactions, sum, date))


def ui_print_all_transactions_with_type(all_transactions):
    is_in = input("The type of all the transactions that we to print is: ")
    while not validate_is_in(is_in):
        print("The type is not valid.")
        is_in = input("The type of all the transactions that we to print is: ")
    print("The transactions that have the given type: ")
    ui_print_all_transaction(print_all_transactions_with_type(all_transactions, is_in))


def ui_print_total_sum_all_transactions_type(all_transactions):
    is_in = input("The type of all the transactions that we want to calculate the total sum is: ")
    while not validate_is_in(is_in):
        print("The type is not valid.")
        is_in = input("The type of all the transactions that we want to calculate the total sum is: ")

    print("The total sum of all the transactions that have the given type is: " + str(
        calculate_total_sum_type(all_transactions, is_in)))


def ui_print_account_balance_date(all_transactions):
    date = int(input("The date of the transactions that we want to calculate the account balance is: "))
    while not validate_date(date):
        print("The date " + str(date) + " is not valid.")
        date = int(input("The date of the transactions that we want to calculate the account balance is: "))
    if not date_exist(all_transactions, date):
        print("There are no transactions made on the given date")
    else:
        print("The account balance is: " + str(calculate_account_balance_date(all_transactions, date)))


def ui_print_sorted_sum_by_type(all_transactions):
    is_in = input("The type of all the transactions that we want to order by sum is: ")
    while not validate_is_in(is_in):
        print("The type is not valid.")
        is_in = input("The type of all the transactions that we want to order by sum is: ")
    if not is_in_exist(all_transactions, is_in):
        print("There are no transactions with that type")
    else:
        print("The sorted list of all the transactions that have the given type is:")
        ui_print_all_transaction(transactions_sorted_sum(all_transactions, is_in))


def ui_filter_all_transactions_type(all_transactions):
    is_in = input("The type of all the transactions that we want to filter is: ")
    while not validate_is_in(is_in):
        print("The type is not valid.")
        is_in = input("The type of all the transactions that we want to filter is: ")
    if not is_in_exist(all_transactions, is_in):
        print("There are no transactions with that type")
    else:
        print("The filtered transactions are: ")
        ui_print_all_transaction(filter_all_transactions_type(all_transactions, is_in))


def ui_filter_all_transactions_type_and_sum(all_transactions):
    is_in = input("The type of all the transactions that we want to filter is: ")
    while not validate_is_in(is_in):
        print("The type is not valid.")
        is_in = input("The type of all the transactions that we want to filter is: ")
    sum = float(input("The sum we want to compare the transactions with is: "))
    while not validate_sum(sum):
        print("The sum " + str(sum) + " is not valid.")
        sum = float(input("The sum we want to compare the transactions is: "))
    if not is_in_exist(all_transactions, is_in):
        print("There are no transactions with that type")
    else:
        print("The filtered transactions are: ")
        ui_print_all_transaction(filter_all_transactions_type_and_sum(all_transactions, is_in, sum))


def run_menu():
    print("Choose an option!")
    all_transactions = []
    while True:
        print_all_options()
        all_options = {1: ui_add_transaction, 2: ui_print_all_transaction, 3: ui_update_transaction,
                       4: ui_delete_transaction_date, 5: ui_delete_transaction_period, 6: ui_delete_transaction_type,
                       7: ui_print_all_transactions_with_bigger_sums, 8: ui_print_bigger_sum_and_smaller_date,
                       9: ui_print_all_transactions_with_type, 10: ui_print_total_sum_all_transactions_type,
                       11: ui_print_account_balance_date, 12: ui_print_sorted_sum_by_type,
                       13: ui_filter_all_transactions_type,
                       14: ui_filter_all_transactions_type_and_sum}
        option = input("Introduce your option: ")

        if option == 'x':
            break
        option = int(option)
        if option in all_options:
            all_options[option](all_transactions)
        else:
            print("Invalid command!")
