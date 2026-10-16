"""
n
"""
greeting = lambda: print("Hello")
def greetingSmbd(x):
    """
    This function greet somebody
    
    Args:
        x(str): Type here somebody's name
    
    """
    print(f"Hello, {x}")

print(greetingSmbd.__doc__)
# greeting()

from functools import wraps

def simpleDecorator(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        print("#"*10)
        orig_func(*args, **kwargs)
        print("#"*10)
    
    # wrapper.__name__ = orig_func.__name__
    # wrapper.__doc__ = orig_func.__doc__
    return wrapper

# greeting = simpleDecorator(greeting)
# greeting()

@simpleDecorator
def sample():
    return "str"

greetingSmbd = simpleDecorator(greetingSmbd)
greetingSmbd("Tom")


def decorWithParametrs(symbol:str):
    def simpleDecorator(orig_func):
        @wraps(orig_func)
        def wrapper(*args, **kwargs):
            print(symbol*10)
            orig_func(*args,**kwargs)
            print(symbol*10)
        return wrapper
    return simpleDecorator

greeting = decorWithParametrs("$")(greeting)
greeting()

help(greetingSmbd)

@decorWithParametrs("^")
@simpleDecorator
def sample_text():
    print("SAMPLE TEXT")
    
sample_text()
                

"""
*args = list, arguments without name 
**kwargs = key-word arguments: dict
"""

# print("f",1,2)

def sample(*args, **kwargs):
    if len(args)>0:
        print("Args: ")
        for arg in args:
            print("argument: ", arg)
    
    if len(kwargs) > 0:
        print("kwargs:")
        for k,v in kwargs.items():
            print(f"[{k}] -> {v}")

# sample(1,"Hello", *[1,2,3,4,5], name='Joe', surname="Due", **{"animal":"cat", "animal_name":"Mursik"})
# sample()

# print(2,3,4,5,**{"sep":", ", "end":"\t"})
# print("Hello")

