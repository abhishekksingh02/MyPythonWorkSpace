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

def fun():
    print("Inside function fun")
fun()