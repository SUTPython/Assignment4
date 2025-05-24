class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, position, salary):
        super().__init__(name, age)
        self.position = position
        self.salary = salary

    def is_retired(self):
        return self.age >= 60


def main():
    n = int(input())
    employees = []

    for _ in range(n):
        name, age, position, salary = input().split()
        age = int(age)
        salary = int(salary)
        employees.append(Employee(name, age, position, salary))

    retired_count = sum(emp.is_retired() for emp in employees)
    print(retired_count)


if __name__ == "__main__":
    main()
