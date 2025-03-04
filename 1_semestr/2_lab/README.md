# Звіт до роботи 2
## Тема: _Основи програмування на Python_
### Мета роботи: _Навчитись застосовувати основні конструкції мови Python, виконати всі приклати та з використанням ChatGPT створити власні приклади які демонструють особливості кодових конструкцій Pyhton_

---
### Виконання роботи
### Так як усі завдання виконані у Python ноутбуці, скріни не потрібно було робити

* ### Створив [Python ноутбук](2.ipynb) в якому буду виконувати основні конструкції та базові приклади мови Python. Застосовуючи команду print виконав наступне:

   #### 1. Познайомився з основними типами даних та попракувався з простими змінними str та int, списками list, наборами set, незмінним списком об'єктів tuple та словниками dict;

    #### 2. Познайомились з трьома основними вбудованими константами в Python (True, False та None) та за допомоги встроєної функції **_print_** вивів значення **"False"**;

    #### 3. Дізналися про такі вбудовані функції як **_len()_** яка використовується для визначення довжини кількості елементів, **_sum()_** який підсумовує всі елементи ітерабельного об'єкта та **_max()_** яка повертає найбільше значення з ітерабельного об'єкта.

    #### 4. Ознайомились з двома циклами в Python **_for_**  та **_while_**, переконалися що одне і те ж завдання можна виконати як за допомоги циклу **_while_** так і за допомоги циклу  **_for_** та дізналися про оператор **_break_**, який перериває цикл перш ніж виконати всі ітерації, і оператор **_continue_** який дозволяє пропустити певну ітерацію ;

    #### 5. Познайомилися з розгалуженням в Python (_if_),дізналися що **_if_** в Python замінює оператор switch у інших мовах і те що по канонічному **_if/else_** повинні застосовуватись у парі, але зазвичай умови роблять лише з **_if_**;

    #### 6. Ознайомилися з конструкією **_try->except->finally_** та привели приклад коду в якому остання частинка конструкції **_try_** це є очищувач (приберальник), а **_finally_** буде виконуватись завжди незалежно чи була помилка чи ні;

    #### 7. Ознайомився з контекст-менеджером **_with_**, та дізналися що є багато програм які вимагають узгодженої взаємодії та те що найбільш яскравим прикладом узгодженої взаємодії це робота з файлами - _відкрити - зробити щось - закрити_;

    #### 8. Познайомився з _Python lambdas_ та дізналися що це безіменні фінкції, дізналися що визначення функції можна помістити в один рядок за допомоги **_Lambdas_** та навели декілька прикладів;

    * ### Запитав в GhatGPT як би він розписав про основи Python. Виконання його прикладів коду я протестив у новому [Python ноутбуці](2.1.ipynb). Відповідь штучного інтелекту далі нижче:

    #### Основи Python включають ключові концепції програмування, які дозволяють ефективно працювати з мовою. Ось короткий огляд найважливіших аспектів:

    ## 1. Змінні та типи даних
    Python є мовою з динамічною типізацією, що означає, що типи даних не потрібно вказувати явно. Наприклад:

    ```python
    x = 5  # int
    y = 3.14  # float
    name = "Dima"  # str
    ```

    __Основні типи даних:__

    * __int__ – цілі числа.
    * __float__ – числа з плаваючою комою.
    * __str__ – рядки (текст).
    * __list__ – списки (колекції елементів).
    * __tuple__ – кортежі (незмінні списки).
    * __set__ – множини (унікальні елементи).
    * __dict__ – словники (пари "ключ-значення").

    ## 2. Оператори
    Оператори використовуються для виконання різних операцій над змінними:

    * __Арифметичні:__ +, -, *, /, //, %, **
    * __Порівняльні:__ ==, !=, >, <, >=, <=
    * __Логічні:__ and, or, not

    ## 3. Умовні конструкції
    Використовуються для виконання різних блоків коду в залежності від умов:

    ```python
    if x > 0:
        print("Positive")
    elif x == 0:
        print("Zero")
    else:
        print("Negative")
    ```

    ## 4. Цикли
    Цикли дозволяють повторювати блоки коду:

    * __for__ – перебір елементів колекції:

    ```python
    for i in range(5):
        print(i)
    ```
    * __while__ – виконується доти, поки умова є істинною:

    ```python
    while x > 0:
        x -= 1
    ```

    ## 5. Функції
    Функції дозволяють структурувати код, роблячи його більш читабельним і повторно використовуваним:

    ```python
    def greet(name):
        return f"Hello, {name}!"

    print(greet("Dima"))
    ```

    ## 6. Обробка помилок
    Можна використовувати блоки _try-except_ для обробки виняткових ситуацій:

    ```python
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero")
    ```

    ## 7. Модулі та бібліотеки
    Python має велику кількість вбудованих модулів, які можна підключати за допомогою import. Наприклад, для роботи з випадковими числами:

    ```python
    import random
    print(random.randint(1, 10))
    ```

    ## 8. Спискові включення (List comprehensions)
    Спрощений спосіб створення списків:

    ```python
    squares = [x**2 for x in range(10)]
    ```
    Ці основи формують фундамент Python, і розуміння цих концепцій дозволяє писати ефективний код та розвивати більш складні програми.

---
### Висновок:

#### У ході виконання лабораторної роботи я ознайомився з основними конструкціями мови Python, такими як змінні, оператори, умовні вирази, цикли та функції. Я вивчив основні типи даних, зокрема int, float, str, list, tuple, set, і dict, та навчився працювати з ними в середовищі Python.
#### Крім того, я створив Python-файл у форматі .ipynb для практичного закріплення знань і успішно реалізував приклади коду з використанням вбудованих функцій та констант. Особливо цікавим було ознайомлення з функціями-лямбдами, які дозволяють створювати анонімні функції на місці, що робить код більш лаконічним.
#### Отже, я отримав практичні навички роботи з Python та зрозумів базові концепції програмування на цій мові, що стане міцною основою для подальшого вивчення і розробки складніших програм.
---