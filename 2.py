a1 = int(input("Введите a1:"))
a2 = int(input("Введите a2:"))
b1 = int(input("Введите b1:"))
b2 = int(input("Введите b2:"))
c2 = (a2 + b2) % 10
c1 = (a1 * 10 + b1 * 10 + (a2 + b2) //10 )// 10
print("Десятки", c1)
print("Единицы", c2)

