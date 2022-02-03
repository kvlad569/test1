# вводим в консоль цифры
text = input()

s = text.replace(" ", "")# убираем пробелы
s = " ".join(s)
l = s.split()
k = []

for i in range(0,len(l)):
    k.append(str(max(l)))
    l.remove(max(l))
res ="".join(k)
print(res)















