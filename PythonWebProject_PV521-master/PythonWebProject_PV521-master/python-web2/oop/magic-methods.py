# __magic__() - магічний метод виділяється двома нижніми підкресленнями з обох боків у назві
# частина методів визначає життєвий цикл об'єкту(конструктор, деструктор)
# поведінка у ситуації коли об'єкт є аргументом (строкове представлення класу)
# перевантаження стандартних арифметичних операцій
# використання в стандартних функціях

class Collection:
    __start = 0

    def __init__(self, *args):
        self.collect = list(args)

    def __len__(self):
        return len(self.collect)

    def __getitem__(self, index):
        if index < 0:
            raise IndexError("Index out of range")
        return self.collect[index]

    def __setitem__(self, index, value):
        if index < 0:
            raise IndexError("Index out of range")
        self.collect[index] = value

    def __delitem__(self, index):
        if index < 0:
            raise IndexError("Index out of range")
        del self.collect[index]

    def __iter__(self):
        self.__start = 0
        return self

    def __contains__(self, member):  # in
        print("Contains")
        return member in self.collect

    def __next__(self):
        if self.__start >= len(self):
            self.__start = 0
            raise StopIteration

        current = self[self.__start]
        self.__start += 1
        return current


class PositiveNumber:
    def __new__(cls, value: int):
        if value < 0:
            print("Від'ємне число заборонено")
            return None
        return super().__new__(cls)

    def __init__(self, value: int):
        self.value = value


if __name__ == "__main__":
    # --- Collection Testing ---
    c = Collection(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(c.collect)

    print(max(c.collect))

    print("length: ", len(c))

    c[0] = 1000
    print("Collection item: ", c[0])

    del c[0]

    print(c.collect)
    print(1 in c)

    # --- PositiveNumber Testing ---
    print("\n--- PositiveNumber Class Testing ---")
    a = PositiveNumber(10)
    b = PositiveNumber(-5)

    if a is not None:
        print(a.value)  # Expected: 10

    print(b)  # Expected: None