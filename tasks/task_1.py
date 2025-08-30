# Создай базовый класс Employee с атрибутами: name, base_salary
# и методом get_salary(), который возвращает базовую зарплату.

# Создай два подкласса:
# Developer, у которого есть доп. атрибут bonus, который прибавляется к зарплате.
# Manager, у которого фиксированная премия 15% от базовой зарплаты.

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def get_salary(self):
        return self.base_salary


class Developer(Employee):
    def __init__(self, name, base_salary, bonus):
        # вызываем конструктор родителя, чтобы не дублировать код
        super().__init__(name, base_salary)
        self.bonus = bonus

    def get_salary(self):
        # зарплата = базовая + бонус
        return self.base_salary + self.bonus


class Manager(Employee):
    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)

    def get_salary(self):
        # зарплата = базовая + 15%
        return self.base_salary * 1.15

