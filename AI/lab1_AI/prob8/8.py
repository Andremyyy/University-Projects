# Să se genereze toate numerele (în reprezentare binară) cuprinse între 1 și n.
# De ex. dacă n = 4, numerele sunt: 1, 10, 11, 100.

# Complexitate timp: O(n log n), pt ca descompun pe rand numerele in cifre binare
# Complexitate spatiala: O(n), pt ca stochez cifrele binare intr-o lista suplimentara

def conversie_binar(nr):
    """
    Generează toate numerele binare de la 1 la n folosind conversia manuală în bază 2.

    Metodă:
        1. Parcurgem numerele de la 1 la n.
        2. Convertim fiecare număr în binar:
        3. Împărțim succesiv la 2, păstrând resturile într-o listă.
        4. Afișăm lista inversată pentru a obține reprezentarea binară corectă.

    :param n: Număr natural
    :return: Afișează numerele binare de la 1 la n.

    """

    if nr == 0:
        print(0)
        return

    cifre_binare = []
    while nr > 0:
        cifre_binare.append(nr % 2)  # la sfarsit
        nr //= 2

    for i in range(len(cifre_binare) - 1, -1, -1):
        print(cifre_binare[i], end = '')
    print()

def numere_binare(n):
    for i in range(1, n +1):
        conversie_binar(i)


if __name__ == '__main__':
    numere_binare(4)