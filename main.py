#### Imports et définition des variables globales
"""f"""
import sys

#### Fonctions secondaires
def artcode_i(s):
    """

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    car = [s[0]]
    occ = [1]
    n = len(s)
    for i in range(1, n):
        if s[i] == s[i-1]:
            occ[-1] += 1
        else:
            car.append(s[i])
            occ.append(1)
    l = list(zip(car, occ,strict=True))
    return l
def artcode_r(s):
    """
    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    sys.setrecursionlimit(4000)
    # votre code ici
    n = len(s)  # Longueur de la chaîne
    if not s:
        return []
    base = s[0]
    c = 1
    for i in range(1, n):
        if s[i] == base:
            c += 1
        else:
            break
    return [(base, c)] + artcode_r(s[c:])
#### Fonction principale
def main():
    """dd"""
    print(artcode_i('nikolalebogoss'))
    print(artcode_r('nikolalebogoss'))

if __name__ == "__main__":
    main()
