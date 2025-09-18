a = float(input("Введите значение первой стороны: "))
b = float(input("Введите значение второй стороны: "))
c = float(input("Введите значение третьей стороны: "))
p = (a + b + c) / 2
pl = (p*(p - a) * (p - b) * (p - c))**0.5
pl = round(pl, 2)
print(pl)
