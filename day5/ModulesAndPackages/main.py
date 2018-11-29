import my_math_stuff
#from my_math_stuff import add

from tools.math import add, Pi, a_obj, A
import tools.math

class B:
    def method(self):
        pass

def my_method(self, name):
    print(self.x, name)

def main():
    print(my_math_stuff.add(3, 4))
    print(add(4, 5))
    print(tools.math.add(3, 7))

    a_obj.x = 100
    a_obj.method_stub = my_method
    a_obj.method_stub(a_obj, "John")
    #A.__dict__.update("x_printer", my_method)
    #a_obj.x_printer("John")
    print(a_obj.x)

if __name__ == '__main__':
    main()
