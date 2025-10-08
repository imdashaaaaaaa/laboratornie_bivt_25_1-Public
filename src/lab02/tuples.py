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


