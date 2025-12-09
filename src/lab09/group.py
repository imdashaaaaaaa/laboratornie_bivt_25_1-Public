import csv
from pathlib import Path
from ..lab08.models import Student


class Group:

    headers = ["fio", "birthdate", "group", "gpa"]
    
    def __init__(self, storage_path: str):
        """Инициализация группы студентов """
        self.path = Path(storage_path)

        if not self.path.exists():
            if not self.path.exists():
                with open(self.path, 'w', encoding='utf-8') as f:
                    f.write("fio,birthdate,group,gpa\n")

    
    def _read_all_dicts(self):
        """Читает все записи из CSV файла и возвращает список словарей."""
        if not self.path.exists():
            return []
        
        rows = []
        with open(self.path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
        
        return rows
    
    def _write_all_dicts(self, rows):
        """Записывает все записи в CSV файл."""
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.headers)
            writer.writeheader()
            writer.writerows(rows)
    
    def list(self):
        """ Возвращает Список объектов Student """
        rows = self._read_all_dicts()
        students = []
        
        for row in rows:
            # Создаем объект Student из словаря
            student = Student.from_dict(row)
            students.append(student)
        
        return students
    
    def add(self, student):
        """
        Добавляет нового студента в базу данных.
            student (Student): Объект Student для добавления
        """
        rows = self._read_all_dicts()
        student_dict = student.to_dict()
        student_dict["gpa"] = str(student_dict["gpa"])
        rows.append(student_dict)
        self._write_all_dicts(rows)
    
    def find(self, substr):
        """ Находит студентов по подстроке в ФИО """
        all_students = self.list()
        substr_lower = substr.strip().lower()
        
        found_students = []
        for student in all_students:
            if substr_lower in student.fio.lower():
                found_students.append(student)
        
        return found_students
    
    def remove(self, fio: str):
        "Удаляет запись по точному ФИО. Возвращает количество удалённых."
        rows = self._read_all_dicts()
        new_rows = [r for r in rows if r["fio"] != fio]
        removed = len(rows) - len(new_rows)

        if removed:
            self._write_all_dicts(new_rows)

        return removed
    
    def update(self, fio, **fields):
        """Обновляет студента по ФИО."""
        rows = self._read_all_dicts()
        fio_lower = fio.strip().lower()
        
        for row in rows:
            if row["fio"].strip().lower() == fio_lower:
                row.update({k: str(v) for k, v in fields.items()})
                self._write_all_dicts(rows)
                return True
        
        return False