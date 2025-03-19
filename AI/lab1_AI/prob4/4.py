# Să se determine cuvintele unui text care apar exact o singură dată în acel text.
# De ex. cuvintele care apar o singură dată în ”ana are ana are mere rosii ana" sunt: 'mere' și 'rosii'.

# Complexitate timp: O(n log n), pt ca sortez cuvintele
# Complexitate spatiala: O(n), pt ca stochez cuvintele unice

def cuvinte_unice(text):
    """
        Determină cuvintele care apar exact o singură dată într-un text, sortand lista alfabetic.

        :param text: String cu textul de analizat
        :return: Listă cu cuvintele care apar o singură dată
        """
    parts = text.split(" ")

    parts.sort()

    unice = []
    n = len(parts)

    i = 0
    while i < n:
        if (i == 0 or parts[i] != parts[i - 1]) and (i == n - 1 or parts[i] != parts[i + 1]):
            unice.append(parts[i])
        i += 1

    return unice

def test_cuvinte_unice():
    assert cuvinte_unice("ana are ana are mere rosii ana") == ["mere", "rosii"]
    assert cuvinte_unice("casa mare casa mica casa") == ["mare", "mica"]
    assert cuvinte_unice("test test test test") == []
    assert cuvinte_unice("unu doi trei unu doi trei patru") == ["patru"]
    assert cuvinte_unice("a b c d e f g h i j") == ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    print("Toate testele au trecut!")

if __name__ == '__main__':
    test_cuvinte_unice()
    print(cuvinte_unice("ana are ana are mere rosii ana"))