#initial commit

#Printing all keyword once using kwlist()
# import keyword
# print("The list of all keywords in pythons is: ")
# print(keyword.kwlist)

#Value Keywords: True, False, None Keyword, del
# print(False == 0)
# print(True == 1)
# In python booleans have their own integer value as in True=1, False=0
# print(True + True + True)#Ans:3
# print(True + False + False)#Ans: 1
# print(None == 0)
# print(None == [])

# a= True
# b= False
# print(a and b)
# print(a or b)
# print(not b)

# print(3 in [1,2,3])
# if 's' in "Abhishek":
#     print("S is present in your name")
# else:
#     print("S is not present in your name.")

#For loop example(here for num in range means starting from 0 till 3{Excluded})
# for num in range (3):
#     if num == 2:
#       continue
#     print(num, end=' ')

#While loop example
# count =0 
# while count < 4:
#    count += 1
#    if count==3:
#       break
#    print(count, end=' ')
    
# n=10
# for i in range(n):
#    pass #pass statement used when a block of code is syntatically required but you dont want to write anything yet

#Exception handiling keyword
# a,b = 4,0
# try:
#  k=a//b
#  print(k)
# except ZeroDivisionError:
#  print("Cannot divide by zero")
# finally:
#  print("This will always execute")

# assert b != 0, "Divide by 0 error" 

# s = "GeeksForGeeks"
# print(s)
# del(s)
# print(s)

# def fun():
#     print("Inside function fun")
# fun()

#Keyword "return" and "yeild"
# def fun():
#     s=2
#     return s
# print(fun())
# def Fun():
#     yield 1
#     yield 2
#     yield 3
# for value in Fun():
#     print(value)

# g = lambda x: x*x*x
# print(g(7))

# def cubicFun():
#     g=7
#     return 7*7*7
# print(cubicFun())

# with open('file_Path','w') as file:
#     file.write('Hello World!')

# import math 
# print(math.factorial(10))

# a=15
# b=10

# def addition():
#     c=a+b
#     print(c) #Output: 25

# addition()

# def subtraction():
#     temp_var = 10
#     def subFun():
#         nonlocal temp_var 
#         temp_var -= 10 #Output: 0
#         print(temp_var)
#     subFun()

# subtraction()   

#async and await fun in py
import asyncio
async def test():
    print("Hellooo")
    await asyncio.sleep(2) # Will wait for 2 seconds and then prints below statement
    print("Abhishek Singh")
asyncio.run(test())

async def task_1():
    print("Task 1 started....")
    await asyncio.sleep(2) #await means "wait here, but let other runs meanwhile"
    print("Task 1 ended....")
async def task_2():
    print("Task 2 started....")
    await asyncio.sleep(1)
    print("Task 2 ended....")

async def main():
    await asyncio.gather(task_1(),task_2())

asyncio.run(main())