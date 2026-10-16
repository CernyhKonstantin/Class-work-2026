# Декоратор - це прийом який дозволяє "змінити" поведінку функції, 
# але оригінальний код залишається без змін. 
# Технічно декоратор це також функція.
"""
Декоратор працює наступним чином, посилання оригінальної 
функції передається у параметри функції декоратора. 
Посилання функції декоратора 
присвоюється посиланню оригінальної функції.
Функція декоратор, складається з двох функцій, 
зовнішня та друга внутрішня, посилання на яку повертає зовнішня. 
Зовнішня в параметрах приймає
посилання на оригінальну функцію

def outer(original):
    def inner(*args, **kwargs):
        # (*args, **kwargs) - такий підхід дозволяє створити функцію з 
        # будь-якою кількістю параметрів. 
        # І такий підхід надає можливість декорувати
        # будь-яку функцію
        # викликаємо оригінал
        original(*args, **kwrags)
    
    # повертаємо посилання на внутрішню функцію, саме вона і буде "заміною" оригінальної функції.
    return inner
    

def sample():
    print("example")
    
# декоруємо функцію
sample = outer(sample)

# виклик вже зміненої функції
sample()

# Чи можна декорувати вже декоровану функцію? Так, скільки завгодно разів

# Ми пам'ятаємо що все в Python є об'єкт. 
# Справа в тому що оригінальній функції ми надаємо посилання на новий 
# об'єкт функції, у якої є свої 
# властивостію.
# Наприклад ім'я функції та документація(в Python можна 
# викликати функцію help(object) який повертає текстом опис та підказку)
# Є два шляхи які дозволяють зберегти оригінальній функції
1 - Декорувати внутрішню функцію декоратора, вбудованим декоратором, 
який автоматично зробить перенос властивостей
якщо вивести ім'я функції sample: print(sample.__name__) то виведеться 
ім'я inner

from functools import wraps
def outer(original):
    @wraps(original) # передаємо оригінальну функцію, 
    з якої необхідно зняти властивості
    def inner(*args, **kwargs):
        ....

2 - Замість ручного переносу посиланнь з оригінальної функції на функцію декоратор використовувати синтаксичний цукор
Було:
# декоруємо функцію
sample = outer(sample)

# виклик вже зміненої функції
sample()
Стало:
@outer
def sample():
    print("example")
"""


def beatify(orig_func):
    def wrapped(*args, **kwargs):
        print("-"*10)
        orig_func(*args, **kwargs)
        print("-"*10)
    return wrapped

def add_text(text="wrapped"):
    def wrap_add_text(orig_func):
        def wrapped(*args, **kwargs):
            print(text)
            orig_func(*args, **kwargs)
        return wrapped
    return wrap_add_text


# Так як є можливість зробити об'єкти які поводять себе як функція, ми маємо можливість створювати декоратори як класи
class class_decor:
    orig_func=None
    counter:int=0
    def __init__(self, orig_func):
        self.orig_func = orig_func
    
    def __call__(self, *args, **kwds):
        print("this class decor")
        self.counter+=1
        return self.orig_func(*args, **kwds)

@add_text("MyText")
@beatify
def greet():
    print("hello")

@class_decor
def greet_smbd(somebody):
    print(f"Hello, {somebody}")
greet_smbd("Tom")
greet()

print("Class decor call count: ", class_decor.counter)
# greet = beatify(greet)
# greet = add_text(greet)
# greet()

# greet_smbd = beatify(greet_smbd)
# greet_smbd("Tom")

####################### Декоратор з параметрами: #########################


# Декоратор з параметрами завжди має 3 рівні вкладеності:
# 1) Функція-фабрика — приймає параметри декоратора
# 2) Декоратор — приймає оригінальну функцію
# 3) wrapped — замінює оригінальну функцію

def repeat(times=2):
    # 1 рівень: фабрика декораторів
    # Викликається ОДИН раз у момент написання @repeat(...)
    # Повертає функцію-декоратор
    print("→ repeat() створює декоратор, параметр times =", times)

    def decorator(original_func):
        # 2 рівень: сам декоратор
        # Викликається, коли Python декорує функцію
        print("→ decorator() декорує функцію:", original_func.__name__)

        def wrapped(*args, **kwargs):
            # 3 рівень: обгортка
            # Викликається КОЖЕН раз, коли ми викликаємо вже декоровану функцію
            for i in range(times):
                print(f"Виклик №{i+1}")
                original_func(*args, **kwargs)

        return wrapped  # повертаємо заміну оригінальної функції

    return decorator  # повертаємо декоратор з фабрики


@repeat(times=3)  # ← спочатку викликається repeat(3), а її результат — декоратор
def say_hi():
    print("Hi!")


# Тепер say_hi = wrapped
say_hi()


# Класовий декоратор — це декоратор, який приймає КЛАС, а повертає змінений або обгорнутий КЛАС.
# Логіка така ж, як і з функціями: декоратор приймає клас, повертає новий клас або той самий з модифікаціями.

def add_repr(cls):
    # Декоратор класу отримує сам клас як аргумент
    # cls — це НЕ екземпляр, а сам клас (MyClass)
    
    # Додаємо або перевизначаємо метод __repr__
    def new_repr(self):
        # self — вже екземпляр класу
        return f"<{cls.__name__}: {self.__dict__}>"
    
    cls.__repr__ = new_repr  # додаємо метод до класу
    return cls  # повертаємо клас (зміненим або тим самим)


@add_repr  # тепер MyClass проходить через декоратор
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


obj = MyClass(10, 20)
print(obj)  # викличе наш новий __repr__

