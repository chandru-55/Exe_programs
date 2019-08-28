class A:
    def fun(self):
        print("hi")
def monkey(self):
    print("Hi","monkey")
m.A.fun = monkey
a = m.A()
a.fun()
