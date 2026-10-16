"""
В Python є механізм, який дозволяє передавати довільну кількість аргументів у функцію і розбивати їх на окремі елементи. 
Частіше за все ви можете його зустріти в параметрах функцій/методів:

def example(*args, **kwargs):
    pass

"""


def sample(*args, **kwargs):
    # args - це кортеж, який містить неіменованні аргументи
    # kwargs(key-word arguments) = це словник, який містить іменовані аргументи
    # за правилами мови, спочатку йдуть аргументи без імен, після них іменовані аргументи
    print(type(args)) # Output: <class 'tuple'>
    print(type(kwargs)) # Output: <class 'dict'>
    
    if len(args) > 0:
        print("args: ")
        for item in args:
            print(f"{item}, ", end="")
        print("\n")
    
    if len(kwargs) > 0:
        print("kwargs: ")
        for key, value in kwargs.items():
            print(f"{key} : {value}")
        print("\n")

# Тепер можемо передавати будь-яку кількість аргументів, навіть нуль аргументів.
sample() # спрацює без помилок


sample(1,"Hello", name="Tom", surname="Due")
"""
Output:
....
args:
1, Hello,

kwargs:
name : Tom
surname : Due
"""


# Зверніть увагу на наступні два виклики:

"""
У першому виклику список та словник передаются як звичайні аргументи. Тут нічого цікавого:)
"""
sample(['item1', 'item2'], _dict={"key1":"value1", "key2":"value2"})
"""
Output:
....
args:
['item1', 'item2'],

kwargs:
_dict : {'key1': 'value1', 'key2': 'value2'}
"""

"""
Другий виклик вже цікавіше. Тут список та словник розбиваються на окремі аргументи
Іншими словами це називається розпаковка
"""
sample(*['item1', 'item2'], **{"key1":"value1", "key2":"value2"})
"""
Output:
....
args:
item1, item2,

kwargs:
key1 : value1
key2 : value2
"""