import pytest

from tasks import Developer, Employee, Manager


def test_developer_salary():
    dev = Developer(name="Alice", base_salary=100000, bonus=20000)
    assert dev.get_salary() == 120000

def test_manager_salary():
    mgr = Manager(name="Bob", base_salary=100000)
    assert round(mgr.get_salary(), 2) == 115000

def test_polymorphic_salary_sum():
    team = [
        Developer("Dev1", 100000, 15000),
        Manager("Mgr1", 80000),
        Developer("Dev2", 110000, 10000)
    ]
    total = sum(emp.get_salary() for emp in team)
    assert total == 100000 + 15000 + 80000 + 80000 * 0.15 + 110000 + 10000
