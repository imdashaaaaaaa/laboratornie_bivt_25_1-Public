a = input("a: ")
a_finish = a.replace(",", ".")
b = input("b: ")
b_finish = b.replace(",", ".")
summa = float(a_finish) + float(b_finish)
summa = round(summa, 2)
avg = summa / 2
avg = round(avg, 2)
print("sum=", summa, "; avg=", avg, sep="")
