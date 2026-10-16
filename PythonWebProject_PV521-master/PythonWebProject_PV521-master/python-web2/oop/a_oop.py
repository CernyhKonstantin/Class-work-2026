"""
Python дозволяє писати додатки у функціональному, процедурному та 
об'єктно-орієнтованому стилях. 
Але все з чим ми працюємо в Python є об'єктом:
- Типи даних
- Функції
- Класи також є об'єктами спеціальних класів(метакласи див. metaclasses.py)
Навіть файл з python-кодом(модуль) також є об'єктом
"""

# об'єкт класу int.class
var = 10 

# об'єкт класу function.class
def work():
    pass

# модуль це також об'єкт який має свої властивості
# Наприклад: властивість __name__ зберігає назву модуля
# Якщо цей модуль є виконавчим, то зміна __name__ тримає значення '__main__' інакше містить просто назву модуля
print("OOP-module:", __name__)

# Це дозволяє нам відокремити код який має працювати тільки 
# при виконані данного модуля
# При імпорті цього модуля код виконуватися не має
if __name__ == '__main__':
    print(__name__)
    print(type(var))
    print(type(work))
    
# Перейдемо до класів
# Синтаксис створення класу:
"""
class ClassName(BaseClass1, BaseClass2...BaseClassn):
    pass
"""
# Усі об'єкти в Python мають батьківський клас object

"""
Усі об'єкти мають властивість __dict__, звичайний словник, 
який зберігає усі атрибути об'єкта у вигляді пари ключ:значення

Така особливість дозволяє до об'єктів додавати нові властивості
Розглянемо декілька прикладів нижче:
"""

# class Point:
#     pass

# p1=Point()

# p1.newAttr = 'Hello'

# print(p1.newAttr)

class Point:
    # Метод ініціалізації. Тут створюються та задаються початкові 
    # значення полів об'єкта.
    # Саме в __init__ ми визначаємо, які атрибути матиме екземпляр класу.
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # ‼️Усі нестатичні методи приймають мають мати перший 
    # параметр self(аналог this але явний)
    
    # Строкове представлення об'єкту, викликається автоматично, 
    # коли передаємо наш об'єкт у якості аргументу де очікується str
    def __str__(self):
        return f"X: {self.x} | Y: {self.y}"

"""
Зараз об'єкт p1 має лише 2 атрибути, координати х та у.
""" 
p1 = Point(10, 20)
print(p1)
print(p1.__dict__)


# Тут ми задаємо третю координату, і тепер p1 відображає точку у 3Д просторі.
# Зверніть увагу що тільки цей об'єкт має третю координату. 
# Тобто у кожного об'єкта словник атрибутів свій.
p1.z = 30

def new_str(self):
    return f"X: {self.x} | Y: {self.y} | Z: {self.z}"

p1.__str__ = new_str

print(p1.__str__(p1))

print(p1.__dict__)

# Таку поведінку можна змінити, замість словника атрибутів створювати кортеж, 
# який може зберігати
# тільки задану кількість атрибутів. Словник замінюємо слотами.
# Заміна словника слотами, робить об'єкти значно легшими
# class witohut dict atrributes
class Sample:
    __slots__ = ["field_1", "field_2", "field_3"]
    def __init__(self):
        self.field_1 = 1
        self.field_2 = "2"
        self.field_3 = "string"

s1 = Sample()
s1.field_1 = "Hello"
print(s1.field_1, s1.field_2, s1.field_3, sep=", ")
print(s1.__slots__)

"""
# ПОМИЛКА: додавати нові атрибути не можна!
# s1.newAttr='new'
"""


from utils import current_timestamp


"""
Інкапсуляція -- принцип який дозволяє приховати реалізацію об'єкта 
та надає доступ до стану об'єкта через інтерфейс(публічні методи)
Розглянемо реалізацію інкапсуляції в Python:
"""
# В Python немає звичних специфікаторів доступу(public, private, protected), 
# замість цього використовується спеціальний неймінг полів
"""
__<fieldName> - private. Закриває доступ до полів, зверенення тільки 
через аксессори або властивості.
Символи __ запускають механізм name mangling, що ускладнює доступ до поля ззовні. 

_<fieldName> - protected. Технічно доступ залишається публічним, 
але за домовленістю вважається, 
що це поле не слід чіпати за межами класу та його нащадків.
"""

"""
Аксесори та властивості:
Аксесори це набір методів, який дозволяє задавати значення полям(сеттери), 
або отримувати значення полів(геттери)

property - це спеціальний об'єкт(дескриптор), який дозволяє операції 
читання та запис полів. Є два способи створення властивості:
1) Набір функцій і властивість як поле:
Уявимо що в класі є приватне поле __email, давайте створимо властивість:
class Sample:
    __email: str
    # Упустимо конструктор: уявімо що він тут є:)
    
    def set_email(self, new_value:str):
    
        # логіка з валідацією поля
        
        # задаємо значення
        self.__email = new_value
    
    # property(f_get, f_set, f_del) це перш за все об'єкт, 
    # який приймає три метода управління полем(читання, запис, видалення)
    email = property(
        lambda self: self.__email, # f_get
        set_email, # f_set
        None # f_del не обов'зяково, у більшості випадках не використовується, викликається при використані ключового слова del
    )

2) Використаємо декоратор
class Sample:
    __email: str
    
    # методи які декоруються property мають мати однакове ім'я
    @property
    def email(self):
        return self.__email
        
    @email.setter
    def email(self, new_value):
        self.__email = new_value

"""
# Більш практичний приклад:

class Product:
    """
    ще один спосіб описати поля класу, створити їх як атрибути класу
    але обов'язково необхідно вказати тип або значення.
    ‼️Але будьте обережні з мутабельними типами
    Мутабельні типи -- це типи які можуть змінюватись на місці, 
    без створення нового об'єкту.
    Наприклад коллекції, додавання, видалення, зміна елементів 
    відбувається в існуючому об'єкті.
    
    Немутабельні типи -- це типи які не можуть змінюватись. 
    При змінні значення, створюється новий об'єкт в пам'яті. 
    Приклади таких типів: int, float, bool, str, tuple
    
    Отже в чому ризик? Якщо ви створите мутабельний тип як атрибут класу,
      він буде спільний для усіх об'єктів цього класу.
    Тому створюйте мутабельні типи, тільки в __init__, для кожного 
    об'єкту вони будуть екземплярними.
    """
    __id: str
    # __name = "product"
    __name: str
    __price: float
    __description: str
    
    def __init__(self, name, price, description):
        self.__name = name
        self.__price = price
        self.__description = description
    
    # метод класу, на відміну від статичних методів, приймають першим параметром 
    # посилання на клас
    # завдяки ним є можливість задавати додаткові атрибути, 
    # надавати значення полям
    # створювати нові методи, кротко кажучи змінювати поведінку класу    
    @classmethod
    def method_class(cls):
        cls.__id = current_timestamp()
    
    @staticmethod
    def print_product(product):
        print(product)
    
    # create properties for Product
    # Description property
    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, new_value):
        if not new_value or len(new_value.strip()) <= 0:
            raise ValueError("new_value is None or empty")
        self.__description = new_value
        
    # Price property
    @property
    def price(self):
        return self.__price    
    
    @price.setter
    def price(self, new_value: float):
        if not new_value or new_value <= 0:
            raise ValueError("new_value is None or empty")
        self.__price = new_value
    
    # Accessor methods for Name
    def get_name(self) -> str:
        return self.__name
        
    def set_name(self, new_value: str | int | float):
        if not new_value or len(str(new_value).strip()) <= 0:
            raise ValueError("new_value is None or empty")
        self.__name = str(new_value)

    def del_name(self):
        print("Delete name")
    
    name: property = property(get_name, set_name, del_name)
    
    def __str__(self):
        return f"""
    -----------------------------
    ProductId: {self.__id}
    Name: {self.__name}
    Description: {self.__description}
    Price: {self.__price}
    -----------------------------
    """


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def is_new(self) -> bool:
        return self.year >= 2020


# p1 = Product()
# print(p1.__id) #! Error: __id is private field

if __name__ == "__main__":
    Product.method_class()

    p1 = Product("product1", 299.99, "Lorem ipsum")
    print(p1)
    print(p1.get_name())
    p1.set_name("Product1")
    print(p1.get_name())

    print(p1.name)
    p1.name = "Product2" 
    print(p1.name)
    del p1.name

    Product.print_product(p1)

    # Verification / Testing the Book class
    print("\n--- Book Class Testing ---")
    book1 = Book("Dune", "Frank Herbert", 1965)
    book2 = Book("The Midnight Library", "Matt Haig", 2020)
    book3 = Book("Project Hail Mary", "Andy Weir", 2021)

    print(f"'{book1.title}' is new: {book1.is_new()}")  # Expected: False
    print(f"'{book2.title}' is new: {book2.is_new()}")  # Expected: True
    print(f"'{book3.title}' is new: {book3.is_new()}")  # Expected: True