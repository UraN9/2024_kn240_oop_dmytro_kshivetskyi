class MyClass:
    """   Це буде клас для експериментів,
        його використовуємо для лаб роботи № 3

        ---
        Atributes:
        surname: Прізвище
        name: Ім'я
    """
    def __init__(self, surname:str, name:str, mark:int): # у конструктор передаються аргументи
        print("Викликали конструктор!")
        # а тут визначаємо атрибути об`єкта
        self.surname = surname
        self.name = name
        self.mark = mark
        #self.penalty = None # можеми записати динамічний атрибут тут, але він перстане бути динамічним
        print("Завершили присвоєння атрибутів")
        self._test_protected = True

        self.__do_not_touch = "Це змінювати не можна"

    
    def print_private_atributes(self):
        return self.__do_not_touch
    
    def __repr__(self):
        return f"MyClass(Ніяких аргументів не переаємо)"
    
    def __len__(self):
        return len(self.surname)
    
    def __eq__(self, value):
        if getattr(self, "mark") and getattr(value, "mark", None):
            return True if self.mark == value.mark else False
        return None

class MySecondClass:
    pass