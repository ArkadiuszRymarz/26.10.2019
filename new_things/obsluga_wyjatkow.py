# zmienna = input("Podaj liczbę")
#
# try:
#     zmienna_integer = int(zmienna)
#     print(f"To jest liczba {zmienna_integer}.")
# except Exception:
#     print("Nie byłem w stanie zrzutować na inta")
#
# print("Koniec")



zmienna_1 = input("Podaj liczbę :")
zmienna_2 = input("Podaj liczbę :")

try:
    a = int(zmienna_1)
    b = int(zmienna_2)
    print(f"Suma liczb to {a+b}.")
except Exception:
    print("Nie byłem w stanie zrzutować na inta")

print("Koniec")