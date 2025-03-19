from collections import deque
# Complexitate timp: O(n), pt ca parcurg numerele si calculez reprezentarea binara intr-o coada
# Complexitate spatiala: O(n), pt ca stochez cifrele binare intr-o coada suplimentara

def numere_binare_optimizat(n):
    """ Generează numerele binare de la 1 la n folosind o coadă. """

    rezultat = []
    coada = deque(["1"])

    for _ in range(n):
        num = coada.popleft()
        rezultat.append(num)
        coada.append(num + "0")
        coada.append(num + "1")

    return rezultat

if __name__ == '__main__':
    print(numere_binare_optimizat(4))


