'''
#we want to see list of all keywords
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
'''
value=input("enter any value from keyboard")
print(value)
print(type(value)) #OOPS concept- every val in python is object of a class
#by default input() func only accept string values
#type casting->changing a datatype to another datatype
#methods ->int(),str(),float()..
value=int(input("enter any no from keyboard"))
print(value)
print(type(value))
print(1,2,3,4,sep='#',end='&')
#samplefile here is a file oject open for writing
samplefile=open('C:/Users/vaish/OneDrive/Desktop/igdtuw ai ml internship/demo.txt','w')
#two modes to open a file-'r' for reading and 'w' for writing
print(1,2,3,4,sep='%',end='$$',file=samplefile)
print("Hello all {} people in class".format("10"))
str1=input("enter no of ppl in class")
print("Hello all {} people in class".format(str1))
str1="hello"
str2="welcome!!"
str3=str1+str2
print(str3)
# + operator is and overloaded operator that can combine 2/more similar type of objects
num1=10
print("the num is:",num1,"the type is:",type(num1))
num2=10.12
print("the num is:",num2,"the type is:",type(num2))
num3=10+5j
print("the num is:",num3,"the type is:",type(num3))
#no system
#int base 10
#binary base 2 for using binary no->prefix 0b or 0B
print(0b101)
print(0B1011)
#octal base 8 -> prefix 0o or 0O
print(0o156)
#hexadecimal -> prefix 0x or 0X
print(0xAFB)# 0 to 9, 10-A,11-B...15-F
#implicit -> automatic conversion of smaller date type to bigger data type
print(100+15.67)#here int 100 automatically gets coverted to float 100.00
#explicit conversion->bigger to smaller datatype conversion
val=(-55.88)
print(int(val))
val1=complex("10+3j")
print(val1)
print(type(val1))#string 10+3j converted to complex np
#number based modules -> random and math modules
#random module -> generate nos randomly on the fly
import random
print(random.randrange(20,50))#generates any no in given range
print(random.random())#generates any no
#use random to pick a val randomly from a sequence
list1=["hello","bye","hi","go",'y','a']
print(random.choice(list1))
random.shuffle(list1)
print(list1)
#math module
#aliases means nick names
import math as mt    #mt as alias name for math
print(mt.factorial(5))
print(mt.pi)
print(mt.log(100000000))
print(mt.pow(2,3))
#sequence data->list,string and tuple
#list ->v flexible seq of data as it allows all sort of modification
# data in list can be of diff datatypes
#data starts from index position 0
#characterisitics of list->order by position,mutable can be modified easily,duplicate val r allowed
list1=[1,2,3,"hello","bye",12.77,True,False,'go']
print("first ele",list1[0])
print("second ele",list1[1])
#if we acceess list drom L->R index starts frm 0
#if we acceess list drom R->L(start from bakcwards/end) index starts frm -1
print("last ele",list1[-1])
print("second last ele",list1[-2])
#tuples()->seq of data having positions of elements but it is immutable
#if we acceess list drom L->R index starts frm 0
#if we acceess list drom R->L(start from bakcwards/end) index starts frm -1
#it contains data of any type
tup1=(1,2,3,"hello","bye",True,12.66)
print("first ele",tup1[0])
print("second ele",tup1[1])
print("last ele",tup1[-1])
print("second last ele",tup1[-2])
list1=[1,2,3,"hello","bye",12.77,True,False,'go']
print("original list",list1)
list1[-1]="gonow"#this is not possible in case of immutable tupple
print("modified mutable list",list1)
#Dictionary,Set-> collection of data with no index
#dictionary{}->values in form of key:val pairs
#each val is recognized by unique key
dict1={'Name':"Ajay","Age":20,"salary":200000.15,"house no":20}
print(dict1["salary"])
print(dict1.keys())
print(dict1.values())
print(dict1.items())
dict1["degree"]="B.TEch."
print(dict1)
#Set{}->no duplicate elements r allowed
set1={1,2,3,4,4,5,5,3,3,2,2,1}
print(set1)
