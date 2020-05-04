
alfovit = {
    'а': None, 'б': None, 'в': None, 'г': None, 'д': None, 'е': None, 'ё': None, 'ж': None, 'з': None, 'и': None,
    'й': None, 'к': None, 'л': None, 'м': None,
    'н': None, 'о': None, 'п': None, 'р': None, 'с': None, 'т': None, 'у': None, 'ф': None, 'х': None, 'ц': None,
    'ч': None, 'ш': None, 'щ': None, 'ъ': None,
    'ы': None, 'ь': None, 'э': None, 'ю': None, 'я': None,
}

def alf(alfo):
    for idx, key in enumerate(alfo.keys()):
        alfo.update({key: idx})
    return alfo


def preobr(words, alf):
    mas_word = []
    for key in words:
        mas_word.append(alf[key])
    return mas_word

def get_key_dict(slov, value):
    for k, v in slov.items():
        if v == value:
            return k

def frz(frza):
    answ = ''
    for el in frza:
        answ = answ + ''.join(str(el))
    return answ

def get_keys(e_num, yel_num):
    answ = []
    d = 0
    while len(answ) < 2:
        if (d*e_num)%yel_num == 1:
            answ.append(d)
        d += 1
    return answ

def dvoich(num):
    per_dvo = bin(num)[2:]
    return len(per_dvo)-1

def bin_text(mass):
    answ = ''
    for el in mass:
        answ += '0'*(6-len(bin(el)[2:])) + bin(el)[2:] #+ ' '
    return answ

def razbitie_na_dvoich(kod):
    answ = []
    bitt = dvoich(my_key[1]) #равна 4
    for idx in range(0, len(kod), bitt):
        answ.append(kod[idx:(idx+ bitt)] +'0'*(bitt-len(kod[idx:(idx+ bitt)])))
    return answ

def desitic_cisl(mass):
    answ = []
    for el in mass:
        answ.append(int(str(el), base=2))
    return answ

def coding(mass, e, n):
    answ = []
    for el in mass:
        answ.append((el**e)%n)
    return answ

p = 7#int(input())
q = 3#int(input())

n = p*q
yel = (p-1)*(q-1)
e = 5#nt(input(f'Введите простое чиосло меньше {yel}:'))

hide_keys = get_keys(e, yel)
my_key = [e, n]
print(f'Открытый ключ [e, n]: {my_key}')
hide_key = 17#int(input(f'Выберете одно из этих чисел {hide_keys} и введите его: '))
print('Принято')
hide_keys = [hide_key, n]
print(f'Закрытый ключ [d, n]: {hide_keys}')

fraza = 'приветт'#input('Введите вашу фразу: ').lower().split()
alfovit = alf(alfovit)
fraza = frz(fraza)
fraza = preobr(fraza, alfovit)
dvoi_fraz = bin_text(fraza)
print(dvoi_fraz)
dvoi_fraz = razbitie_na_dvoich(dvoi_fraz)
print(dvoi_fraz)
dvoi_fraz = desitic_cisl(dvoi_fraz)
print(dvoi_fraz)
dvoi_fraz = coding(dvoi_fraz, e, my_key[1])
print(f'Это мы отправляем: {dvoi_fraz}')

