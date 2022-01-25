# Создать переменную типа String
a = 'Olga'
print (type(a), a)

# Создать переменную типа Integer
b = 13
print (type(b), b)

# Создать переменную типа Float
c = 13,3
print (type(c), c)

# Создать переменную типа Bytes
# последовательность чисел в диапазоне 0-255
d = bytes(13)
print(type(d), d)

# Создать переменную типа List
f = [1,"Olga", 1,13]
print(type(f), f)

# Создать переменную типа Tuple
k = (10, 20, 30)
print(type(k), k)

# Создать переменную типа Set
l = {1, 2, 3}
print(type(l), l)

# Создать переменную типа Frozen set
k = {4, 5, 6}
print(type(k), k)

# Создать переменную типа Dict
m = {"key":12}
print(type(m), m)

# Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print ((type(a), a), (type(b), b), (type(c), c), (type(d), d), (type(f), f), (type(k), k), (type(l), l), (type(k), k), (type(m), m) )
# Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
a = 'Olga'
b = 'QA'
c = (a+b)
print(c)

# Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
a = 'Olga'
b = 13
print(a, b)

# Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
a = 'Olga'
b = '13'
print(a + b)
