
class Parent():
    def __init__(self):
        print("Parent init")

    def parent(self):
        print("Parent parent")

    def poke(self):
        print("Parent poked")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child init")

    def poke(self):
        print("Child poked")

parent = Parent()
parent.parent()
parent.poke()

child = Child()
child.poke()
child.parent()