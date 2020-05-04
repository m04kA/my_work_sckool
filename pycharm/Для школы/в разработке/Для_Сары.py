import math

def shifr_matr(shif_fraz):
    mtr_a = []
    for i in range(int(math.sqrt(len(shif_fraz)))): #4
        mtr_a.append([])
        rashod = shif_fraz[i*int(math.sqrt(len(shif_fraz))):i*int(math.sqrt(len(shif_fraz)))+int(math.sqrt(len(shif_fraz)))]#(input().split())
        for j in range(int(math.sqrt(len(shif_fraz)))): #4
            mtr_a[i].append(int(rashod[j]))
    return mtr_a

a = [0,12,29,16,9,14,9,8,13]
matr = shifr_matr(a)
print(matr)

























def insertion_together(mass):
    for k in range(0, len(mass), 2):
        el_1 = k
        el_2 = k + 1
        bufer_1 = mass[k]
        bufer_2 = mass[k + 1]
        if bufer_1 > bufer_2:
            bufer_2 = mass[k]
            bufer_1 = mass[k + 1]
        for i in range(k - 1, -1, -1):
            if mass[i] > bufer_2:
                mass[el_2] = mass[i]
                el_2 -= 1
                el_1 -= 1
            elif mass[i] > bufer_1:
                mass[el_1] = mass[i]
                el_1 -= 1
        mass[el_1] = bufer_1
        mass[el_2] = bufer_2
    return mass