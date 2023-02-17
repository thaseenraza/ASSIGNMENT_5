# Challenge 1: Square Numbers and Return Their Sum
# 🔴 In this challenge, you need to implement a method that squares passing variables and returns their sum.

# Problem statement: Implement a class Point that has three properties and a method. All these attributes (properties and methods) should be public. This problem can be broken down into two tasks:

# Task 1: 👉 Implement a constructor to initialize the values of three properties: x, y, and z.

# Task 2: 👉 Implement a method, sqSum(), in the Point class which squares x, y, and z and returns their sum.

# Sample properties 1, 3, 5

# Sample method output 35



class point:
    def __init__(self,var1,var2,var3):
        self.var1 = var1**2
        self.var2 = var2**2
        self.var3 = var3**2
        print("The squares of inputs are : ",(self.var1 ,self.var2 ,self.var3))
    def sqsum(self):
        total = self.var1 + self.var2 + self.var3
        return total
var1 = int(input("Enter the var1 : "))
var2 = int(input("Enter the var2 : "))
var3 = int(input("Enter the var3 : "))
obj_point = point(var1,var2,var3)
totalsum = obj_point.sqsum()
print("The Sum of the squares are : " ,totalsum)
obj_point.sqsum()