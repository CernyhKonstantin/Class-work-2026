from car import Car
from book import Book
from stadium import Stadium


class PositiveNumber:
    def __new__(cls, value: int):
        if value < 0:
            print("Negative numbers are not allowed")
            return None
        return super().__new__(cls)

    def __init__(self, value: int):
        self.value = value


class MyIntArray:
    def __init__(self, elements=None):
        if elements is None:
            self._data = []
        else:
            if not all(isinstance(x, int) and not isinstance(x, bool) for x in elements):
                raise TypeError("MyIntArray accepts integer values only.")
            self._data = list(elements)

    def __str__(self) -> str:
        pairs = [f"{idx}: {val}" for idx, val in enumerate(self._data)]
        return f"[{', '.join(pairs)}]"

    def __add__(self, other):
        if isinstance(other, MyIntArray):
            if len(self._data) != len(other._data):
                raise ValueError("Arrays must be of the same size to perform addition.")
            return MyIntArray([a + b for a, b in zip(self._data, other._data)])
        elif isinstance(other, int) and not isinstance(other, bool):
            return MyIntArray([a + other for a in self._data])
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, MyIntArray):
            if len(self._data) != len(other._data):
                raise ValueError("Arrays must be of the same size to perform multiplication.")
            return MyIntArray([a * b for a, b in zip(self._data, other._data)])
        elif isinstance(other, int) and not isinstance(other, bool):
            return MyIntArray([a * other for a in self._data])
        else:
            return NotImplemented

    def __eq__(self, other) -> bool:
        if isinstance(other, MyIntArray):
            return self._data == other._data
        return False

    def __getitem__(self, index: int) -> int:
        return self._data[index]

    def __setitem__(self, index: int, value: int):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("Only integer values can be assigned.")
        self._data[index] = value

    def __len__(self) -> int:
        return len(self._data)


def demonstrate_positive_number():
    print("POSITIVE NUMBER VERIFICATION")
    print("----------------------------")
    a = PositiveNumber(10)
    b = PositiveNumber(-5)

    if a is not None:
        print(f"a.value: {a.value}")

    print(f"b: {b}")
    print("----------------------------\n")


def demonstrate_my_int_array():
    print("MY INT ARRAY VERIFICATION")
    print("-------------------------")
    arr1 = MyIntArray([10, 20, 30])
    arr2 = MyIntArray([1, 2, 3])

    print(f"arr1: {arr1}")
    print(f"arr2: {arr2}")
    print(f"arr1 + arr2: {arr1 + arr2}")
    print(f"arr1 + 5: {arr1 + 5}")
    print(f"arr1 * arr2: {arr1 * arr2}")
    print(f"arr1 * 2: {arr1 * 2}")

    arr3 = MyIntArray([10, 20, 30])
    print(f"arr1 == arr3: {arr1 == arr3}")

    arr1[0] = 99
    print(f"arr1 after modifying index 0: {arr1}")
    print("-------------------------\n")


def manage_object(obj, object_name):
    while True:
        print(f"\n{object_name.upper()} MANAGEMENT")
        print("1. Enter or update data")
        print("2. Display data")
        print("3. Display object using __str__")
        print("0. Back to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            obj.input_data()
        elif choice == "2":
            obj.show_data()
        elif choice == "3":
            print(obj)
        elif choice == "0":
            break
        else:
            print("Invalid option. Please choose again.")


def main():
    demonstrate_positive_number()
    demonstrate_my_int_array()

    car = Car()
    book = Book()
    stadium = Stadium()

    while True:
        print("\nOBJECT-ORIENTED PROGRAMMING")
        print("HW 12.10.2026")
        print("---------------------------")
        print("1. Car management")
        print("2. Book management")
        print("3. Stadium management")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            manage_object(car, "Car")
        elif choice == "2":
            manage_object(book, "Book")
        elif choice == "3":
            manage_object(stadium, "Stadium")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()