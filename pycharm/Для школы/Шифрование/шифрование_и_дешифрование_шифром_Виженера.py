fraza = input('Введите вашу фразу: ').lower().split()
kod = input('Введите гамму: ').lower().split()

alfovit = {
    'а': None, 'б': None, 'в': None, 'г': None, 'д': None, 'е': None, 'ё': None, 'ж': None, 'з': None, 'и': None,
    'й': None, 'к': None, 'л': None, 'м': None,
    'н': None, 'о': None, 'п': None, 'р': None, 'с': None, 'т': None, 'у': None, 'ф': None, 'х': None, 'ц': None,
    'ч': None, 'ш': None, 'щ': None, 'ъ': None,
    'ы': None, 'ь': None, 'э': None, 'ю': None, 'я': None,
}


def alf(alfo):
    for idx, key in enumerate(alfo.keys(), 1):
        alfo.update({key: idx})
    return alfo


def frz(frza):
    answ = ''
    for el in frza:
        answ = answ + ''.join(str(el))
    return answ


def preobr(words, alf):
    mas_word = []
    for key in words:
        mas_word.append(alf[key])
    return mas_word


def get_key(slov, value):
    for k, v in slov.items():
        if v == value:
            return k


alfovit = alf(alfovit)
fraza = frz(fraza)
kod = frz(kod)
fraza = preobr(fraza, alfovit)
kod = preobr(kod, alfovit)


def coding(frza, gamm):
    gamma = []
    g = 0
    for idx in range(len(fraza)):
        if g == len(gamm):
            g = 0
        gamma.append(gamm[g])
        g += 1
    for idx in range(len(frza)):
        if frza[idx] + gamma[idx] % 33 == 0:
            frza[idx] = 33
        else:
            frza[idx] = (frza[idx] + gamma[idx])%33
    return frza


def decoding(frza, gamm):
    gamma = []
    g = 0
    for idx in range(len(fraza)):
        if g == len(gamm):
            g = 0
        gamma.append(gamm[g])
        g += 1
    for idx in range(len(frza)):
        if frza[idx] - gamma[idx] < 1:
            frza[idx] = 33 + frza[idx] - gamma[idx]
        else:
            frza[idx] = frza[idx] - gamma[idx]
    return frza


fraza = coding(fraza, kod)


def ansv(frz, alf):
    my_fraz = ''
    for el in frz:
        my_fraz = my_fraz + str(get_key(alf, el))
    return my_fraz



fraza = ansv(fraza, alfovit)
print(fraza)
fraza = preobr(fraza, alfovit)

fraza = decoding(fraza, kod)

fraza = ansv(fraza, alfovit)
print(fraza)
