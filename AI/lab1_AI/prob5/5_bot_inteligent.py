# Complexitate timp: O(n), pt ca fac o suma pe elementele vectorului
# Complexitate spatiala: O(1), pt ca nu folosesc structuri de date suplimentare

def valoare_repetata_optimizat(sir):
    """
        Identifică valoarea care se repetă de două ori într-un șir care conține numere de la 1 la n-1.

        Metodă:
        - Se calculează suma teoretică a numerelor de la 1 la n-1 folosind formula sumei aritmetice: S_teoretic = n * (n - 1) / 2.
        - Se calculează suma efectivă a elementelor din șir.
        - Diferența dintre suma efectivă și suma teoretică reprezintă numărul care se repetă.

        :param sir: Listă de numere întregi unde un singur număr apare de două ori.
        :return: Valoarea care se repetă.
        """
    n = len(sir)
    suma_teoretica = (n - 1) * n // 2
    suma_reala = sum(sir)

    return suma_reala - suma_teoretica

if __name__ == '__main__':
    print(valoare_repetata_optimizat([1,2,3,4,2]))