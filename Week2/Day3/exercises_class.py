class MyClass:
    def __init__(self, x, y):
        self.__x = x
        self._b = 1
        self.y = y

    @staticmethod
    def add(x, y):
        return x + y
    
    @property
    def x(self):
        return self.__x
    

new_class = MyClass(1, 2)
print(new_class.add(10, 20))

print(new_class._b)
print(new_class.__x)
