# Pentru un șir cu n numere întregi care conține și duplicate, să se determine elementul majoritar
# (care apare de mai mult de n / 2 ori).
# De ex. 2 este elementul majoritar în șirul [2,8,7,2,2,5,2,3,1,2,2].

# Complexitate timp: O(n log n), pt ca sortez numerele
# Complexitate spatiala: O(n), pt ca folosesc un dictionar


def element_majoritar(sir):
    """
        Identifică elementul majoritar dintr-un șir (apare de mai mult de n/2 ori).

        Metodă:
        - Se construiește un dicționar de frecvență unde se numără de câte ori apare fiecare element.
        - Se sortează elementele în funcție de frecvență în ordine descrescătoare.
        - Se verifică dacă cel mai frecvent element apare de mai mult de n/2 ori și se returnează.

        :param sir: Listă de numere întregi.
        :return: Elementul majoritar sau None dacă nu există sau daca sirul este vid.
    """
    if len(sir) == 0:
        return None

    frecventa = {}

    for numar in sir:
        frecventa[numar] = frecventa.get(numar, 0) + 1

    numere_descr = sorted(frecventa.items(),key = lambda item:item[1], reverse=True)

    if numere_descr[0][1] > len(sir) // 2:
        return numere_descr[0][0]

    return None

def teste_element_majoritar():
    assert element_majoritar([1, 1, 1, 2, 3, 4, 1, 1]) == 1
    assert element_majoritar([1, 2, 3, 4, 5, 6]) is None
    assert element_majoritar([4, 4, 4, 4, 4]) == 4
    assert element_majoritar([]) is None
    print("Testele au trecut cu succes!")

if __name__ == '__main__':
    teste_element_majoritar()
    print(element_majoritar([2,8,7,2,2,5,2,3,1,2,2]))