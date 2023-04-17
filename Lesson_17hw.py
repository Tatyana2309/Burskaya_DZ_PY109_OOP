# task 2
#
class Calculator:
    numb = 2

    def __init__(self):
        self.numb_1 = float(input("Введите первое число: "))
        self.numb_2 = float(input("Введите второе число: "))

    def addition(self):
        return self.numb_1 + self.numb_2

    def divide(self):
        return self.numb_1 / self.numb_2

    def multi(self):
        return self.numb_1 * self.numb_2

    def minus(self):
        return self.numb_1 - self.numb_2


object_Calculator = Calculator()
print(object_Calculator.addition())
print(object_Calculator.minus())
print(object_Calculator.multi())
print(object_Calculator.divide())


# Homework
class Example:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.list_1 = []
        self.list_2 = []

    def func(self, d):
        if type(d) is str:
            for i in d:
                if i in "aeyuio":
                    self.a += 1
                    self.list_1.append(i)
                elif i not in "aeyuio":
                    self.b += 1
                    self.list_2.append(i)
                else:
                    print('Error')
            print(f'Количество гласных букв: {self.a}')
            print(f'Количество согласных букв: {self.b}')
            print(f'Длина слова равна: {self.func1(d)}')

            if (self.a * self.b) <= self.func1(d):
                print(f'Гласные: { self.list_1}')
            else:
                print(f'Согласные: {self.list_2}')

        elif type(d) is int:
            for i in str(d):
                i = int(i)
                if i % 2 == 0:
                    self.c += i
            print(f'Произведение равно: {self.c * self.func1(d)}')

    def func1(self, d):
        return len(str(d))


example_1 = Example()
d = input('Введите строку или число: ')
if d.isalpha():
    example_1.func(d)
elif d.isdigit():
    example_1.func(int(d))

# add homework
class Employee:
    numb = 2

    def __init__(self, name, family_name, position, salary):
        self.name = name
        self.family_name = family_name
        self.position = position
        self.salary = salary

    def func(self):
        print(f'Имя сотрудника: {self.name} Фамилия сотрудника: {self.family_name}'
              f' Должность сотрудника: {self.position} Зарплата сотрудника: {self.salary}')

    def func1(self, amount, percent):
        print(f'Новая зарплата у {self.name}: {self.salary + amount}')
        print(f'Новая зарплата,увеличенная на процент, у {self.name} : {self.salary + ((self.salary * percent) // 100)}')

    def func2(self, obj):
        if self.salary > obj.salary:
            print(f'Зарплата больше у {self.name}')
        else:
            print(f'Зарплата больше у {obj.name}')


empl = Employee('Kate', 'Smith', 'Accountant', 2000)
empl2 = Employee('Mary', 'Holmes', 'Manager', 3000)

empl.func()
empl2.func()
amount = int(input('Введите сумму: '))
percent = int(input('Введите процент, на который будет увеличена зарплата: '))

empl.func1(amount, percent)
empl2.func1(amount, percent)

empl.func2(empl2)
