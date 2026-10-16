class User:
    test_counter = 0
    __counter = 0 #static
    #constructor
    # def __new__(cls, name, age):
    #     print("I am ctor User()")
    #     return super().__new__(cls)

    def __init__(self, name='unknown', age=18):
        print('I am init method')
        User.__counter += 1
        self.__name = name #_nameClass__nameField
        self.__age = age
        self._email = 'admin@gmai.com'
        self._phone = '+1 555 555 555'

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, new_age):
        if not isinstance(new_age,int):
            raise ValueError(f"Age is not an integer")
        if new_age<0 or new_age>=120:
            raise  ValueError(f"Invalid Age {new_age}")
        self.__age = new_age

    def __str__(self):
        return f'User: {self.__name}, Age: {self.__age} {User.__counter}'

    def show_user(self):
        return f'User: {self.__name}, Age: {self.__age} {User.__counter}'

    @staticmethod
    def get_counter():
        return User.__counter

    def __del__(self):
        print('__del__')

    def __add__(self, other):
        if isinstance(other,User):
            self.__name += ' '+other.__name
        if isinstance(other,int):
            self.__age += other

    def __mul__(self, other):
        self.__age *= other
