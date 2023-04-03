import random

#vytvornie funkcie pre triedenie
def partition(pole, low, high):

    #zvolenie elementu najviac v pravo
    pivot = pole[high]

    #pointer pre vacsi element
    i = low -1

    #prechadzanie cez vsetky elementy
    #porovnanie kazdeho elementu s pivotom
    for j in range(low, high):
        if(pole[j] <= pivot):
            #ak je element mensi ako pivot najdeny
            #vymen pivot s vacsim elementom
            i = i + 1

            #vymen element za i elementom j
            (pole[i], pole[j]) = (pole[j], pole[i])

    #vymen pivot element s vacsim elementom urcenym i
    (pole[i + 1], pole[high]) = (pole[high], pole[i + 1])

    #vrat poziciu na ktorej je urobnena particia
    return i+1

#funkcia na vykonanie quick sortu
def quick_sort(pole, low, high):
    if (low < high):

        #najdi pivot elementi ako taky
        #element mensi ako pivot je na lavej strane
        #element vacsi ako pivot je na pravej strane
        pi = partition(pole, low, high)

        #recrusivne vlanie na lavi pivot
        quick_sort(pole, low, pi-1)

        #recrusivne volanie na pravo od pivotu
        quick_sort(pole, pi + 1, high)

#spustenie kodu

if __name__ == "__main__":
    print("Quick sort algoritmus")
    #urcenie velkosti pola a maximalnu hodnotu nahodnych cisel v poli
    velk = int(input("Zadaj velkost pola: "))
    max = int(input("Zadaj maximum: "))

    pole = [0]*velk

    #naplnenie pola cislami
    for i in range(len(pole)):
        pole[i] = random.randint(0, max)
    
    #vypisanie pola
    print("Neutriedene pole je: ", pole)
    quick_sort(pole, 0, len(pole) - 1)
    print("Utriedene pole je: ", pole)