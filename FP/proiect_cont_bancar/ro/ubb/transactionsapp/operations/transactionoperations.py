from ro.ubb.transactionsapp.domain.entities import create_transaction, get_id, get_date, set_date, set_sum, set_is_in, \
    get_is_in, get_sum


def add_transaction(all_transactions, id, date, sum, is_in):
    """
        Add a new transaction.
    :param list[dict] all_transactions: the list of all transactions
    :param int id: transaction id, should be unique
    :param int date: number between 1-31
    :param float sum: variable
    :param string is_in: 'y' if the transaction is in
                        'n' if the transaction is out
    :return: None
    """

    transaction = create_transaction(id, date, sum, is_in)
    all_transactions.append(transaction)


def id_index(all_transactions, id):
    """
    Returns the index of the transaction that has the given id
    :param list[dict] all_transactions: the list of all transactions
    :param int id: transaction id, should be unique
    :return: -1, if the id is not found in the list
            the index of the transaction that has the given id, if it is found
    """
    for index in range(len(all_transactions)):
        if get_id(all_transactions[index]) == id:
            return index
    return -1


def date_exist(all_transactions, date):
    """
    Checks if the list of transactions contains a transaction with the given date
    :param list[dict] all_transactions: the list of all transactions
    :param int date: number between 1-31
    :return: True, if the list of transactions contains a transaction with the given date
            False, if the date does not exist
    """
    for transaction in all_transactions:
        if get_date(transaction) == date:
            return True
    return False


def delete_transaction_date(all_transactions, date):
    """
    Deletes all the transactions that have the given date
    :param list[dict] all_transactions: the list of all transactions
    :param int date: number between 1-31
    :return: None
    """

    # for index in range(len(all_transactions) - 1, -1, -1):
    #     if get_date(all_transactions[index]) == date:
    #         all_transactions.pop(index)

    all_transactions[:] = [transaction for transaction in all_transactions if get_date(transaction) != date]


def update_transaction(all_transactions, id, date, sum, is_in):
    """
    Update a transaction
    :param list[dict] all_transactions: the list of all transactions
    :param int id: transaction id, should be unique
    :param int date: number between 1-31
    :param float sum: variable
    :param string is_in: 'y' if the transaction is in
                        'n' if the transaction is out
    :return: None
    """

    index = id_index(all_transactions, id)

    set_date(all_transactions[index], date)
    set_sum(all_transactions[index], sum)
    set_is_in(all_transactions[index], is_in)


def period_exist(all_transactions, first_date, last_date):
    """
    Checks if the list of transactions contains a transaction within the given period
    :param all_transactions: list[dict] all_transactions: the list of all transactions
    :param int first_date: number between 1-31
    :param int last_date: number between 1-31
    :return: True, if the list of transactions contains a transaction within the given period
            False, if there is no transaction within the given period
    """
    for transaction in all_transactions:
        if first_date <= get_date(transaction) <= last_date:
            return True
    return False


def is_in_exist(all_transactions, is_in):
    """
    Function that checks if the is_in variable exists within the list of dictionaries
    :param all_transactions: list[dict] all_transactions: the list of all transactions
    :param is_in: string variable
    :return: True, if the variable exists within the list of dictionaries
            False, if the variable does not exist within the list of dictionaries
    """
    for transaction in all_transactions:
        if get_is_in(transaction) == is_in:
            return True
    return False


def delete_transaction_period(all_transactions, first_date, last_date):
    """
    Deletes all the transactions within a given period
    :param all_transactions: list[dict] all_transactions: the list of all transactions
    :param int first_date: number between 1-31
    :param int last_date: number between 1-31
    :return: None
    """

    while first_date <= last_date:
        delete_transaction_date(all_transactions, first_date)
        first_date += 1


def delete_transaction_type(all_transactions, is_in):
    """
    Deletes all the transactions that have a specific type
    :param all_transactions: list[dict] all_transactions: the list of all transactions
    :param is_in: string variable
    return: None
    """

    all_transactions[:] = [transaction for transaction in all_transactions if get_is_in(transaction) != is_in]


def print_all_transactions_with_bigger_sums(all_transactions, sum):
    """
    Prints all the transactions that have a bigger sum than a specific one
    :param all_transactions: list[dict] all_transactions: the list of all transactions
    :param sum: float variable
    return: a new list with the transactions that have bigger sums that the given one
    """
    new_all_transactions = []
    for transaction in all_transactions:
        if sum < get_sum(transaction):
            new_all_transactions.append(transaction)
    return new_all_transactions


def print_bigger_sum_and_smaller_date(all_transactions, sum, date):
    """
    Prints all the transactions that have a bigger sum and a smaller date than the specific ones
    :param all_transactions: list[dict] all_transactions: the list of all transactions
    :param sum: positive float variable
    :param date: int variable between 1 and 31
    return: a new list with the transactions that have bigger sums and smaller date than the given one
    """
    new_all_transactions = []
    for transaction in all_transactions:
        if sum < get_sum(transaction) and date > get_date(transaction):
            new_all_transactions.append(transaction)
    return new_all_transactions


def id_unique(all_transactions, id):
    """
    Function that checks if a given id is unique within the list of transactions
    :param all_transactions: list[dict] all_transactions: the list of all transactions
    :param int id: transaction id, should be unique
    :return: False, if the id is not unique
             True, if the id is unique
    """

    for transaction in all_transactions:
        if get_id(transaction) == id:
            return False
    return True


def validate_date(date):
    """
    Function that checks if an integer is between 1 and 31
    :param int date: number between 1 and 31
    :return: False, if the date is smaller than 1 or bigger than 31
             True, if the date is between 1 and 31
    """
    if date < 1 or date > 31:
        return False
    return True


def validate_sum(sum):
    """
    Function that checks if a float is positive
    :param sum: float variable
    :return: False, if the float is negative
             True, if the float is positive
    """
    if sum <= 0.0:
        return False
    return True


def validate_is_in(is_in):
    """
    Function that checks if the variable is either 'y' or 'n'
    :param is_in: string variable
    :return: False, if the variable is anything else than 'y' or 'n'
            True, if the variable is either 'y' or 'n'
    """
    if not is_in == 'y' and not is_in == 'n':
        return False
    return True


def print_all_transactions_with_type(all_transactions, is_in):
    """

    :param all_transactions:
    :param is_in:
    :return:
    """
    new_all_transactions = []
    for transaction in all_transactions:
        if get_is_in(transaction) == is_in:
            new_all_transactions.append(transaction)
    return new_all_transactions


def calculate_total_sum_type(all_transactions, is_in):
    """
    The function calculates the total sum of all the transactions that have the given type
    :param all_transactions: list[dict] all_transactions: the list of all transactions
    :param is_in: string variable
    :return: the total sum of all the transactions that have the given type
            0, if there are no transactions that have the given type
    """

    sum = 0.0
    for transaction in all_transactions:
        if get_is_in(transaction) == is_in:
            sum += get_sum(transaction)
    return sum


def calculate_account_balance_date(all_transactions, date):
    """
    This functions calculates the account balance on a given date
    :param all_transactions: list[dict] all_transactions: the list of all transactions
    :param int date: variable between 1 and 31
    :return: a float variable which represents the account balance on that given date (it can be negative or positive)
    """
    sum = 0.0
    for transaction in all_transactions:
        if get_date(transaction) == date:
            if get_is_in(transaction) == 'y':
                sum += get_sum(transaction)
            else:
                sum -= get_sum(transaction)

    return sum


def transactions_sorted_sum(all_transactions, is_in):
    """
    This function sorts by sum a given list of transactions filtered by type
    :param all_transactions: list[dict] all_transactions: the list of all transactions
    :param is_in: string variable('y' or 'n')
    :return: a new list ordered by sum and filtered by type
    """
    transactions_type = []
    for transaction in all_transactions:
        if get_is_in(transaction) == is_in:
            transactions_type.append(transaction)
    transaction_type_sorted = sorted(transactions_type, key=get_sum)
    return transaction_type_sorted


def filter_all_transactions_type(all_transactions, is_in):
    """
    This function filters the transactions that have a specific type
    :param all_transactions: list[dict] all_transactions: the list of all transactions
    :param is_in: string variable ('y' or 'n')
    :return: a new list that contains all the transactions with the given type
    """
    new_all_transactions = []
    for transaction in all_transactions:
        if get_is_in(transaction) == is_in:
            new_all_transactions.append(transaction)

    return new_all_transactions


def filter_all_transactions_type_and_sum(all_transactions, is_in, sum):
    """
    This function filters by type all transactions that have the sum smaller than a given one
    :param all_transactions: list[dict] all_transactions: the list of all transactions
    :param is_in: string variable('y' or 'n')
    :param sum: positive float variable
    :return: a new list of the transactions filtered by type that have a sum smaller than a given one
    """
    new_all_transactions = []
    for transaction in all_transactions:
        if get_is_in(transaction) == is_in:
            if get_sum(transaction) < sum:
                new_all_transactions.append(transaction)
    return new_all_transactions


def exist_list(all_transactions):
    """
    Checks if the list has at least one transaction
    :param all_transactions: list[dict] all_transactions: the list of all transactions
    :return: True if the list has at least one transaction
            False, if the list has no transactions
    """
    if len(all_transactions) == 0:
        return False
    return True
