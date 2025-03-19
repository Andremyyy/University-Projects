
# # Complexitate timp: O(m) unde m este nr de cuvinte
# # Complexitate spatiala: O(m)

def ultimul_cuvant_optimizat(words):
    """
    Determină ultimul cuvânt în ordine alfabetică (lexicografică) dintr-un text,
    fără a folosi sortare (mai eficient decât `sorted()`).

    :param words: Șir de caractere conținând mai multe cuvinte separate prin spații.
    :return: Cuvântul care apare ultimul în ordine alfabetică (ignorând majusculele).

    **Algoritm:**
    1. Se împarte șirul `words` într-o listă de cuvinte.
    2. Se inițializează `max_word` cu primul cuvânt din listă.
    3. Se parcurg toate cuvintele rămase, comparând lexicografic.
    4. Dacă un cuvânt este mai mare decât `max_word`, se înlocuiește.
    5. Se returnează `max_word` la final.

    """
    parts = words.split()
    max_word = parts[0]

    for word in parts[1:]:
        if word.casefold() > max_word.casefold():
            max_word = word

    return max_word

if __name__ == '__main__':
    print(ultimul_cuvant_optimizat("Ana are mere rosii si galbene"))