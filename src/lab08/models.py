from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:

    fio: str
    birthdate: str
    group: str
    gpa: float
    
    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Неправильный формат даты: {self.birthdate}, требуется: YYYY-MM-DD")
        
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"Средний балл должен быть от 0 до 5. Вы ввели: {self.gpa}")
    
    def age(self) -> int:
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - birth_date.year
        
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        return age
    
    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        # Валидация произойдет автоматически в __post_init__
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=float(data["gpa"])
        )
    
    def __str__(self) -> str:
        return (
            f"{self.fio}\n"
            f"Дата рождения: {self.birthdate}\n"
            f"Группа: {self.group}\n"
            f"Средний балл: {self.gpa}"
        )
    
if __name__ == "__main__":
    student = Student("Королева Дарья Михайловна", "2006-09-26", "БИВТ-25-1", 5.0)
    print(student)
    print( "=" * 140)

    print(f"Возраст: {student.age()}")
    
    student_dict = student.to_dict()
    print(f"Сериализованный: {student_dict}")
    
    restored_student = Student.from_dict(student_dict)
    print(f"Десериализованный: {restored_student}")