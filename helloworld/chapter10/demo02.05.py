import os

path = "C:\\Users\\zxz\\PycharmProjects\\helloworld\\chapter10"
tuples = os.walk(path)
for tuple1 in tuples:
    print(tuple1, "\n")
