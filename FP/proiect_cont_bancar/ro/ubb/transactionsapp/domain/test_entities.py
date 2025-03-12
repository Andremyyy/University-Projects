from ro.ubb.transactionsapp.domain.entities import create_transaction, get_id, get_date, get_sum, get_is_in, set_is_in, \
    set_sum, set_date


def test_create_transaction():
    transaction = create_transaction(1, 12, 245.12, 'y')
    assert (get_id(transaction) == 1)
    assert (get_date(transaction) == 12)
    assert (get_sum(transaction) == 245.12)
    assert (get_is_in(transaction) == 'y')


def test_get_and_set():
    transaction = {"id": 1, "date": 12, "sum": 245.12, "is_in": 'y'}
    epsilon = 0.00001
    assert (get_id(transaction) == 1)
    assert (get_date(transaction) == 12)
    assert (abs(get_sum(transaction) - 245.12) <= epsilon)
    assert (get_is_in(transaction) == 'y')

    set_is_in(transaction, 'n')
    set_sum(transaction, 300)
    set_date(transaction, 1)
    assert (get_date(transaction) == 1)
    assert (abs(get_sum(transaction) - 300) <= epsilon)
    assert (get_is_in(transaction) == 'n')


def test_all_entities():
    test_create_transaction()
    test_get_and_set()
