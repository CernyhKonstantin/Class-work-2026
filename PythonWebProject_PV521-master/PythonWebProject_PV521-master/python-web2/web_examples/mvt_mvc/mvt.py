# MVT -> Model -> View -> Template
# data = View->Model.getTask
# View -> render(Template, data)

"""
ProductCardTemplate
<CardBody>
    <Image></Image>
    <Link>ProductName</Link>
    <Label>Price</Label>
</CardBody>

ProductPageTemplate
ProductGallery
ProductDescription
ProductProperties
Reviews
"""
from datetime import datetime
from abc import abstractmethod, ABC

def get_current_timestamp(): 
    return int(datetime.timestamp(datetime.now()))

# Entity
class Book:
    __id:int
    name: str
    author: str
    genre: str
    
    def __init__(self, name, author, genre):
        self.__id = get_current_timestamp()
        self.name = name
        self.author = author
        self.genre = genre
    
    @property
    def id(self):
        return self.__id
    
class BookModel:
    def __init__(self):
        self.__books:list[Book] = []
    # CRUD
    @property
    def books(self): return self.__books
    
    def add(self, book:Book): self.books.append(book)
    
class BookTemplate(ABC):
    @abstractmethod
    def render(self, books: list[Book]): pass
    
class BookView:
    def __init__(self, model: BookModel):
        self.model = model
    
    def render(self, template: BookTemplate):
        return template.render(self.model.books)
    
class BookListDetailed(BookTemplate):
    def render(self, book:Book):
        print("test")
    def render(self, books:list[Book]):
        if len(books) <= 0: print("Book list is empty!")
        else:
            for item in books:
                print("\n")
                print("-"*30)
                print(f"BookId: {item.id}")
                print(f"Name: {item.name}")
                print(f"Author: {item.author}")
                print(f"Genre: {item.genre}")
                print("-"*30)
                print("\n")

class BookListNames(BookTemplate):
    def render(self, books:list[Book]):
        if len(books)<=0: print("Book list is empty")
        else:
            print("-"*30)
            for item in books:
                print(f"{item.id}-{item.name}")
            print("-"*30)

def create_book()->Book:
    name = input("Enter book name: ")
    author = input("Enter book author: ")
    genre = input("Enter book genre: ")
    return Book(name, author, genre)

def show_menu():
    print("1) Add book")
    print("2) Show books(detailed)")
    print("3) Show books(short info)")
    print("4) Exit")
    return int(input("Show menu item: "))\

booksModel = BookModel()
bookView = BookView(booksModel)

detailedTemplate = BookListDetailed()
shortTemplate = BookListNames()

while True:
    selected = show_menu()

    match selected:
        case 1:
            bookView.model.add(create_book())
        case 2:
            bookView.render(detailedTemplate)
        case 3:
            bookView.render(shortTemplate)
        case 4:
            print("Exit!")
        case _:
            print("Wrong menu item. Please try again...")