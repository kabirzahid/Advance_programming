from ast import arguments
from cmath import e
from logging import exception


print("this is exceptions examples...")

a=4
b=0

try:
    print(a/a)
except ZeroDivisionError:
    print("this is an ezception")
except IOError:
    print ("io exception ...")
else:
    print("not an exception...")
finally:
    print("we didnt an exception....")