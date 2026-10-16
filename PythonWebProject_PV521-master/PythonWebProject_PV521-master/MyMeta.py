class MyMeta(type):
    # mcsl - посилання на наш клас
    # name - назва
    # bases - tuple (батьківські класи) (A,B,C)
    # attrs - dict {name:"Alex", say_hi:lambda self:f'hello, self.name'}
    def __new__(mcls, name, bases, attrs):
        print(f'Створився класс {name}')
        attrs['category'] = 'general'
        return super().__new__(mcls, name,bases,attrs)

class Product(metaclass=MyMeta):
    pass
class User(metaclass=MyMeta):
    pass

p = Product()
print(type(Product))
print(type(p))
print(type(User))