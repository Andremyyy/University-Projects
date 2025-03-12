"""
1. Sa se determine oglinditul unui numar.
2. Verificati daca un numar dat este palindrom (=egal cu numarul sau)
ex: 121 palindrom
3.Se da un numar natural k. Sa se determine primul palindrom mai mare decat k dat.
4.Se da o lista cu numere naturale. Sa se returneze o noua lista care contine palindroamele din lista data.

"""


def determinare_oglindit(n):
    """
    Sa se determine oglinditul unui numar.
    :param n: un numar natural
    :return: oglinditul lui n
    """
    t = 0
    while n > 0:
        t = t * 10 + n % 10
        n = n // 10
    return t


def verificare_numar_palindrom(n):
    """
    Verificati daca un numar este palindrom (=inversul sau)
    ex: 121 palindrom
    :param n: un numar natural
    :return: True - n este palindrom,
             False - n nu este palindrom
    """
    ogl = 0
    copie = n
    while n > 0:
        ult_cif = n % 10
        ogl = ogl * 10 + ult_cif
        n = n // 10
    if ogl == copie:
        return True
    return False


def primul_palindrom_mai_mare(k):
    """
    Se da un numar natural k. Sa se determine primul palindrom mai mare decat k dat
    :param k: un numar natural
    :return: primul palindrom mai mare decat k
    """
    ok = True
    k = k + 1
    while ok:
        if verificare_numar_palindrom(k) == 1:
            ok = False
        else:
            k = k + 1

    return k


def generare_lista_palindroame(lista):

    """
    Se da o lista cu numere naturale.
    Sa se returneze o noua lista care contine palindroamele din lista data.
    :param lista: o lista cu numere naturale
    :return: o lista cu palindroamele din l
    """
    rez = []
    for element in lista:
        ogl = 0
        copie = element
        while copie > 0:
            ult_cif = copie % 10
            ogl = ogl * 10 + ult_cif
            copie = copie // 10
        if ogl == element:
            rez.append(element)
    return rez


if __name__ == '__main__':
    # print("Hello")

    # a = int(input("a = "))
    # print("Oglinditul numarului", a, "este ", determinare_oglindit(a))
    # # 6758493
    # print()

    # a = int(input("Numarul de verificat este: "))
    # if verificare_numar_palindrom(a):
    #     print("Numarul", a, "este palindrom")
    # else:
    #     print("Numarul", a, "nu este palindrom")
    # print()

    # a = int(input("a = "))
    # print("Primul palindrom mai mare decat", a, "este", primul_palindrom_mai_mare(a))
    # # 91036282002
    # print()

    lista_data = [234, 545, 7, 1711, 99, 101, 0, 255552]
    print("Lista care contine numai palindroamele din lista data este: ", generare_lista_palindroame(lista_data))
