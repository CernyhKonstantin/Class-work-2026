"""
Множинне наслідування -- механізм який надає можливість створити клас на основі двох або більше батьківських класів.
Проблема: однакові методи! Який метод буде викликатися?
Вирішується ця проблема за допомогою MRO (Method Resolution Order) — механізму,
який визначає порядок пошуку методів у випадку множинного наслідування.

Python використовує алгоритм C3 Linearization.
Цей алгоритм будує лінійний порядок обходу усіх класів, щоб уникнути конфліктів
і гарантує, що кожен клас у ієрархії буде відвіданий один раз.

Перевірити порядок пошуку методів можна так:
print(Child.mro()) або Child.__mro__

Саме MRO визначає, який метод буде викликаний першим.
"""

class A:
    def __init__(self):
        print("Constructor A")
    
    def method(self):
        print("Class A method")
    
    def method2(self):
        print("method 2 A")

class B:
    def __init__(self):
        print("Constructor B")
    
    def method(self):
        print("Class B method")

class C(B, A):
    pass

C().method() # Method B

print(C.mro())

class D(B, A):
    def __init__(self):
        print("Constructor D")
    
    def method(self):
        print("Class D method")
        
"""
У нашому прикладі MRO буде виглядати так:
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
- Спочатку пошук методу відбувається в класі D. Метод відсутній? Йдемо вгору по ієрархії
- Йдемо у клас B. Якщо метод є -- виклик, інакше далі пошук
"""

D().method() # Method D
    #  object
    # B   A
    # \   /
    #   D
D().method2()
print(D.mro())
# MRO - Method Resolution Order