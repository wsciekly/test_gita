import random

los = random.randint(1,10)
ok = True
wynik = 0
print("wylosowałem sobie jakąś liczbe z zakresu 1-10")
print("Zgadniesz jaką???")
print("-" * 17)
while ok :
	wynik += 1
	odp = input("no to podaj mi liczbę")
	try:
		odp = int(odp)
		if odp == los:
			print("no proszę,zgadłeś :) ")
			print(f"twój wynik to: {wynik}")
			ok = False
		else: 
			print("niestety to nie ta liczba")
	except:
		print("nie podałeś liczby całkowitej!")
		wynik -= 1