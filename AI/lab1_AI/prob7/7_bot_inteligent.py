import heapq

# Complexitate timp: O(n log k), pt ca sortez numerele si retin doar k elemente
# Complexitate spatiala: O(k), pt ca stochez k elemente

def al_k_lea_element_optimizat(sir, k):
    """
    Determină al k-lea cel mai mare element dintr-un șir de numere folosind un heap minim.

    Metodă:
        1. Se utilizează heapq.nlargest(k, sir), care construiește un heap minim cu k elemente cele mai mari.
        2. Se returnează ultimul element din această listă, care este al k-lea cel mai mare.

    :param sir: Listă de numere întregi.
    :param k: Poziția elementului dorit (1 ≤ k < n).
    :return: Al k-lea cel mai mare element.

    """

    return heapq.nlargest(k, sir)[-1]

if __name__ == '__main__':
    print(al_k_lea_element_optimizat([7, 4, 6, 3, 9, 1], 2))