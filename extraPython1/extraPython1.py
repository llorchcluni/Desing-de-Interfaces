

def max(a, b):
    if (b > a):
        return b
    else:
        return a

def max_de_tres(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if (b > c):
            return b
        else:
            return c

def longCad(n):
    i = 0
    cont = 0

    for i in range (len(n)):
        cont = cont + 1
    return cont
def esVocal(n):
    rang = 'aeiouáéíóúü'
    for i in range(longCad(n)):
        for j in range(longCad(rang)):
            if(rang[j] == n[i]):
                return True
    return False


def mult(n):
    multip = 1
    for i in range(longCad(n)):
        multip *= n[i]
    return multip
def sum(n):
    sum = 1
    for i in range(longCad(n)):
        sum += n[i]
    return sum

def reverse(n):
    cadRev = ''
    for i in range(longCad(n)):
        cadRev += n[longCad(n)-(i+1)]
    return cadRev





