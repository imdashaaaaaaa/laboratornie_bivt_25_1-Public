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
### Задание 1 (arrays)
```python
def min_max(nums:list[float | int]) -> tuple [float | int, float | int]:
    if not nums: 
        return ValueError 
    return tuple((min(nums), max(nums)))

def unique_sorted(nums: list[float|int]) -> list[float|int]:
    return tuple(sorted(set(nums)))

def flatten(mat: list[list | tuple]) -> list:
    array=[]
    for element in mat:
         if not isinstance(element, (list, tuple)):
             return TypeError
         array.extend(element)
    return array

print(min_max([3, -1, 5, 5, 0]), min_max([42]), min_max([-5,-2,-9]), min_max([]), min_max([1.5,2,2.0,-3.1])) #Тест-кейсы min_max

print(unique_sorted([3,1,2,1,3]), unique_sorted([]), unique_sorted([-1,-1,0,2,2]), unique_sorted([1.0, 1, 2.5, 2.5, 0])) #Тест-кейсы unique_sorted

print(flatten([[1,2],[3,4]]), flatten([[1,2],(3,4,5)]), flatten([[1],[],[2,3]]), flatten([[1,2],"ab"])) #Тест-кейс flatten
```
https://github.com/imdashaaaaaaa/laboratornie_bivt_25_1-Public/blob/main/images/lab02/arrays_ph.png

### Задание 2 (matrix)
```python
def is_valid_matr(mat: list[list[float | int]]) -> bool:
    for i in range (len(mat)):
        if len(mat[i])!=0 and len(mat[0])!=len(mat[i]):
            return False
    return True 

def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat)==0:
        return []
    if is_valid_matr(mat)==False:
        return ValueError

    result = []
    for columns in range (len(mat[0])):
        new_row=[]
        for row in range (len(mat)):
            new_row.append(mat[row][columns])
        result.append(new_row)

    return result 

print(transpose([[1, 2, 3]]), transpose([[1], [2], [3]]), transpose([[1, 2], [3,4]]), transpose([]), transpose([[1, 2], [3]])) #Тест-кейс transpose

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if is_valid_matr(mat)==False:
        return ValueError
    
    result=[]
    for row in mat:
        result.append(sum(row))

    return result

print(row_sums([[1,2,3], [4,5,6]]), row_sums([[-1,1], [10,-10]]), row_sums([[0,0], [0,0]]), row_sums([[1,2], [3]])) #Тест-кейс row_sums

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if is_valid_matr(mat)==False:
        return ValueError
    
    new_mat=(transpose(mat))
    result=(row_sums(new_mat))

    return result

print(col_sums([[1,2,3], [4,5,6]]), col_sums([[-1,1], [10,-10]]), col_sums([[0,0], [0,0]]), col_sums([[1,2], [3]])) #Тест-кейс col_sums
```

### Задание 3 (tuples)
```python
def format_record(rec: tuple[str, str, float]) -> str:
    cleaned_fio=rec[0].strip().split()
    surname=cleaned_fio[0][0].upper()
    if len(cleaned_fio)==3:
        form_fio=f"{surname}{cleaned_fio[0][1:]} {cleaned_fio[1][0].upper()}.{cleaned_fio[2][0].upper()}."
    elif len(cleaned_fio)==2:
        form_fio=f"{surname}{cleaned_fio[0][1:]} {cleaned_fio[1][0].upper()}."
    else:
        return ValueError
    
    group=rec[1].strip()
    if not group:
        return ValueError
    
    gpa=f"{float(rec[2]):.2f}"

    return f"{form_fio}, гр. {group}, GPA {gpa}"

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record((" К ", "", 4.877)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.5689)))
```
