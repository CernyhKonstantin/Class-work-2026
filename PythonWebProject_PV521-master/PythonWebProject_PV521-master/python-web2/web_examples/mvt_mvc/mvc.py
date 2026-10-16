# MVC -> Model, View, Controller

# Model (Databases->ORM->Model)
# View (Client: Input, Form, Button)
# Controller(View, Model) - посередник між View і Controller

# Model:
from datetime import datetime

def get_current_timestamp(): 
    return int(datetime.timestamp(datetime.now()))

# Entity
class Task:
    __id:int
    title:str
    description:str
    created_at:str
    
    def __init__(self, title, description):
        self.__id=get_current_timestamp()
        self.title = title
        self.description = description
        # YYYY-MM-DD HH:MM:SS
        self.created_at = str(datetime.now())
    
    @property
    def id(self):
        return self.__id
    
    def __str__(self):
        return f"TaskId: {self.id}\nTitle: {self.title}\nDescription: {self.description}\nCreated at: {self.created_at}"
    
# task = Task("DoSmth", "Description")
# print(task)

class Model:
    def __init__(self):
        self.__tasks=[]
    
    # CRUD methods (Create, Read, Update, Delete)
    
    def add_task(self, task:Task):
        self.__tasks.append(task)
    
    # get_tasks
    @property
    def tasks(self): return self.__tasks
    
    def get_task(self, id:int)->Task:
        if len(self.tasks)  <= 0: return None
        for item in self.tasks:
            if item.id == id:
                return item
        return None
    
    def update_task(self, id, task:Task)->bool:
        _task = self.get_task(id)
        if not _task: return False
        _task.title = task.title
        _task.description = task.description
        return True
    
    def delete_task(self, id):
        _task = self.get_task(id)
        if not _task: return False
        self.tasks.remove(_task)
        return True
    
class View:
    def show_menu(self)->int:
        print("1) Show all tasks")
        print("2) Show task by id")
        print("3) Create new task")
        print("4) Update task")
        print("5) Delete task")
        print("6) Exit")
        
        return int(input("Select menu item, enter value 1-5: "))
    
    def show_message(self, msg:str): 
        print("\n")
        print("-"*30)
        print(msg)
        print("-"*30)
        print("\n")
    
    def create_task(self)->Task:
        title = input("Enter title for task: ")
        description = input("Enter description for task")
        return Task(title, description)
    
    def update_task(self, tasks:list[Task])->tuple:
        self.show_tasks(tasks)
        id = int(input("Choose task for update(enter id): "))
        title = input("Enter new title: ")
        description = input("Enter new description: ")
        return (id, Task(title, description))
    
    def delete_task(self, tasks:list[Task])->int:
        self.show_tasks(tasks)
        return int(input("Choose task for delete(enter id): "))
       
    def show_tasks(self, tasks:list[Task]):
        for task in tasks:
            print("-"*30)
            print(task)
            print("-"*30)
    
    def show_task(self):
        return int(input("Choose task(enter id): "))
    
class Controller:
    def __init__(self, model:Model, view: View):
        self.__model = model
        self.__view = view
    
    @property
    def view(self): return self.__view
    
    @property
    def model(self): return self.__model
     
    def action_create(self):
        task = self.__view.create_task()
        self.__model.add_task(task)
        self.__view.show_message("Task successfuly created!")
    
    def action_update(self):
        (id, task) = self.__view.update_task(self.__model.tasks)
        result = self.__model.update_task(id, task)
        if result:
            self.__view.show_message("Task was successfuly updated")
        else: self.__view.show_message("Update operation failed")
    
    def action_delete(self):
        id = self.__view.delete_task(self.__model.tasks)
        result = self.__model.delete_task(id)
        if result:
            self.__view.show_message("Task was successfuly deleted")
        else: self.__view.show_message("Delete operation failed")
        
    def action_show_tasks(self):
        self.__view.show_tasks(self.__model.tasks)
    
    def action_show_task(self):
        id = self.__view.show_task()
        task = self.__model.get_task(id)
        if not task is None:
            self.__view.show_message(task)
        else: self.__view.show_message("Task is not exist!")
        
app = Controller(Model(), View())

while True:
    menu_item = app.view.show_menu()
    
    """
    print("1) Show all tasks")
        print("2) Show task by id")
        print("3) Create new task")
        print("4) Update task")
        print("5) Delete task")
        print("6) Exit")
    """
    
    match menu_item:
        case 1:
            app.action_show_tasks()
        case 2:
            app.action_show_task()
        case 3:
            app.action_create()
        case 4:
            app.action_update()
        case 5:
            app.action_delete()
        case 6:
            app.view.show_message("Exit!")
            break
        case _:
            app.view.show_message("Wrong choice! Try again:")