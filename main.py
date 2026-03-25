# 1-m
tekshir = lambda x: "Musbat" if x > 0 else "Manfiy"

print(tekshir(5))
print(tekshir(-3))

# 2-m
son = lambda x: "Juft" if x % 2 == 0 else "Toq"
print(son(24))
print(son(36))

# 3-m
katta_son = lambda a, b: a if a > b else b
print(katta_son(16, 4))
print(katta_son(43, 2))

# 4-m
kicik_son = lambda a, b: a if a < b else b
print(kicik_son(3, 35))
print(kicik_son(45, 9))

# 5-m
son = lambda x: "Katta" if x > 10 else "Kichik"
print(son(13))
print(son(9))

# 6-m
son = lambda x: "teng" if x == 0 else "Teng emas"
print(son(0))
print(son(9))

# 7-m
katta_son = lambda x: "katta" if x > 100 else 'kichik'
print(katta_son(101))
print(katta_son(9))

# 8-m
import math
funk = lambda son: math.fabs(son) if son < 0 else son
print(funk(-23))
print(funk(8))

# 9-m
son = lambda a, b: "Teng" if a == b else "Teng emas"

print(son(4, 4))
print(son(4, 7))

# 10-m
son = lambda x: "5 ga karrali" if x % 5 == 0 else "5 ga karrali emas"

print(son(10))
print(son(3))

# 11-m
a = 7
b = 5
c = 10

katta = lambda x, y: "Birinchi kattaroq" if x > y else ("Ikkinchi kattaroq" if y > x else "Teng")

print(katta(a, b))
print(katta(b, c))

# 12-m
son = lambda x: "adult" if x > 18 else "minor"
print(son(9))
print(son(19))

# 13-m
positive = lambda x: "positive" if x > 0 else "negative"
print(positive(1))
print(positive(-9))

# 14-m
boliw = lambda x: "yes" if x % 2 == 0 else "no"
print(boliw(8))
print(boliw(15))

# 15-m

# 16-m
x = 60
natija = (lambda n: n*2 if n > 50 else n/2)(x)
print(natija)

# 17-m
son = lambda x: x + 2 if x % 2 == 0 else x - 1
print(son(22))

# 18-m
son = lambda a, b: "Katta" if a + b > 100 else "Kichik"
print(son(90, 12))

# 19-m
funk = lambda x: "yes" if 1 <= x <= 10 else "no"
print(funk(8))
print(funk(19))

# 20-m
son = lambda x: x % 3 == 0 or x % 5 == 0
print(son(4))
print(son(20))
