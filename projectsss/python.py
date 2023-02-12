class Car:
    def __init__(self):
        self.name ="rajesh"
        self.__age=22
    def two(self):
        self.__age=6545
        print(self.__age)
c1=Car()
print(c1.name)
c1.two()
self.__age=77
print(self.__age)