#2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

print("Ввведите координаты двух точек:")
x1 = float(input("x1="))
y1 = float(input("y1="))
x2 = float(input("x2="))
y2 = float(input("y2="))
if x1 == x2 and y1 == y2:
    print("Введены координаты одной точки, для прямой необходимо две.")
elif y1 == y2:
    print("y =", y1)
elif x1 == x2:
    print("x =", x1)
else:
    k = (y1 - y2) / (x1 - x2)
    b = y1 - k * x1
    if b > 0:
        print("y = {}x + {}".format("%.2f" % (k), "%.2f" % (b)))
    elif b == 0:
        print("y = {}x".format("%.2f" % (k)))
    else:
        print("y = {}x - {}".format("%.2f" % (k), "%.2f" % (abs(b))))
