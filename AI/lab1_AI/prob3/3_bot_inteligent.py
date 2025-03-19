
# !pt vectori foarte mari!
# Complexitate timp: O(k), unde k este nr de elemente nenule
# Complexitate spatiala: O(1), unde k este nr de elemente nenule

def produs_scalar_optimizat(v1, v2):
    """
    Variantă optimizată pentru vectori foarte rari,
    folosind dicționare pentru a evita parcurgerea elementelor nule.
    """
    dict_v1 = {i: v1[i] for i in range(len(v1)) if v1[i]}
    dict_v2 = {i: v2[i] for i in range(len(v2)) if v2[i]}

    return sum(dict_v1[i] * dict_v2[i] for i in dict_v1 if i in dict_v2)

if __name__ == '__main__':
    print(produs_scalar_optimizat([1, 0, 2, 0, 3], [1, 2, 0, 3, 1]))