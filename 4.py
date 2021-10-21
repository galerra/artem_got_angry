k = str(input())
p = input()
x = list(p)
q = []
y =[]
n = 0
m = 1
while m <= len(x):
	q.append(x[n])
	q.append(x[m])
	j = [q[-2],q[-1]]
	y.append(j)
	n += 2
	m += 2

w = -1
for i in y:
        if i[0] + i[1] == k:
		w = sym = i[0] + i[1]
		ind = y.index(i) + 1
		break
	for j in i:
		if j == k:
			ind = y.index(i) + 1
			sym = i[0] + i[1]
			break
print('Индекс числа:',ind)
print('Само число:',sym)
print('k-ая цифра',k)


