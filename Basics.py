# print("Abhishek kumar Singh")
# age_input = input("Enter you age: ")
# age = int(age_input)
# if age < 0:
#     print("You are minor")
# if age < 18:
#     print("You cannot vote")
# if age >= 18:
#     print("You can vote....")
# name = input("What is your name: ")
# print(name)

# a="Hello"
# b=10
# c=11.22
# d=("Abhishek","Suresh","Himanshu")
# e={"Suresh","Abhishek","Himanshu"}
# f={"Abhishek":1,"Himanshu":2,"Suresh":3}
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))

# %d –integer
# %f – float
# %s – string
# %x –hexadecimal
# %o – octal

# num = int(input("Enter a Num you will get final results with addition of 5: "))
# num += 5
# print("The final number is: %d " %num)

# x = 10
# x = "Abhishek"
# print(type(x))
# print(len(x))

# a=b=c = 100,200,300

# print(a,b,c)

a=10
def f():
    global a #10
    a = 11
f()
print(a)
    
