# Реализуй класс GradeBook (электронный дневник), который хранит оценки студентов по пятибалльной шкале.
# Требования:

# Добавление оценок:
# Метод add_grade(student_name: str, grade: int) добавляет оценку студенту.
# Оценка должна быть целым числом от 1 до 5.
# Если указана неправильная оценка (например, 0, 6, -1), метод должен выбросить ValueError.

# Просмотр средней оценки одного студента:
# Метод get_average(student_name: str) -> float возвращает среднюю оценку для указанного студента.
# Если у студента пока нет оценок, возвращается 0.0.

# Просмотр всех средних оценок:
# Метод get_all_averages() -> dict[str, float] возвращает словарь, где ключ — имя студента, а значение — его средняя оценка.
# Внутреннее хранилище оценок (словарь) должно быть приватным (self.__grades), чтобы не допустить прямого изменения извне.

class GradeBook:
    def __init__(self):
        self.__grades = {}

    def add_grade(self, student_name: str, grade: int):
        if grade < 1 or grade > 5:
            raise ValueError("Оценка должна быть от 1 до 5")

        if student_name not in self.__grades:
            self.__grades[student_name] = []

        self.__grades[student_name].append(grade)

    def get_average(self, student_name: str) -> float:
        if student_name not in self.__grades or len(self.__grades[student_name]) == 0:
            return 0.0
        grades = self.__grades[student_name]
        return sum(grades) / len(grades)

    def get_all_averages(self) -> dict[str, float]:
        return {
            student: (sum(grades) / len(grades) if grades else 0.0)
            for student, grades in self.__grades.items()
        }

