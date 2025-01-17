class MyClass:
    def instance_method(self):
        return "This is an instance method."

    @classmethod
    def class_method(cls):
        return "This is a class method."

    @staticmethod
    def static_method():
        return "This is a static method."

# Example Usage
obj = MyClass()
print(obj.instance_method())
print(MyClass.class_method())
print(MyClass.static_method())
