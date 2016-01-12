# coding: utf-8 
def getNext(password):
    """
    Série de tests exprimés en doctest
    >>> getNext('a')
    'b'
    >>> getNext('az')
    'ba'
    >>> getNext('bc')
    'bd'
    """
    pwd = list(password)  # initialisation de pwd ,une liste de lettre de charactere de password ( passe en parametre dans la fonction )
    found = False
    i=len(pwd)-1
    
    while not found:
        if pwd[i] < 'z':
           pwd[i] = chr(ord(pwd[i])+1)  #2 On passe à la lettre suprérieur si le carctère est inférieur a Z sinon on passe à la lettre precedent de la liste
           found = True             
        else:
           pwd[i] = 'a'
           i = i-1 
    
    return ''.join(pwd) #3 On le retourne le mot de passe en 1 seule chaîne de caracteres
     
     
     
# Grâce à ce fragment de code, si vous exécutez ce fichier, les tests doctests seront exécutés également. 
# Si vous ne voulez plus que les tests s'exécutent, commentez les deux lignes ci-dessous. 
# Si vous préférez lancer vos tests à la main, commentez également les lignes, et utilisez "python -m doctest pass.py" en console. 
if __name__ == "__main__":
    import doctest
    doctest.testmod()

