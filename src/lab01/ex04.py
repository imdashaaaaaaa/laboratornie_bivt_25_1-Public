m=int(input("Минуты: "))
hours=m//60
minutes=m%60
print(hours,":", f"{minutes:02d}", sep="")
