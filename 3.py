a3 = int(input("Введите a1:"))
a2 = int(input("Введите a2:"))
a1 = int(input("Введите a3:"))
b2 = int(input("Введите b1:"))
b1 = int(input("Введите b2:"))
c1 = (a1 + b1) % 10
c2 = (a2 + b2 + (a1 + b1) // 10) % 10
c3 = ((a2 + b2 + (a1 + b1) // 10) // 10) + a3
print("Сотни", c3)
print("Десятки", c2)
print("Единицы", c1)



