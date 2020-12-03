# Created by Leon Hunter at 9:54 AM 10/23/2020
class Calculator(object):
    def add(self, a, b):

        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        a = float(a)
        return a / b
        #if a != 0 and b != 0:
         #   div = a / b
         #   return div
       # else:
        #    return ZeroDivisionError
