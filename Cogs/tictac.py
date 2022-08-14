igralci = ['O', 'X']

def preostalePoteze(polje):
    for i in range(3):
        for j in range(3):
            if (polje[i][j] == ' '):
                return True
    
    return False

def oceniPolozaj(polje) :    
    for vrstica in range(3) :    
        if (polje[vrstica][0] == polje[vrstica][1] and polje[vrstica][1] == polje[vrstica][2]) :       
            if (polje[vrstica][0] == igralci[0]) :
                return 10
            elif (polje[vrstica][0] == igralci[1]) :
                return -10

    for stolpec in range(3) :
        if (polje[0][stolpec] == polje[1][stolpec] and polje[1][stolpec] == polje[2][stolpec]) :
            if (polje[0][stolpec] == igralci[0]) :
                return 10
            elif (polje[0][stolpec] == igralci[1]) :
                return -10

    if (polje[0][0] == polje[1][1] and polje[1][1] == polje[2][2]) :
        if (polje[0][0] == igralci[0]) :
            return 10
        elif (polje[0][0] == igralci[1]) :
            return -10
 
    if (polje[0][2] == polje[1][1] and polje[1][1] == polje[2][0]) :
        if (polje[0][2] == igralci[0]) :
            return 10
        elif (polje[0][2] == igralci[1]) :
            return -10

    return 0


def minimax(polje, globina, jeMax):
    rezultat = oceniPolozaj(polje)
    
    if (rezultat == 10 or rezultat == -10):
        return rezultat
    
    if (not preostalePoteze(polje)):
        return 0
    
    if jeMax:
        naj = -1000
        for i in range(3):
            for j in range(3):
                if (polje[i][j] == ' '):
                    polje[i][j] = igralci[0]
                    naj = max(naj, minimax(polje, globina + 1, not jeMax))
                    polje[i][j] = ' '
        
        return naj
    else:
        naj = 1000
        for i in range(3):
            for j in range(3):
                if (polje[i][j] == ' '):
                    polje[i][j] = igralci[1]
                    naj = min(naj, minimax(polje, globina + 1, not jeMax))
                    polje[i][j] = ' '
        
        return naj

    return naj

def racunalnikPoteza(polje):
    najPostavitev = [-1, -1]
    naj = -1000
    for i in range(3):
        for j in range(3):
            if (polje[i][j] == ' '):
                polje[i][j] = 'O'
                tr = minimax(polje, 0, False)
                if (tr > naj):
                    naj = tr
                    najPostavitev[0] = i
                    najPostavitev[1] = j

                polje[i][j] = ' '
    
    polje[najPostavitev[0]][najPostavitev[1]] = 'O'

def main():
    polje = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]
    
    while True:
        for i in range(3):
            if (i != 0):
                print('---------')
            
            for j in range(3):
                print(polje[i][j], end = '')
                if (j != 2):
                    print(' | ', end = '')
            
            print()
        
        print()

        ocena = oceniPolozaj(polje)

        if (ocena == 10):
            print("zgubil si")
            return 0
        elif(ocena == -10):
            print("zmagal si")
            return 0
        
        if (not preostalePoteze(polje)):
            print("Remi")    
            return 0

        izbira = int(input("Vnesi polje za potezo: "))
        j = int(izbira % 3)
        i = int(izbira / 3)

        polje[i][j] = 'X'

        if (not preostalePoteze(polje)):
            print("Remi")    
            return 0
        
        racunalnikPoteza(polje)
    
    return 0

main()
