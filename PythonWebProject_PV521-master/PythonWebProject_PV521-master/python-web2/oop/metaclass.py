# У Python ВСЕ є об’єктами.
# Клас — це також об’єкт, і створюється він МЕТАКЛАСОМ.
# За замовчуванням усі класи створює метаклас `type`.

################################# type #############################################
class Person:
    pass

# Person() → це екземпляр класу Person
# type(Person()) → покаже клас об’єкта → <class '__main__.Person'>
# Але сам клас Person теж є об’єктом, який створюється метакласом `type`.
print(type(Person()))  # => <class '__main__.Person'>

# Створення класу вручну через type:
# type(className: str, bases: tuple, attrs: dict)
# Це аналогічно тому, ніби ми написали class SampleClass: ...
SampleClass = type(
    'SampleClass',   # назва класу
    (),              # батьківські класи (порожній tuple → немає наслідування)
    {
        "attr1": "Hello",  # додаємо атрибут у клас
        "sample_method": lambda self: print("Hello, World")  # додаємо метод
    }
)

s_obj = SampleClass()
print(s_obj.attr1)         # використовуємо доданий атрибут
s_obj.sample_method()      # викликаємо доданий метод
print(SampleClass.__dict__)  # дивимося всі атрибути класу


############################################ власні метакласи #####################################

# Створюємо власний метаклас.
# Метаклас — це клас, який створює інші класи.
class MyMetaClass(type):
    # __new__ викликається на етапі створення КЛАСУ (не об’єкта!)
    def __new__(cls, classname, bases, dict):
        print("Створено новий клас:", classname)
        print("Атрибути класу:", dict)

        # Створюємо клас через стандартний механізм type
        newClass = super().__new__(cls, classname, bases, dict)

        # Додаємо метод у створений клас
        newClass.sample_method = lambda self: print("sample_method")

        return newClass

    # __call__ викликається, коли ми створюємо ЕКЗЕМПЛЯР класу: MyClass()
    def __call__(self, *args, **kwds):
        return super().__call__(*args, **kwds)


# Використовуємо власний метаклас
class MyClass(metaclass=MyMetaClass):
    attr1 = 1
    pass

# type(MyMetaClass) → це тип метакласу (тобто сам type)
print(type(MyMetaClass))

# type(MyClass) → показує, що MyClass створено через MyMetaClass
print(type(MyClass))

# Створюємо екземпляр MyClass
s_obj = MyClass()

# Метод було додано метакласом у момент створення класу
s_obj.sample_method()
