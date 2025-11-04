import csv
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    try:
        wb = Workbook() #создаем файл в экселе
        ws = wb.active #создаем активный лист в экселе
        ws.title = "Sheet1"
        
        # Читаем CSV и записываем в XLSX
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                ws.append(row)
        
        # Настраиваем авто-ширину колонок
        for column_cells in ws.columns:
            length = max(len(str(cell.value or "")) for cell in column_cells) #находим самую длинную строку в колонке для ориентира
            ws.column_dimensions[column_cells[0].column_letter].width = max(length + 2, 8) #column_dimensions - определяет букву столбца, width - присваивает ему ширину (минимум 8, +2 - запасные знаки на пробелы с двух сторон) 
        
        wb.save(xlsx_path)
        
    except FileNotFoundError:
        raise FileNotFoundError