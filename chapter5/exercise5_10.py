# 5.10 (Anagrams) An anagram of a string is another string formed by rearranging the letters
# in the first. Write a script that produces all possible anagrams of a given string using
# only techniques that you’ve seen to this point in the book. [The itertools module provides
# many functions, including one that produces permutations.]


# Creer des permutations
# Voir algorithme de Heap en fixant l'element de droite
def permute(liste):
    liste = list(liste)
    result = []
    if len(liste) == 1:
        return [liste[:]]

    for i in range(len(liste)):
        valeur_fixe = liste.pop(0)

        perms = permute(liste)

        for perm in perms:
            perm.append(valeur_fixe)
        result.extend(perms)
        liste.append(valeur_fixe)
    return result


permute('allo')
