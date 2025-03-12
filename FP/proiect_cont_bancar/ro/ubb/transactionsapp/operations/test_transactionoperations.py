from ro.ubb.transactionsapp.domain.entities import get_id, get_sum, get_date, get_is_in
from ro.ubb.transactionsapp.operations.transactionoperations import add_transaction, update_transaction, \
    delete_transaction_date, delete_transaction_period, delete_transaction_type, calculate_total_sum_type, \
    calculate_account_balance_date, transactions_sorted_sum, filter_all_transactions_type, \
    filter_all_transactions_type_and_sum, print_all_transactions_with_bigger_sums, print_bigger_sum_and_smaller_date, \
    print_all_transactions_with_type, exist_list, validate_is_in, validate_sum, validate_date, id_unique, is_in_exist, \
    period_exist, date_exist, id_index


def test_add_transaction():
    all_transactions = []
    add_transaction(all_transactions, 101, 15, 80, 'y')
    assert (len(all_transactions) == 1)
    add_transaction(all_transactions, 23, 3, 15, 'n')
    add_transaction(all_transactions, 15, 7, 2456, 'n')
    assert (len(all_transactions) == 3)
    assert (get_id(all_transactions[0]) == 101)
    assert (get_sum(all_transactions[2]) == 2456)


def test_update_transaction():
    all_transactions = []
    add_transaction(all_transactions, 101, 15, 80, 'y')
    add_transaction(all_transactions, 23, 3, 15, 'n')
    add_transaction(all_transactions, 15, 7, 2456, 'n')

    update_transaction(all_transactions, 101, 16, 70, 'n')
    update_transaction(all_transactions, 3, 7, 150, 'y')
    update_transaction(all_transactions, 15, 3, 897, 'n')
    update_transaction(all_transactions, 23, 6, 657, 'y')
    assert (get_sum(all_transactions[0]) == 70)
    assert (get_date(all_transactions[2]) == 3)
    assert (get_is_in(all_transactions[0]) == 'n')
    assert (get_date(all_transactions[1]) == 6)


def test_delete_transaction_date():
    all_transactions = []
    add_transaction(all_transactions, 101, 15, 80, 'y')
    add_transaction(all_transactions, 23, 3, 15, 'n')
    add_transaction(all_transactions, 15, 7, 2456, 'n')

    delete_transaction_date(all_transactions, 3)
    assert (len(all_transactions) == 2)
    assert (get_id(all_transactions[1]) == 15)
    delete_transaction_date(all_transactions, 15)
    assert (len(all_transactions) == 1)
    delete_transaction_date(all_transactions, 7)
    assert (len(all_transactions) == 0)


def test_delete_transaction_period():
    all_transactions = []
    add_transaction(all_transactions, 101, 3, 80, 'y')
    add_transaction(all_transactions, 23, 5, 15, 'n')
    add_transaction(all_transactions, 15, 6, 2456, 'n')
    add_transaction(all_transactions, 4, 6, 246, 'n')
    add_transaction(all_transactions, 5, 7, 256, 'n')
    add_transaction(all_transactions, 6, 19, 456, 'n')
    add_transaction(all_transactions, 20, 25, 24, 'n')
    add_transaction(all_transactions, 9, 31, 2, 'n')

    delete_transaction_period(all_transactions, 4, 7)
    assert (len(all_transactions) == 4)
    assert (get_id(all_transactions[1]) == 6)
    assert (get_id(all_transactions[3]) == 9)

    delete_transaction_period(all_transactions, 3, 9)
    assert (len(all_transactions) == 3)
    delete_transaction_period(all_transactions, 1, 31)
    assert (len(all_transactions) == 0)


def test_delete_transaction_type():
    all_transactions = []
    add_transaction(all_transactions, 101, 3, 80, 'y')
    add_transaction(all_transactions, 23, 5, 15, 'n')
    add_transaction(all_transactions, 15, 6, 2456, 'n')
    add_transaction(all_transactions, 4, 6, 246, 'y')
    add_transaction(all_transactions, 5, 7, 256, 'n')
    add_transaction(all_transactions, 6, 19, 456, 'y')
    add_transaction(all_transactions, 20, 25, 24, 'n')
    add_transaction(all_transactions, 9, 31, 2, 'n')
    assert (len(all_transactions) == 8)
    delete_transaction_type(all_transactions, 'y')
    assert (len(all_transactions) == 5)
    delete_transaction_type(all_transactions, 'n')
    assert (len(all_transactions) == 0)


def test_calculate_total_sum_type():
    all_transactions = []
    add_transaction(all_transactions, 101, 3, 80, 'y')
    add_transaction(all_transactions, 23, 5, 15, 'n')
    add_transaction(all_transactions, 15, 6, 2456.8, 'n')
    add_transaction(all_transactions, 4, 6, 246, 'n')
    add_transaction(all_transactions, 5, 7, 256, 'y')
    add_transaction(all_transactions, 6, 19, 456.3, 'n')
    add_transaction(all_transactions, 20, 25, 24, 'y')
    add_transaction(all_transactions, 9, 31, 2.542, 'n')

    epsilon = 0.00001
    # print(calculate_total_sum_type(all_transactions, 'y'))
    assert (abs(calculate_total_sum_type(all_transactions, 'y') - 360) <= epsilon)
    # print(calculate_total_sum_type(all_transactions, 'n'))
    assert (abs(calculate_total_sum_type(all_transactions, 'n') - 3176.642) <= epsilon)


def test_calculate_account_balance_date():
    all_transactions = []
    add_transaction(all_transactions, 101, 3, 80, 'y')
    add_transaction(all_transactions, 23, 3, 80, 'n')
    add_transaction(all_transactions, 15, 6, 2456.8, 'n')
    add_transaction(all_transactions, 4, 6, 246, 'n')
    add_transaction(all_transactions, 5, 7, 256, 'y')
    add_transaction(all_transactions, 6, 7, 456.3, 'n')
    add_transaction(all_transactions, 20, 7, 24, 'y')
    add_transaction(all_transactions, 9, 7, 2.542, 'n')

    epsilon = 0.00001
    assert (abs(calculate_account_balance_date(all_transactions, 3) - 0) <= epsilon)
    # print(calculate_account_balance_date(all_transactions, 6)) = -2702.8
    assert (abs(calculate_account_balance_date(all_transactions, 6) + 2702.8) <= epsilon)
    # print(calculate_account_balance_date(all_transactions, 7)) = -178.842
    assert (abs(calculate_account_balance_date(all_transactions, 7) + 178.842) <= epsilon)


def test_transactions_sorted_sum():
    all_transactions = []
    add_transaction(all_transactions, 101, 3, 80, 'y')
    add_transaction(all_transactions, 23, 3, 324.1, 'n')
    add_transaction(all_transactions, 15, 6, 2456.8, 'n')
    add_transaction(all_transactions, 4, 6, 45.12, 'n')
    add_transaction(all_transactions, 5, 7, 256, 'y')
    add_transaction(all_transactions, 6, 7, 456.3, 'n')
    add_transaction(all_transactions, 20, 7, 246.3, 'y')
    add_transaction(all_transactions, 9, 7, 2.542, 'n')

    sorted_list_y = transactions_sorted_sum(all_transactions, 'y')
    sorted_list_n = transactions_sorted_sum(all_transactions, 'n')
    assert (len(sorted_list_y) == 3)
    assert (len(sorted_list_n) == 5)
    # print(sorted_list_y)
    # [{'id': 101, 'date': 3, 'sum': 80, 'is_in': 'y'},
    # {'id': 20, 'date': 7, 'sum': 246.3, 'is_in': 'y'},
    # {'id': 5, 'date': 7, 'sum': 256, 'is_in': 'y'}]
    # print(sorted_list_n)
    # [{'id': 9, 'date': 7, 'sum': 2.542, 'is_in': 'n'},
    #  {'id': 4, 'date': 6, 'sum': 45.12, 'is_in': 'n'},
    #  {'id': 23, 'date': 3, 'sum': 324.1, 'is_in': 'n'},
    #  {'id': 6, 'date': 7, 'sum': 456.3, 'is_in': 'n'},
    #  {'id': 15, 'date': 6, 'sum': 2456.8, 'is_in': 'n'}]
    assert (get_id(sorted_list_y[0]) == 101)
    assert (get_id(sorted_list_y[1]) == 20)
    assert (get_id(sorted_list_y[2]) == 5)
    assert (get_sum(sorted_list_y[0]) == 80)
    assert (get_sum(sorted_list_y[1]) == 246.3)
    assert (get_sum(sorted_list_y[2]) == 256)
    assert (get_sum(sorted_list_n[0]) == 2.542)
    assert (get_sum(sorted_list_n[1]) == 45.12)
    assert (get_sum(sorted_list_n[2]) == 324.1)
    assert (get_sum(sorted_list_n[3]) == 456.3)
    assert (get_sum(sorted_list_n[4]) == 2456.8)


def test_filter_all_transactions_type():
    all_transactions = []
    add_transaction(all_transactions, 101, 3, 80, 'y')
    add_transaction(all_transactions, 23, 3, 324.1, 'n')
    add_transaction(all_transactions, 15, 6, 2456.8, 'n')
    add_transaction(all_transactions, 4, 6, 45.12, 'n')
    add_transaction(all_transactions, 5, 7, 256, 'y')
    add_transaction(all_transactions, 6, 7, 456.3, 'n')
    add_transaction(all_transactions, 20, 7, 246.3, 'y')
    add_transaction(all_transactions, 9, 7, 2.542, 'n')

    filter_all_transactions_y = filter_all_transactions_type(all_transactions, 'y')
    filter_all_transactions_n = filter_all_transactions_type(all_transactions, 'n')

    # print(filter_all_transactions_y)
    # # [{'id': 101, 'date': 3, 'sum': 80, 'is_in': 'y'}, {'id': 5, 'date': 7, 'sum': 256, 'is_in': 'y'},
    # #  {'id': 20, 'date': 7, 'sum': 246.3, 'is_in': 'y'}]
    # print(filter_all_transactions_n)
    # # [{'id': 23, 'date': 3, 'sum': 324.1, 'is_in': 'n'}, {'id': 15, 'date': 6, 'sum': 2456.8, 'is_in': 'n'},
    # #  {'id': 4, 'date': 6, 'sum': 45.12, 'is_in': 'n'}, {'id': 6, 'date': 7, 'sum': 456.3, 'is_in': 'n'},
    # #  {'id': 9, 'date': 7, 'sum': 2.542, 'is_in': 'n'}]

    assert (len(filter_all_transactions_y) == 3)
    assert (len(filter_all_transactions_n) == 5)
    assert (get_id(filter_all_transactions_y[1]) == 5)
    assert (get_sum(filter_all_transactions_y[2]) == 246.3)
    assert (get_date(filter_all_transactions_n[2]) == 6)
    assert (get_sum(filter_all_transactions_n[4]) == 2.542)


def test_filter_all_transactions_type_and_sum():
    all_transactions = []
    add_transaction(all_transactions, 101, 3, 80, 'y')
    add_transaction(all_transactions, 23, 3, 324.1, 'n')
    add_transaction(all_transactions, 15, 6, 2456.8, 'n')
    add_transaction(all_transactions, 4, 6, 45.12, 'n')
    add_transaction(all_transactions, 5, 7, 256, 'y')
    add_transaction(all_transactions, 6, 7, 456.3, 'n')
    add_transaction(all_transactions, 20, 7, 246.3, 'y')
    add_transaction(all_transactions, 9, 7, 2.542, 'n')

    filter_all_transactions_y_and_sum = filter_all_transactions_type_and_sum(all_transactions, 'y', 247)
    filter_all_transactions_n_and_sum = filter_all_transactions_type_and_sum(all_transactions, 'n', 500)

    # print(filter_all_transactions_y_and_sum)
    # [{'id': 101, 'date': 3, 'sum': 80, 'is_in': 'y'}, {'id': 20, 'date': 7, 'sum': 246.3, 'is_in': 'y'}]

    # print(filter_all_transactions_n_and_sum)
    # [{'id': 23, 'date': 3, 'sum': 324.1, 'is_in': 'n'}, {'id': 4, 'date': 6, 'sum': 45.12, 'is_in': 'n'},
    #  {'id': 6, 'date': 7, 'sum': 456.3, 'is_in': 'n'}, {'id': 9, 'date': 7, 'sum': 2.542, 'is_in': 'n'}]

    assert (len(filter_all_transactions_y_and_sum) == 2)
    assert (len(filter_all_transactions_n_and_sum) == 4)
    assert (get_id(filter_all_transactions_y_and_sum[0]) == 101)
    assert (get_sum(filter_all_transactions_y_and_sum[1]) == 246.3)
    assert (get_date(filter_all_transactions_n_and_sum[3]) == 7)
    assert (get_sum(filter_all_transactions_n_and_sum[2]) == 456.3)


def test_print_all_transactions_with_bigger_sums():
    all_transactions = []
    add_transaction(all_transactions, 101, 3, 80, 'y')
    add_transaction(all_transactions, 23, 3, 324.1, 'n')
    add_transaction(all_transactions, 15, 6, 2456.8, 'n')
    add_transaction(all_transactions, 4, 6, 45.12, 'n')
    add_transaction(all_transactions, 5, 7, 256, 'y')
    add_transaction(all_transactions, 6, 7, 456.3, 'n')
    add_transaction(all_transactions, 20, 7, 246.3, 'y')
    add_transaction(all_transactions, 9, 7, 2.542, 'n')

    new_list = print_all_transactions_with_bigger_sums(all_transactions, 246.3)
    assert (len(new_list) == 4)
    assert (get_id(new_list[0]) == 23)
    assert (get_id(new_list[3]) == 6)


def test_print_bigger_sum_and_smaller_date():
    all_transactions = []
    add_transaction(all_transactions, 101, 3, 80, 'y')
    add_transaction(all_transactions, 23, 3, 324.1, 'n')
    add_transaction(all_transactions, 15, 6, 2456.8, 'n')
    add_transaction(all_transactions, 4, 6, 45.12, 'n')
    add_transaction(all_transactions, 5, 7, 256, 'y')
    add_transaction(all_transactions, 6, 7, 456.3, 'n')
    add_transaction(all_transactions, 20, 7, 246.3, 'y')
    add_transaction(all_transactions, 9, 7, 2.542, 'n')

    new_list = print_bigger_sum_and_smaller_date(all_transactions, 246.3, 7)
    assert (len(new_list) == 2)
    assert (get_id(new_list[0]) == 23)
    assert (get_id(new_list[1]) == 15)


def test_print_all_transactions_with_type():
    all_transactions = []
    add_transaction(all_transactions, 101, 3, 80, 'y')
    add_transaction(all_transactions, 23, 3, 324.1, 'n')
    add_transaction(all_transactions, 15, 6, 2456.8, 'n')
    add_transaction(all_transactions, 4, 6, 45.12, 'n')
    add_transaction(all_transactions, 5, 7, 256, 'y')
    add_transaction(all_transactions, 6, 7, 456.3, 'n')
    add_transaction(all_transactions, 20, 7, 246.3, 'y')
    add_transaction(all_transactions, 9, 7, 2.542, 'n')

    new_list_y = print_all_transactions_with_type(all_transactions, 'y')
    assert (len(new_list_y) == 3)
    new_list_n = print_all_transactions_with_type(all_transactions, 'n')
    assert (len(new_list_n) == 5)
    assert (get_id(new_list_y[1]) == 5)
    assert (get_id(new_list_n[3]) == 6)


def test_validate_exist_unique():
    all_transactions = []
    assert (not exist_list(all_transactions))
    add_transaction(all_transactions, 101, 3, 80, 'y')
    assert (exist_list(all_transactions))
    assert (not is_in_exist(all_transactions, 'n'))
    add_transaction(all_transactions, 23, 3, 324.1, 'n')
    assert (validate_is_in(all_transactions[1]['is_in']))
    assert (not validate_is_in('t'))
    add_transaction(all_transactions, 15, 6, 2456.8, 'n')
    assert (validate_sum(all_transactions[2]['sum']))
    assert (not validate_sum(0))
    assert (not validate_sum(-15.8372))
    add_transaction(all_transactions, 4, 6, 45.12, 'n')
    assert (validate_date(all_transactions[3]['date']))
    assert (not validate_date(0))
    assert (not validate_date(32))
    add_transaction(all_transactions, 5, 7, 256, 'y')
    assert (id_unique(all_transactions, 1))
    assert (not id_unique(all_transactions, 5))
    add_transaction(all_transactions, 6, 7, 456.3, 'n')
    assert (is_in_exist(all_transactions, 'y'))
    add_transaction(all_transactions, 20, 9, 246.3, 'y')
    assert (period_exist(all_transactions, 1, 9))
    assert (not period_exist(all_transactions, 30, 31))
    assert (not period_exist(all_transactions, 10, 9))
    assert (period_exist(all_transactions, 7, 7))
    assert (date_exist(all_transactions, 7))
    assert (not date_exist(all_transactions, 31))
    assert (id_index(all_transactions, 101) == 0)
    assert (id_index(all_transactions, 20) == 6)
    assert (id_index(all_transactions, 1) == -1)


def test_all_operations():
    test_add_transaction()
    test_update_transaction()
    test_print_all_transactions_with_bigger_sums()
    test_print_bigger_sum_and_smaller_date()
    test_print_all_transactions_with_type()
    test_delete_transaction_date()
    test_delete_transaction_period()
    test_delete_transaction_type()
    test_calculate_total_sum_type()
    test_calculate_account_balance_date()
    test_transactions_sorted_sum()
    test_filter_all_transactions_type()
    test_filter_all_transactions_type_and_sum()
    test_validate_exist_unique()
