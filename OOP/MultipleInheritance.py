#!/usr/bin/python3

'''technically all multiple inheritance in python3 is diamond,
because all classes inherit from object '''

#diamond problem in below code, Baseclass method will be called twice

class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("Calling method on Base class")
        self.num_base_calls += 1

class LeftSubClass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        super().call_me()    
        print("Calling method on left subclass")
        self.num_left_calls += 1

class RightSubClass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        super().call_me()   
        print("Calling method on  right sublcass")
        self.num_right_calls += 1

class SubClass(LeftSubClass, RightSubClass):
    num_sub_calls = 0 
    def call_me(self):
        super().call_me() 
        print("Calling method on the sublcass")
        self.num_sub_calls += 1
        
''' with multiple Inheritance, we only want to call the "next" method
in the class hierarchy, not the "parent" method" '''


s = SubClass()
s.call_me()

print(s.num_sub_calls, s.num_left_calls,s.num_right_calls,s.num_base_calls)
