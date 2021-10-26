def decorator(func):
    def wrapper():
        print("dupa jasia hehehehe")
        func()
        print("dupa jasia hehehehe")
    return wrapper

def hello():
    print("hello world")

hello = decorator(hello)
hello()

@decorator
def witaj():
    print("witaj świecie")

witaj()