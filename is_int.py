# odp = input("podaj jakas liczbe całkowitą: ")
# try :
#     int(odp)
#     print("tak,to jest liczba całkowita")
# except:
#     print("nie podałeś liczby całkowitej")
a = 12
b = 12
c = 2
try:
    print (a + c)
    print(a * b)
    print(hehehe)
except ZeroDivisionError :
    print("próba dzielenia przez zero!")
except TypeError:
    print("niepoprawne dane")
#INNY BŁĄD
except: 
    print("wystąpił nieprzewidziany błąd")
finally:
    #przydatne do zamknięcia połączenia z bazą danych
    #czy był czy nie było,połącznie trzeba zakończyć
    print("FINALLY: wykonam się tak czy siak,a co :)")