"""
i = "si"
while i=="si":
    operazione = int(input("selezione operazione\n1-somma\n2-sottrazione\n3-moltiplicazione\n4-divisione\n"))
    risultato = str("il risultato è: ") #ho creato una variabile stringa che mi tornerà utile nella calcolatrice 
    
    if operazione == 1: #if per gestire la selezione dell'operazione e eseguirla
        num1 = int(input()) 
        num2 = int(input())
        print(risultato, num1+num2)
    elif operazione == 2:
        num1 = int(input()) 
        num2 = int(input())
        print(risultato, num1-num2)
    elif operazione == 3:
        num1 = int(input()) 
        num2 = int(input())
        print(risultato, num1*num2)
    elif operazione == 4: #in caso di divisione ho aggiunto delle opzioni
        num1 = int(input()) 
        num2 = int(input())
        if num1 == 0:
            print("impossibile")
        elif num2 == 0:
            print("infinitoo")
        else:
            print(risultato, num1/num2)
    else:
        print("non hai selezionato un'opzione valida") 
    i = str(input("continuare?"))

"""

continuare = "si"
while continuare == "si":
    num1 = float(input())
    operatore = str(input())
    num2 = float(input())
    if operatore == ">":
        if num1 > num2:
            print(num1, "è maggiore di ", num2)
        else:
            print(num1, "non è maggiore di ", num2)
    elif operatore == "<":
        if num1<num2:
            print(num1, "è minore di", num2)
        else:
            print(num1, "non è minore di ", num2)
    elif operatore == "=":
        if num1==num2:
            print("i due numeri sono uguali")
        else:
            print("i due numeri non sono uguali")
    else:
        print("operazione non contemplata")
    continuare = str(input("continuare?\n"))
