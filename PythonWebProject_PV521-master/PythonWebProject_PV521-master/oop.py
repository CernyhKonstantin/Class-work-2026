from User import *

Player = type(
    "Player",
    (),
    {
        'role':'super admin',
        'age':18,
        'move':lambda self:f'Moving...()'
    }
)
p = Player()
#print(p.move(), p.role)

# print(int.__bases__)
print(type(Player))


# user1 = User("Bob",30)
# user1.test_counter+=2
# User.test_counter+=1
# print(User.test_counter, user1.test_counter)
# meta class type
#print(type(object))
# 1 2 Ян
# 1 2 Віталій
# 3 2

# user1+2
# print(user1)
# user1+User("Alice", 25)
# print(user1)


# user2 = User("Bob",30)
# user3 = User("Bob",30)
# print(user1)
# try:
#     user1.age += 1
#     print(user1)
#     user1.age = 40
#     print(user1)
#     print(User.get_counter())
# except Exception as e:
#     print(e)

# user2 = User(name="Bob")
# user3 = User(age=20)
# user4 = User()

#print(user1.show_user())

#SOLID S -Single Responsibility Principle
# __new__ - створення об'єкта
# __init__ - ініціалізація об'єкта




#print(isinstance(user,object))
# print(type(True-True))
# print(type(True+10-3+1.4))
#print(int.__subclasses__())
# print(bool.__bases__)
# print(object.__bases__)

#class Counter:
#     counter = 10
#     def __init__(self):
#         self.counter+=1
#
# a = Counter()
# print(a.counter)
