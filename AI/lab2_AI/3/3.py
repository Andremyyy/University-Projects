import re
import requests
from bs4 import BeautifulSoup

# a) numarul de propozitii din text
def count_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # regex pentru a găsi propozițiile
    # presupun ca propozitiile sunt delimitate prin ".", "!", "?", ";"
    sentences = re.split(r'[.!?;]+', text)

    # elimin eventualele elemente goale
    sentences = [s.strip() for s in sentences if s.strip()]

    return len(sentences)


#b) numarul de cuvinte din text
def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # impart textul în cuvinte folosind spații și semne de punctuație ca delimitatori

    # \b – Este un delimitator de cuvânt (word boundary).
    #       Se asigură că potrivirea începe și se termină la granița unui cuvânt,
    #       adică unde un caracter de cuvânt (\w) se întâlnește cu un caracter non-cuvânt
    #       (de exemplu, spațiu, semne de punctuatie etc.).
    # \w+ – Caută unul sau mai multe caractere care fac parte dintr-un cuvânt.
    #       \w include litere (mici și mari), cifre și caracterul underscore _.
    #       Semnul + indică faptul că trebuie să existe cel puțin un astfel de caracter.
    # \b – Finalizează potrivirea la sfârșitul cuvântului.

    words = re.findall(r'\b\w+\b', text)

    return len(words)


#c) numarul de cuvinte DIFERITE din text
def count_unique_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # toate cuvintele
    # le convertesc la lowercase pentru a elimina diferențele de litere mari/mici
    words = re.findall(r'\b\w+\b', text.lower())

    # un set pentru a număra doar cuvintele unice
    unique_words = set(words)

    return len(unique_words), unique_words

# d) cel mai lung si cel mai scurt cuvant(cuvinte)
# ma folosesc de set-ul de cuvinte unice aflat mai devreme

def find_shortest_longest_words(unique_words):
    if not unique_words:
        return None, None

    #determin cea mai mica/mare lungime din unique_words
    min_length = min(len(word) for word in unique_words)
    max_length = max(len(word) for word in unique_words)

    #extrag toate cuvintele care au lungimea minima/maxima
    shortest_words = [word for word in unique_words if len(word) == min_length]
    longest_words = [word for word in unique_words if len(word) == max_length]

    return shortest_words, longest_words

#e) textul fara diacritice

# def english_text(filepath):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         text = file.read()
#     text = text.replace("ă", "a").replace("â", "a").replace("î", "i") \
#                .replace("ș", "s").replace("ț", "t") \
#                .replace("Ă", "A").replace("Â", "A").replace("Î", "I") \
#                .replace("Ș", "S").replace("Ț", "T")
#     return text


def remove_diacritics(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    mapping = str.maketrans("ăâîșțĂÂÎȘȚ", "aaistAAIST")
    return text.translate(mapping)


#f)sinonimele celui mai lung cuvant din text
#todo: nu merge aceasta functie
def get_synonyms(word):
    url = f'https://www.dictionardesinonime.ro/?c={word}'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        synonyms = []

        # gasesc toate paragrafele care conțin sinonime
        for p in soup.find_all('p'):
            if 'Sinonime:' in p.text:
                # sinonimele sunt în paragraful următor celui care conține "Sinonime:"
                next_p = p.find_next_sibling('p')
                if next_p:
                    synonyms = next_p.get_text(strip=True).split(', ')
                    break  # gasesc doar primul set de sinonime

        return synonyms if synonyms else ["Nu s-au găsit sinonime"]

    return ["Eroare la accesarea dictionardesinonime.ro"]



if __name__ == '__main__':

    file_path = "C:/Users/ema_a/Desktop/AI/texts.txt"
    nr_propozitii = count_sentences(file_path)
    print(f'Numărul de propoziții din text: {nr_propozitii}')

    nr_cuvinte = count_words(file_path)
    print(f'Numărul de cuvinte din text: {nr_cuvinte}')

    nr_cuvinte_unice, cuvinte_unice = count_unique_words(file_path)
    print(f"Numarul de cuvinte unice este: {nr_cuvinte_unice}")

    cele_mai_scurte_cuvinte, cele_mai_lungi_cuvinte = find_shortest_longest_words(cuvinte_unice)
    print(f"f Cele mai scurte cuvinte sunt: {cele_mai_scurte_cuvinte}")
    print(f"Cele mai lungi cuvinte sunt: {cele_mai_lungi_cuvinte}")

    text_fara_diacritice = remove_diacritics(file_path)
    print(f"Textul fara diacritice este \n {text_fara_diacritice}")

    sinonim_cel_mai_mare_cuvant = {word: get_synonyms(word) for word in cele_mai_lungi_cuvinte}
    test = get_synonyms("confirmare")
    print(f"Sinonimul cuvantului cel mai lung este: {sinonim_cel_mai_mare_cuvant}, "
          f"iar pentru 'confirmare' este: {test}" )




