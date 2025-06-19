#Types of operators in python
#Numeric : 1)Integer 2)Float 3)Complex Numbers
#Dictionary
#Boolean
#Set 
#Sequence Type: 1)String 2)List 3)Tuple

x=50 #This is integer
x=60.5 #This is float
x="Hello World" #This is string
x=["Abhishek","Kumar","Singh"] #This is list
#1)List is mutable
#2)List is ordered 
#3)Can contain duplicates
#4)Uses square brackets
x=["3","2","1"]
# print(x)
print(sorted(x))

x=("Abhishek","Kumar","Singh") #This is tuple
#1)Tuple is immutable
#2)Tuple is ordered 
#3)Can contain duplicates
#4)Uses open brackets


x={1,2,3,4,5,5,6,1,2}
#1)set is mutable
#2)set is unordered 
#3)no duplicates allowed 
#4)Uses curly brackets
print(x)

a=5
print(type(a))
b=10.5
print(type(b))
c=2+4j
print(type(c))

s="Hello Abhishek Singh"
print(type(s))
#Accessing elements direclty from String
print(s[1])
print(s[6])
print(s[-2])

#tuple dataType
tup2=('Abhishek','Singh')
print("\nTuple with String is: ", tup2)
print(tup2[0])
print(tup2[-1])

#Boolean Data type 
print(type(True))
print(type(False))

#Set Data type in python
s1= set()
s1= set("GeeksForGeeks")
print(s1)
s2=set("AbhishekSingh")
print(s2)