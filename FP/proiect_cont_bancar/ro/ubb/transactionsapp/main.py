"""
Write an app that manages a bank account. Every transaction has its day,
sum, and type (input/output). The application should allow to:

F1. Add transaction (the id, the day, the amount and the type are given) = 1, 1
F2. Update of the transaction  (the id, the day, the amount and the type are given) = 1, 1
F3. Delete all transactions from the specified day = 1, 1
F4. Delete transactions from a given period (the first day and last day are given) = 1, 1
F5. Delete all transactions of a certain type = 1 , 1
F6. Print the transactions which have the sums bigger than a given sum = 1, 1
F7. Print all transactions which have been made before a given day and bigger than a given
sum (the sum and the day are given ) = 1, 1
F8. Print all transactions of a certain type = 1, 1
F9. Print the total sum of the transactions which have a certain type = 1, 1
F10. Print the account balance on a specified date = 1, 1
F11. Print all transactions of a certain type ordered by sum = 1, 1
F12. Filter all transactions of a certain type = 1, 1
F13. Filter all transactions smaller than a given sum that have a specified type = 1, 1
F14. Split the application into modules (main, ui, domain, operations) = 1,1

I1: F1, F2, F3, F4, F6, F7, F8, F9, F5, F10, F11, F12, F13
I2: F14

"""
# ============================================= domain =====================================
from ro.ubb.transactionsapp.domain.test_entities import test_all_entities
from ro.ubb.transactionsapp.operations.test_transactionoperations import test_all_operations
from ro.ubb.transactionsapp.ui.console import run_menu


# ==================================== operations ============================================


# ==================================== user interface ============================================


# ==================================== tests ============================================


def test_all():
    test_all_entities()
    test_all_operations()


if __name__ == '__main__':
    # print("Hello")
    test_all()
    run_menu()
