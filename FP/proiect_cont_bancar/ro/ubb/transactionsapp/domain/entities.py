def create_transaction(id, date, sum, is_in):
    """
    Create a new transaction.

    :param int id: transaction id
    :param int date: number between 1-31
    :param float sum: variable
    :param string is_in: 'y' if the transaction is in
                        'n' if the transaction is out
    :return: a new transaction dictionary with the keys *id*, *date*, *sum*, *is_in* and the values
            given as arguments
    :rtype: dict
    """
    return {
        "id": id,
        "date": date,
        "sum": sum,
        "is_in": is_in
    }


def get_id(transaction):
    return transaction["id"]


def get_date(transaction):
    return transaction["date"]


def get_sum(transaction):
    return transaction["sum"]


def get_is_in(transaction):
    return transaction["is_in"]


def set_id(transaction, id):
    transaction["id"] = id


def set_date(transaction, date):
    transaction["date"] = date


def set_sum(transaction, sum):
    transaction["sum"] = sum


def set_is_in(transaction, is_in):
    transaction["is_in"] = is_in
