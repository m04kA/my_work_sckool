k = 3
alph = ['a', 'b',               '    cdefghigklmnopqrstuvwxyz']
l = 'abc'


def CeasarCipher(s, k):
    global alph
    temp = []
    for i in s:
        if i == ' ':
            temp.append(' ')
        else:
            ind = alph.index(i)
            temp.append(alph[(ind + k) % 27])
    return temp

print(CeasarCipher(l, 3))
