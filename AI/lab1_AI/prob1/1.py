# Să se determine ultimul (din punct de vedere alfabetic)
# cuvânt care poate apărea într-un text care conține mai multe
# cuvinte separate prin ” ” (spațiu). De ex. ultimul (dpdv alfabetic)
# cuvânt din ”Ana are mere rosii si galbene” este cuvântul "si".



# Complexitate timp: O(m log m) unde m este nr de cuvinte
# Complexitate spatiala: O(m)



def sort_words(words):
    """
        Determină ultimul cuvânt în ordine alfabetică (lexicografică) dintr-un text.

        :param words: Un șir de caractere care conține mai multe cuvinte separate prin spații.
        :return: Cuvântul care apare ultimul în ordine alfabetică (ignorând majusculele).

        Algoritm:
        1. Se împarte șirul `words` într-o listă de cuvinte folosind `split()`, care elimină spațiile inutile.
        2. Se sortează lista în ordine descrescătoare, utilizând `str.casefold()`
           pentru a face sortarea netinand cont de majuscule.
        3. Se returnează primul element din lista sortată, care este ultimul lexicografic.

        """
    parts = words.split(' ')
    sorted_words = sorted(parts, key = str.casefold, reverse = True)
    return sorted_words[0]


def test_sort_words():
    assert sort_words("măr gutui caisă prună") == "prună"
    assert sort_words("X y Z") == "Z"
    assert sort_words("zebra avion carte") == "zebra"
    assert sort_words("a aa aaa aaaa") == "aaaa"
    print("Testele au trecut cu succes!")


if __name__ == '__main__':
    test_sort_words()
    words = input()
    print(sort_words(words))
