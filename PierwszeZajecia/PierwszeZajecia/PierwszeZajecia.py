'''
#Zadanie 1

def x4(x):
    x2=x*x #pierwsze mnożenie
    x4=x2*x2 #drugie
    print(f"Obliczane dla liczby {x}")
    print(f"x4 w 2 mnozeniach to {x4}")

def x6(x):
    x2=x*x #pierwsze mnożenie
    x4=x2*x2 #drugie
    x6 = x4 *x2 #trzecie
    print(f"Obliczane dla liczby {x}")
    print(f"x6 w 3 mnozeniach to {x6}")

def x7(x):
    x2=x*x #pierwsze mnożenie
    x4=x2*x2 #drugie
    x6 = x4 *x2 #trzecie
    x7 = x6* x #czwarte
    print(f"Obliczane dla liczby {x}")
    print(f"x7 w 4 mnozeniach to {x7}")

def x8(x):
    x2=x*x #pierwsze mnożenie
    x4=x2*x2 #drugie
    x8 = x4*x4 #trzecie
    print(f"Obliczane dla liczby {x}")
    print(f"x8 w 3 mnozeniach to {x8}")

def x3ix10(x):
    #nie da sie w 4 mnożeniach
    x2=x*x #pierwsze mnożenie
    x3=x2*x #drugie
    x6=x3*x3 #trzecie
    x9=x6*x3 #czwarte
    x10=x9*x #piate
    sumax3ix10 = x3+x10
    print(f"Obliczane dla liczby {x}")
    print(f"x3 + x10 w 4 mnozeniach i 1 dodawaniu to {sumax3ix10}")

def x5ix13(x):
    x2=x*x #pierwsze mnożenie
    x4=x2*x2 #drugie
    x5=x4*x #trzecie
    x9=x5*x4 #czwarte
    x13=x9*x4 #piate
    sumax5ix13 = x5+x13
    print(f"Obliczane dla liczby {x}")
    print(f"x5 + x13 w 5 mnozeniach i 1 dodawaniu to {sumax5ix13}")

def x2ix5ix17(x):
    x2=x*x #pierwsze mnożenie
    x4=x2*x2 #drugie
    x5=x4*x #trzecie
    x10=x5*x5 #czwarte
    x15=x10*x5 #piate
    x17=x15*x2 #szoste
    sumax2ix5=x2+x5
    sumax2ix5ix17=sumax2ix5+x17
    print(f"Obliczane dla liczby {x}")
    print(f"x2 + x5 + x17 w 5 mnozeniach i 1 dodawaniu to {sumax2ix5ix17}")


#Zadanie 2
def suma3liczbale2zmienne(a,b,c):
    a=a+b
    a=a+c
    print(f"Suma 3 liczb z użyciem 2 zminnych wynosi {a}")


#Zadanie 3
def figura():
    import math    
    wybor=int(input("Co wybierasz? 1-ostrosłup (kwadratowy) 2-walec 3-sześcian "))
    if wybor==1: #ostrosłup
        print("podaj wymiary")
        a = float(input("Długość krawędzi podstawy: "))
        h = float(input("Wysokość ostrosłupa: "))
        objętość = (a**2 * h) / 3
        pole_podstawy = a**2
        pole_bocznej = 2 * a * math.sqrt((a / 2)**2 + h**2)
        pole_całkowite = pole_podstawy + pole_bocznej
    elif wybor==2: #walec
        print("podaj wymiary")
        r = float(input("Promień podstawy walca: "))
        h = float(input("Wysokość walca: "))
        objętość = math.pi * r**2 * h
        pole_podstawy = math.pi * r**2
        pole_bocznej = 2 * math.pi * r * h
        pole_całkowite = 2 * pole_podstawy + pole_bocznej
    elif wybor==3: #sześcian
        print("podaj wymiary")
        a = float(input("Długość krawędzi: "))
        objętość = a**3
        pole_podstawy = a**2
        h=a
        pole_bocznej = 4 * a**2
        pole_całkowite = 6 * a**2
    else: print("Podaj inny numer")
    print("\nWyniki obliczeń:")
    print(f"Objętość: {objętość}")
    print(f"Pole podstawy: {pole_podstawy}")
    print(f"Wysokość: {h}")
    print(f"Pole powierzchni bocznej: {pole_bocznej}")
    print(f"Pole powierzchni całkowitej: {pole_całkowite}")


#Zadanie 4
def pole_trojkat(a,b,c):
    import math    
    s = (a + b + c) / 2
    pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Pole trojkata wynosi: {pole}")


#Zadanie 5
def zmiana_kolejnosci(x):
    dlugosc=len(x)
    match dlugosc:
        case 1: print ("za krótkie")
        case 2: 
            text2=x[1]+x[0]
            print(text2)
        case 3:
            text3=x[2]+x[0]+x[1]
            print(text3)
        case 4:
            text4=x[1]+x[0]+x[3]+x[2]
            text4_2=x[3]+x[0]+x[1]+x[2]
            print(text4)
            print(text4_2)
        case _:
            print("Wybrano za dużo znaków")


def samochod(a,b): #a to cena, b to spalanie
    match(a,b):
        case (x,y) if x<=5000 and y<10:
            print("Samochod jest niedrogi i oszczedny")
        case (x,y) if x<=5000 and y>10:
            print("Samochod jest niedrogi i nieoszczedny")  
        case (x,y) if x>5000 and y<10:
            print("Samochod jest drogi i oszczedny")  
        case (x,y) if x>5000 and y>10:
            print("Samochod jest drogi i nieoszczedny")  
'''
