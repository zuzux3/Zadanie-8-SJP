para1 = float(input("Podaj pierwszy parametr: "))
para2 = float(input("Podaj drugi parametr: "))
para3 = float(input("Podaj trzeci parametr: "))

parametrFinal = para1 * para2 * para3

if para1 == para2 and para2 == para3:
    print("Wynik koncowy: {}".format(parametrFinal * 2))
else:
    print("Wynik koncowy: {}".format(parametrFinal))