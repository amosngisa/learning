class ParentClass:
    def __init__(self):
        self.a = 1
        print("Parent class object created")
        
    def someMethod(self):
        print("Hello")
        
class ChildClass:
    def __init__(self):
        print("Child class object created")
        
            
# parent = ParentClass()
# child = ChildClass()

# isinstance()
# print(isinstance(parent, ParentClass))

# issubclass()
# print(issubclass(ChildClass, int))

# hasattr()
print(hasattr(ParentClass, 'a'))
print(hasattr(ParentClass, 'someMethod'))
print(hasattr(ParentClass, 'b'))