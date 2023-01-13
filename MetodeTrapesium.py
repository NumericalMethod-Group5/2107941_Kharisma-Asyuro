def f(x):
    return 1/(1 + x**2)

def trapesium(x0,xn,n):
    h = (xn - x0) / n
    integrasi = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        integrasi = integrasi + 2 * f(k)
    integrasi = integrasi * h/2
    
    return integrasi

batasBawah = float(input("Masukan batas bawah dari integrasi: "))
batasAtas = float(input("Masukan batas atas dari integrasi: "))
subInterval = int(input("Masukan angka untuk sub intervals: "))

hasil = trapesium(batasBawah, batasAtas, subInterval)
print("Hasil integrasi adalah : %0.6f" % (hasil) )