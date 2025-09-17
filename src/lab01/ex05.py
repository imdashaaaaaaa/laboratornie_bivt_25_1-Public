full_name=input("ФИО: ")
strip_name=full_name.strip()
parts_name=strip_name.split()
initials=""
len_full_name=0
for i in range (3):
    len_full_name+=len(parts_name[i])
    initials+=parts_name[i][0].upper()
print("Инициалы:", initials)
print("Длина (символов):", len_full_name)
