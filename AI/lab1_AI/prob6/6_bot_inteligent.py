# Complexitate timp: O(n), pt ca parcurg sirul
# Complexitate spatiala: O(1), pt ca folosesc un variabile simple suplimentare

def element_majoritar_optimizat(sir):
    """
    Identifică elementul majoritar dintr-un șir (apare de mai mult de n/2 ori).

    Algoritmul lui Boyer-Moore:
    - Inițializăm un candidat și un contor.
    - Parcurgem șirul, incrementăm contorul dacă numărul coincide cu candidatul sau îl resetăm altfel.
    - Verificăm dacă elementul găsit este cu adevărat majoritar.


    :param sir: Listă de numere întregi.
    :return: Elementul majoritar sau None dacă nu există.
    """
    candidat, contor = None, 0

    for numar in sir:
        if contor == 0:
            candidat = numar
        contor += (1 if numar == candidat else -1)

    if sir.count(candidat) > len(sir) // 2:
        return candidat

    return None

if __name__ == '__main__':
    print(element_majoritar_optimizat([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]))