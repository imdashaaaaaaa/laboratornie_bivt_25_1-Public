## Лабораторная №1

### Задание 1
```python
name=input("Имя: ") 
age=int(input("Возраст: ")) 
print("Привет, ", name, "! Через год тебе будет ", age+1, ".", sep="")
```
![ex01](https://github.com/user-attachments/assets/ecebae4d-c888-4c35-8e54-02ee1a0388e5)

### Задание 2
```python
a=(input("a: "))
a_finish=a.replace(",",".")
b=(input("b: "))
b_finish=b.replace(",",".")
summa=float(a_finish)+float(b_finish)
summa=round(summa, 2)
avg=summa/2
avg=round(avg, 2)
print("sum=", summa, "; avg=", avg, sep="")
```
![ex02](https://github.com/user-attachments/assets/e03fb6f6-355e-4fd4-83ee-e581e580dec7)

### Задание 3
```python
price=float(input("Цена(₽): "))
discount=float(input("Скидка(%): "))
vat=float(input("НДС(%): "))
base=round(price*(1-discount/100), 2)
vat_amount=round(base*(vat/100), 2)
total=round(base+vat_amount, 2)
print("База после скидки: ", base, " ₽", sep="")
print("НДС: ", vat_amount, " ₽", sep="")
print("Итого к оплате: ", total, " ₽", sep="")
```
![ex03](https://github.com/user-attachments/assets/51ea0f82-64bf-4c4f-87f2-ec1157fb4927)

### Задание 4
```python
m=int(input("Минуты: "))
hours=m//60
minutes=m%60
print(hours,":", f"{minutes:02d}", sep="")
```
![ex04](https://github.com/user-attachments/assets/ba6553c5-6833-42b5-bdad-9f450d860cb7)

### Задание 5
```python
full_name=input("ФИО: ")
strip_name=full_name.strip()
parts_name=strip_name.split()
initials=""
len_full_name=0
for i in range (3):
    len_full_name+=len(parts_name[i])
    initials+=parts_name[i][0].upper()
print("Инициалы:", initials)
print("Длина (символов):", len_full_name+2)
```
![ex05](https://github.com/user-attachments/assets/6e9bacbb-c4a1-4ba2-bdd9-e3f6565d81d2)



## Лабораторная №2

