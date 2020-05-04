alfovit = {
    'а': None, 'б': None, 'в': None, 'г': None, 'д': None, 'е': None, 'ё': None, 'ж': None, 'з': None, 'и': None,
    'й': None, 'к': None, 'л': None, 'м': None,
    'н': None, 'о': None, 'п': None, 'р': None, 'с': None, 'т': None, 'у': None, 'ф': None, 'х': None, 'ц': None,
    'ч': None, 'ш': None, 'щ': None, 'ъ': None,
    'ы': None, 'ь': None, 'э': None, 'ю': None, 'я': None,
}

p = 37#int(input('Простое число p > 33: '))
g = 15#int(input('Первообразный корень числа по модулю p: '))
x = 27#int(input('Выбираем случайное число x такое, что 1 < x < (p-1): '))
y = (g**x) % p
open_key = [p, g, y]
close_key = x


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

def alf(alfo):
    for idx, key in enumerate(alfo.keys(), 1):
        alfo.update({key: idx})
    return alfo

# def get_key_dict(slovar, value):
#     for k, v in slovar.items():
#         if v == value:
#             return k


def get_key_dict(slovar, mass_num):
    answ = ''
    for el in mass_num:
        for k, v in slovar.items():
            if v == el:
                answ += k
    return answ

def coding(mass, keys):
    answ = []
    k = 18 #1 < k < P
    for el in mass:
        a = (keys[1]**k)%keys[0]
        b = ((keys[2]**k) * el) % keys[0]
        answ.append([a,b])
    return answ

def decoding(mass, open, close):
    answ = []
    for el in mass:
        answ.append((el[1]*(el[0]**(open[0]-1-close))) % open[0])
    return answ

print(f'Open keys: {open_key}')
print(f'Close keys: {close_key}')
fraza = 'привет'#.lower().split()
print(f'My fraz: {fraza}')
alfovit = alf(alfovit)
fraza = frz(fraza)
fraza = preobr(fraza, alfovit)
print(f'Fraz whith numb: {fraza}')
fraza = coding(fraza, open_key)
print(f'Coding: {fraza}')
fraza = decoding(fraza, open_key, close_key)
print(f'Decoding: {fraza}')
fraza = get_key_dict(alfovit, fraza)
print(f'My fraz: {fraza}')
