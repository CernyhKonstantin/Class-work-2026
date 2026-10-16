"""
Наслідування(успадкування) -- механізм який дозволяє створити клас на основі існуючого. Python підтримує множине наслідування
"""

class BaseClass:
    # приватне поле: не буде доступне у дочірньому класі
    __private:str = "private"
    
    # захищене поле: технічно лишається публічним, але за домовленістю вважається, що не слід чіпати за межами класу
    _protected:str = "protected"
    
    def __init__(self, field1, field2):
        self.__private = field1
        self._protected = field2
    
    def __str__(self): return f"Private: {self.private}\nProtected: {self._protected}"
    
    def set_private(self, new_value): self.__private = new_value
    private = property(
        lambda self: self.__private,
        set_private
    )
    
class DerivedClass(BaseClass):
    field:str
    
    def __init__(self, field1, field2, field):
        self.field = field
        # щоб викликати методи батьківського класу використовуйте super()
        super().__init__(field1, field2)
    
    def __str__(self):
        
        return super().__str__() +f"\nfield: {self.field}"

d = DerivedClass("private", "protected", "field")
print(d._protected)

# print(d.__private)
print(d.private)

print(d)
# print(BaseClass()._protected)