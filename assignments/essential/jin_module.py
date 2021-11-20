def hello_world():
    print("Hello World!")

def nice_day(name):
    print(f"Wish you have a nice day, {name}")

class People:
    # default constructor 
    def __init__(self, name):
        self.name = name

    def self_intro(self):
        print(f"My name is {self.name}.")

    def greet(self):
        print("Good day everyone.")