class MyClass:

    def __init__(self, param1=1, param2=10, param3=100, accses = False):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.accses = accses


    def __getattribute__(self, item):
        if item == "param3" and self.accses is False:
            return None
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        return None

    def __setattr__(self, attr_name, attr_value):
        # self.accses = True
        if attr_name == 'param1':
            attr_value = abs(attr_value)
        self.__dict__[attr_name] = attr_value

obj1 = MyClass()
obj2 = MyClass(accses=True)

print(obj1.param1)
print(obj2.param1)

print(obj1.param3)
print(obj2.param3)

print(obj1.param4)
print(obj2.param4)

print('=' * 20)
obj1.param1 = -3
print(obj1.param1)