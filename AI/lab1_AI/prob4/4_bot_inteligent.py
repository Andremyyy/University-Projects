# Complexitate timp: O(n), pt ca parcurg o singura data textul
# Complexitate spatiala: O(n), pt ca folosesc un dictionar pt frecventa

def cuvinte_unice_optimizat(text):
    """
    Determină cuvintele care apar exact o singură dată într-un text, folodind un DICTIONAR.

    :param text: String cu textul de analizat
    :return: Listă cu cuvintele care apar o singură dată
    """
    frecventa = {}

    for cuvant in text.split():
        frecventa[cuvant] = frecventa.get(cuvant, 0) + 1

    return [cuvant for cuvant in frecventa if frecventa[cuvant] == 1]

if __name__ == '__main__':
    print(cuvinte_unice_optimizat("ana are ana are mere rosii ana"))