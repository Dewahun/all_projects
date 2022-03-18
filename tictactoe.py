
import random

kezdés = random.randint(0,1) #későbbi AI-hoz kell
rács = [[], [], []]

for i in range(3):
    for e in range(3):
        rács[e].append(0) #nulla a nincs döntés

játékos1 = []
játékos1Q = str(input("'A' Játékos jele: "))
játékos1_név = input("Neve: ")
játékos2 = []
játékos2Q = str(input("'B' Játákos jele: "))
játékos2_név = input("Neve: ")
mehet = True


def kiírás(rács):
    print(f"{rács[0]}\n{rács[1]}\n{rács[2]}")

def beírás(játékos):
    rács[játékos[1]][játékos[2]] = játékos[0]
    if játékos[0] == "a":
        játékos2.clear()
    else:
        játékos1.clear()
    return rács

def játékosA():
    játékos1.append(játékos1Q)
    játékos1.append(int(input("Melyik sor (A): ")) - 1)
    játékos1.append(int(input("Melyik oszlop (A): ")) - 1)
    if rács[játékos1[1]][játékos1[2]] == 0 or rács[játékos1[1]][játékos1[2]] != játékos2Q:
        return játékos1
    else:
        print("Foglalt!\n"), játékos1.clear()
        return játékosA()

def játékosB():
    játékos2.append(játékos2Q)
    játékos2.append(int(input("Melyik sor (B): ")) - 1)
    játékos2.append(int(input("Melyik oszlop (B): ")) - 1)
    if rács[játékos2[1]][játékos2[2]] == 0 or rács[játékos2[1]][játékos2[2]] != játékos1Q:
        return játékos2
    else:
        print("Foglalt!\n"), játékos2.clear()
        return játékosB()

def ellenőrzés(rács):
    x = ""
    y = ""
    for i,sor in enumerate(rács):
        for e,kar in enumerate(sor):
            x += str(rács[i][e])
            y += str(rács[e][i])
        if x == játékos1Q * 3 or x == játékos2Q * 3 or y == játékos1Q * 3 or y == játékos2Q * 3:
            return True
        elif (rács[0][0] == játékos1Q or rács[0][0] == játékos2Q) and (rács[0][1] == játékos1Q or rács[0][1] == játékos2Q) and (rács[0][2] == játékos1Q or rács[0][2] == játékos2Q):
              return True
        elif (rács[0][2] == játékos1Q or rács[0][2] == játékos2Q) and (rács[1][1] == játékos1Q or rács[1][1] == játékos2Q) and (rács[2][0] == játékos1Q or rács[2][0] == játékos2Q):
            return True
        else:
            x = ""
            y = ""
            return False
def nyerta():
    játékos1_pont = 0
    játékos2_pont = 0
    for sor in rács:
        for kar in sor:
            if kar == játékos1Q:
                játékos1_pont += 1
            elif kar == játékos2Q:
                játékos2_pont += 1
            else:
                pass
    if játékos1_pont > játékos2_pont:
        return print(f"{játékos1_név} nyert!")
    else:
        return print(f"{játékos2_név} nyert!")


#játék:

while mehet:
    if ellenőrzés(rács) == False:
        beírás(játékosA())
        ellenőrzés(rács)
        kiírás(rács)
        if ellenőrzés(rács) == False:
            beírás(játékosB())
            ellenőrzés(rács)
            kiírás(rács)
            if ellenőrzés(rács) == False:
                pass
            else:
                nyerta(rács)
                mehet = False
        else:
            nyerta()
            mehet = False
    else:
        nyerta()
        mehet = False

