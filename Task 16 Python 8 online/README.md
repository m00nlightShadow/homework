
### Завдання
* Створити клас Employee.

* __init__ має приймати наступні аргументи: ім’я, ЗП за один робочий день.

* Створити метод work(self, …) який повертає строку “I come to the office.”

* Створити класи Recruiter та Developer, які наслідують клас Employee.

* Перевизначити методи work в класах R та D, щоб вони повертали значення:

    “I come to the office and start to coding.” - для Developer

    “I come to the office and start to hiring.” - для Recruiter

* Перевизначити методи __str__, щоб они повертали строку: “Посада: Ім’я”

* Зробити можливим порівнювати Employee по рівню ЗП.

* Створити метод check_salary(self, days), який розраховує ЗП за передану кількість днів.

* ** Зробити можливим, щоб метод check_salary рахував ЗП з початку місяця до поточного дня, не враховуючи вихідні дні.
* Додати в конструктор класу Developer атрибут tech_stack (список з назвами технологій).
* Для класу Developer зробити порівняння за кількістю технологій.
* Зробити можливим операцію додавання об’єктів класу Developer. 

  Результатом має бути новий об’єкт, в якому name = name1 + ' ' + name2, a tech_stack - список з технологій двох об’єктів (тільки унікальні значення), ЗП - більша з двох.