from re import L
from unicodedata import name


class Circle:
    pi = 3.14

    def __init__(self,r,x,y):
        self.r = r
        self.x = x
        self.y = y


    def area(self):
        return Circle.pi * self.r * self.r
    
    def circumference(self):
        return 2 * Circle.pi * self.r

    def center(self):
        return (self.x, self.y)

circle1 = Circle(3,2,4)
x = circle1.area()
y = circle1.circumference()
print(x,y)


class Animal:
    def __init__(self,name):
        self.name = name

    def walk(self):
        print(f"{self.name}!걷는다!!!")
    def eat(self):
        print(f"{self.name}!먹는다!!!")

class Dog(Animal):
    def run(self):
        print(f"{self.name}!달린다!")
    def bark(self):
        print(f"{self.name}!짖는다!")
class Bird(Animal):
    def fly(self):
        print(f"{self.name}!푸드덕!")

dog = Dog('꼽이')
dog.run()
dog.bark()

bird = Bird("구구")
bird.walk()
bird.fly()
bird.eat()

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self,p1,p2) -> None:
        self.p1 = p1
        self.p2 = p2
    def get_area(self):
        return (self.p2.x - self.p1.x) * (self.p1.y - self.p2.y)
    def get_perimeter(self):
        return ((self.p2.x - self.p1.x) + (self.p1.y - self.p2.y))*2
    def is_square(self):
        if (self.p2.x - self.p1.x) == (self.p1.y - self.p2.y) :
            return True
        else :
            return False

p1 = Point(1,3)
p2 = Point(3,1)
r1 = Rectangle(p1,p2)

print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3= Point(3 , 7)
p4 = Point(6 , 4)
r2 = Rectangle(p3 , p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

class Stack:
    def __init__(self) -> None:
        self.S_list = []

    def empty(self):
        if len(self.S_list) == 0:
            return True
        else :
            return False
    def top(self):
        try :
            k = self.S_list[-1]
            return k
        except:
            return None
    def pop(self):
        try :
            k = self.S_list[-1]
            self.S_list = self.S_list[:-1]
        except:
            return None

    def push(self,new):
        self.S_list.append(new)
    def __repr__(self) -> str:
        return self.S_list

stack = Stack()
print(stack.empty())
print(stack.push("absd"))
print(stack.top())
# print(repr(stack))
print(stack.pop())
print(stack.empty())

import datetime

# a = datetime.datetime(2022927)
# str(a)
# repr(a)

# 실습
class Human:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    
    def details(cls):
        pass
    def check_age(self):
        if self.age < 19:
            return False
        else :
            return True


class PublicTransport:
    def __init__(self,name,fare) -> None:
        self.name = name
        self.fare = fare
        self.now_passanger = 0
        self.total_passanger = 0
    def get_in(self, passanger):
        self.now_passanger += passanger
        self.total_passanger += passanger
    def get_out(self,passanger):
        self.now_passanger -= passanger

    def profit(self):
        result = self.total_passanger * self.fare
        return result

bus = PublicTransport("bus", 89)
bus.get_in(6)
bus.get_out(5)
bus.get_in(60)
print(bus.profit())
