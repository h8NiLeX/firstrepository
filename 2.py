print("Конвертер: км, м, см, мм, мили, ярды")
number = float(input("Число: "))
iz = input("Из (км/м/см/мм/мили/ярды): ").lower()
v = input("В (км/м/см/мм/мили/ярды): ").lower()
in_meters = {
 'км': number * 1000,
 'м': number,
 'см': number * 0.01,
 'мм': number * 0.001,
 'мили': number * 1609.344,
 'ярды': number * 0.9144
}
result = in_meters[iz] / {
 'км': 1000,
 'м': 1,
 'см': 0.01,
 'мм': 0.001,
 'мили': 1609.344,
 'ярды': 0.9144
}[v]
print(f"{number} {iz} = {result} {v}")