#skript riesi prvu a druhu cast projektu

import random
import copy

def rozmery_hracej_plochy(n, k):
    #handlovanie zleho vstupu od uzivatela
    if n < 5 or n > 10:
        print("Počet stĺpcov/riadkov môže byť len v rozmedzí 5 až 10")
        return 0

    if k < 1 or k > 4:
        print("Počet hráčov môže byt v rozmedzi 1-4")
        return 0

    return n, k

n, k = rozmery_hracej_plochy(int(input("Zadaj parameter n(rozmer hracej plochy): ")), int(input("Zadaj parameter k(pocet hracov): ")))

def generovanie_hracej_plochy(n):
    zoznam_vsetkych_bodov = []
    ciel_y = n - 1

    if n % 2 == 0:
        ciel_x = 0
    else:
        ciel_x = n-1

    ciel = (ciel_y, ciel_x)

    #vkladanie bodov do zoznamu
    for i in range(n):
        zoznam_vsetkych_bodov.append([])
        for j in range(n):
            if (i,j) == (0, 0):
                zoznam_vsetkych_bodov[i].append("+")
                
            elif (i,j) == (ciel_y, ciel_x):
                zoznam_vsetkych_bodov[i].append("*")

            else:
                zoznam_vsetkych_bodov[i].append(".")

    return zoznam_vsetkych_bodov, ciel

zoznam_vsetkych_bodov, ciel = generovanie_hracej_plochy(n)

def generovanie_teleportov(n, body, ciel):
    slovnik_pozitivnych_teleportov = {}
    slovnik_negativnych_teleportov = {}
    zabrate_indexy = []

    i = 0
    while i != (n//2):
        #generovanie_negativnych_teleportov
        negativny_teleport_zaciatok_y = random.randint(1, n-1)
        if negativny_teleport_zaciatok_y == n-1 and n%2 != 0:
            negativny_teleport_zaciatok_x = random.randint(0, n-2)

        elif negativny_teleport_zaciatok_y == n-1 and n%2 == 0:
            negativny_teleport_zaciatok_x = random.randint(1, n-1)
        else:
            negativny_teleport_zaciatok_x = random.randint(0, n-1)

        negativny_teleport_koniec_y = random.randint(0, negativny_teleport_zaciatok_y-1)
        if negativny_teleport_koniec_y == 0:
            negativny_teleport_koniec_x = random.randint(1, n-1)
        else:
            negativny_teleport_koniec_x = random.randint(0, n-1)

        #overovanie si toho aby sa u roznych teleportov neobjavil ten isty index
        if (negativny_teleport_zaciatok_y, negativny_teleport_zaciatok_x) not in zabrate_indexy and (negativny_teleport_koniec_y, negativny_teleport_koniec_x) not in zabrate_indexy:
            zoznam_vsetkych_bodov[negativny_teleport_zaciatok_y][negativny_teleport_zaciatok_x] = chr(i+97)
            zabrate_indexy.append((negativny_teleport_zaciatok_y, negativny_teleport_zaciatok_x))

            zoznam_vsetkych_bodov[negativny_teleport_koniec_y][negativny_teleport_koniec_x] = chr(i+97)
            zabrate_indexy.append((negativny_teleport_koniec_y, negativny_teleport_koniec_x))

            slovnik_negativnych_teleportov.update({chr(i + 97) : [(negativny_teleport_zaciatok_y, negativny_teleport_zaciatok_x), (negativny_teleport_koniec_y, negativny_teleport_koniec_x)] })
            i+=1

    i = 0
    while i != (n//2):
        #generovanie pozitivnych teleportov
        pozitivny_teleport_zaciatok_y = random.randint(0, n-2)
        if pozitivny_teleport_zaciatok_y == 0:
            pozitivny_teleport_zaciatok_x = random.randint(1, n-1)
        else:
            pozitivny_teleport_zaciatok_x = random.randint(0, n-1)

        pozitivny_teleport_koniec_y = random.randint(pozitivny_teleport_zaciatok_y+1, n-1)
        if pozitivny_teleport_koniec_y == n-1 and n%2 != 0:
           pozitivny_teleport_koniec_x = random.randint(0, n-2)

        elif pozitivny_teleport_koniec_y == n-1 and n%2 == 0:
            pozitivny_teleport_koniec_x = random.randint(1, n-1)
        else:
            pozitivny_teleport_koniec_x = random.randint(0, n-1)

        #overovanie si toho aby sa u roznych teleportov neobjavil ten isty index
        if (pozitivny_teleport_koniec_y, pozitivny_teleport_koniec_x) not in zabrate_indexy and (pozitivny_teleport_zaciatok_y,pozitivny_teleport_zaciatok_x) not in zabrate_indexy:
            zoznam_vsetkych_bodov[pozitivny_teleport_zaciatok_y][pozitivny_teleport_zaciatok_x] = chr(i+65)
            zabrate_indexy.append((pozitivny_teleport_zaciatok_y, pozitivny_teleport_zaciatok_x))

            zoznam_vsetkych_bodov[pozitivny_teleport_koniec_y][pozitivny_teleport_koniec_x] = chr(i+65)
            zabrate_indexy.append((pozitivny_teleport_koniec_y, pozitivny_teleport_koniec_x))
            slovnik_pozitivnych_teleportov.update({chr(i + 65) : [(pozitivny_teleport_zaciatok_y, pozitivny_teleport_zaciatok_x), (pozitivny_teleport_koniec_y, pozitivny_teleport_koniec_x)] })
            i+=1

    return zoznam_vsetkych_bodov, slovnik_pozitivnych_teleportov, slovnik_negativnych_teleportov

zoznam_vsetkych_bodov, slovnik_pozitivnych_teleportov, slovnik_negativnych_teleportov = generovanie_teleportov(n, zoznam_vsetkych_bodov, ciel)

def vypisanie_hracieho_pola(rozmer, zoznam_vsetkych_bodov):
    print("Hracie pole: ")

    #printovanie indexov okolo pola
    print(end = "  ")
    for i in range(rozmer):
        print(i, end = " ")
    print()

    #printovanie pola
    for i in range(rozmer):
        print(i, end = " ")
            
        for j in range(rozmer):
            print(zoznam_vsetkych_bodov[i][j], end = " ")
        print()

    print("============")

vypisanie_hracieho_pola(n, zoznam_vsetkych_bodov)

def hra(n, zoznam_vsetkych_bodov, pocet_hracov):
    slovnik_hracov = {}

    for i in range(k):
        slovnik_hracov.update({i+1 : [0,0]})

    #posuvanie figurok
    y = slovnik_hracov.get(1)[0]
    x = slovnik_hracov.get(1)[1]
    
    while (y,x) != ciel:
        print("Pozicie hracov: ")
        print(f"Hrac c. 1 {slovnik_hracov.get(1)}")
        print("---")

        hod_kockou = 6
        sucet_kocky = 0
        
        while hod_kockou == 6:
            zoznam_vsetkych_bodov_nahrada = copy.deepcopy(zoznam_vsetkych_bodov)

            #hadzanie kockov
            hod_kockou = random.randint(1,6)
            hod_kockou_2 = hod_kockou
            sucet_kocky+=hod_kockou
            
            while hod_kockou != 0:

                #posuvanie figurky v parnom riadku
                if y % 2 == 0:
                    if y == (n-1) and x + hod_kockou > n - 1:
                        print("Hrac c. 1 hodil viac bodov nez je vzdialenost do ciela!")
                        break
                    
                    if x + hod_kockou <= n-1:
                        x += hod_kockou
                        hod_kockou = 0
                                
                    elif x + hod_kockou > n-1:
                        while x != n-1:
                            x += 1
                            hod_kockou -=1
                            
                        y+=1
                        hod_kockou -=1

                        if x - hod_kockou < 0:
                            while x != 0:
                                x -= 1
                                hod_kockou -= 1

                            y+=1
                            hod_kockou -= 1
                        
                            x += hod_kockou
                            hod_kockou = 0

                        else:
                            x -= hod_kockou
                            hod_kockou = 0

                #posuvanie figurky v neparnom riadku
                if y % 2 != 0:
                    if y == (n-1) and x - hod_kockou < 0:
                        print("Hrac c. 1 hodil viac bodov nez je vzdialenost do ciela!")
                        break
                    
                    if x - hod_kockou >= 0:
                        x-= hod_kockou
                        hod_kockou = 0

                    elif x - hod_kockou < 0:
                        while x != 0:
                            x -= 1
                            hod_kockou -= 1
                    
                        y+=1
                        hod_kockou -= 1

                        if x + hod_kockou > n-1:
                            while x != n-1:
                                x += 1
                                hod_kockou -=1
                            
                            y+=1
                            hod_kockou -=1

                            x -= hod_kockou
                            hod_kockou = 0

            zaloha = zoznam_vsetkych_bodov_nahrada[y][x]
            zoznam_vsetkych_bodov_nahrada[y][x] = 1
            slovnik_hracov.update({1 : [y,x]})

            hod_kockou = hod_kockou_2

        print("Hrac c. 1 hodil spolu na kocke: ", sucet_kocky, " bodov")
        print("Hrac c. 1 sa posuva na policko: ", [y,x])

        #aplikacia teleportov
        pocet_teleportov = len(slovnik_pozitivnych_teleportov)

        for j in range(pocet_teleportov):
            value_pozitivna = slovnik_pozitivnych_teleportov[chr(j+65)]
            value_negativna = slovnik_negativnych_teleportov[chr(j+97)]

            if (y,x) == value_pozitivna[0]:
                zoznam_vsetkych_bodov_nahrada[y][x] = zaloha
                y = value_pozitivna[1][0]
                x = value_pozitivna[1][1]
                zoznam_vsetkych_bodov_nahrada[y][x] = 1
                slovnik_hracov.update({1 : [y,x]})
                print(f"Hrac c.1 sa pozitivnym teleportom presuva na policko: ", [y,x])

            if (y,x) == value_negativna[0]:
                zoznam_vsetkych_bodov_nahrada[y][x] = zaloha
                y = value_negativna[1][0]
                x = value_negativna[1][1]
                zoznam_vsetkych_bodov_nahrada[y][x] = 1
                slovnik_hracov.update({1 : [y,x]})
                print("Hrac c.1 sa negativnym teleportom presuva na policko: ", [y,x])
                
        vypisanie_hracieho_pola(n, zoznam_vsetkych_bodov_nahrada)

    print('Hrac c. 1 VYHRAL!')

hra(n, zoznam_vsetkych_bodov, k)

        
        
        

    
    
    
