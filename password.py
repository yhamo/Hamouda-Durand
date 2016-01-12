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
    >>> getNext('zzzzz')
    'erreur'
    >>> hasSeries('abc')
    True
    >>> hasSeries('azbc')
    False
    >>> hasSeries('azbc')
    False
    >>> hasTwoPairs('aaeaa')
    True
    >>> hasTwoPairs('baaac')
    False
    >>> hasNoBadChar('azva')
    True
    >>> hasNoBadChar('azia')
    False
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
        if i == -1:
            return 'erreur'
    return ''.join(pwd) #3 On le retourne le mot de passe en 1 seule chaîne de caracteres
          
def hasSeries(password):
    pwd = list(password)
    i=0
    serie = 0
    while i < len(pwd)-1 :
        if chr(ord(pwd[i])+1) == pwd[i+1] :
            serie = serie + 1
            if serie == 2 :
                return True
        else :
            serie = 0
            
        i = i + 1
    return False

def hasTwoPairs(password):
    pwd = list(password)
    i=0
    paire = 0
    while i < len(pwd)-1 :
        if pwd[i] == pwd[i+1] :
            paire = paire + 1 
            i = i + 1 #on saute pwd[i+1] car dans une paire donc on ne le comparera 
            if paire == 2 :
                return True
        i = i + 1
    return False

def hasNoBadChar(password):
    pwd = list(password)
    i=0
    while i < len(pwd) :
        if pwd[i] == 'o' or pwd[i] == 'l' or pwd[i] == 'i':
            return False
        i = i + 1
    return True
    
# Grâce à ce fragment de code, si vous exécutez ce fichier, les tests doctests seront exécutés également. 
# Si vous ne voulez plus que les tests s'exécutent, commentez les deux lignes ci-dessous. 
# Si vous préférez lancer vos tests à la main, commentez également les lignes, et utilisez "python -m doctest pass.py" en console. 
if __name__ == "__main__":
    import doctest
    doctest.testmod()

