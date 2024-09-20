# Функції для арифметичних операцій
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ділення на нуль неможливе!"
    else:
        return x / y

# Вибір операції
print("Виберіть операцію:")
print("1.Додавання")
print("2.Віднімання")
print("3.Множення")
print("4.Ділення")

while True:
    choice = input("Введіть номер операції (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        if choice == '1':
            print(f"Результат: {num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print(f"Результат: {num1} / {num2} = {divide(num1, num2)}")
            
        # Запит на продовження або завершення програми
        next_calculation = input("Хочете зробити ще одну операцію? (так/ні): ")
        if next_calculation.lower() != 'так':
            break
    else:
        print("Неправильний вибір. Спробуйте ще раз.")
