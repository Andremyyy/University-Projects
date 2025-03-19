# Să se determine al k-lea cel mai mare element al unui șir de numere cu n elemente (k < n).
# De ex. al 2-lea cel mai mare element din șirul [7,4,6,3,9,1] este 7.

# Complexitate timp: O(n log n), pt ca sortez numerele
# Complexitate spatiala: O(1), pt ca nu folosesc structuri de date suplimentare

def al_k_lea_element(sir, k):
    """
    Determină al k-lea cel mai mare element dintr-un șir de numere.

    Metodă:
        1. Sortează șirul în ordine descrescătoare.
        2. Returnează elementul de pe poziția k-1.

    :param sir: Listă de numere întregi.
    :param k: Poziția elementului dorit (1 ≤ k < n).
    :return: Al k-lea cel mai mare element.

    """

    sir.sort( reverse=True)
    return sir[k - 1]

def test_al_k_lea_element():
    assert (al_k_lea_element([7, 4, 6, 3, 9, 1], 2)) == 7
    assert (al_k_lea_element([10, 20, 30, 40, 50], 1)) == 50
    assert (al_k_lea_element([3, 1, 2, 5, 4], 3))  == 3
    assert (al_k_lea_element([100, 200, 300, 400, 500], 5)) ==100
    assert (al_k_lea_element([8, 10, 2, 5, 7], 4)) == 5
    print("Testele au trecut cu succes!")

if __name__ == '__main__':
    test_al_k_lea_element()
    print(al_k_lea_element([7,4,6,3,9,1], 2))