print("BASIC INPUT AND OUTPUT\n")
name = "bhuna"
age = int(input("enter age"))
print("my name is : ", name)
print("my age is: ", age)
print(f"age {age} using the f string")
floating_number = 9.8304920
print(f"floating number {floating_number: .2f}")
print("using seperator: " ,"a", "b", sep = "~")
print("using end" ,"hello all: ", end = "00")
print("")

# concatination , addition
# print(name + age) error
print("\nCONCATINATION\n")
print("add 2 nums ", age + age)
print("add / concat 2 stirngs" ,name + " " + name)

print("\nOPERATORS\n")
# operators
a = 20
b = 3
print("addition: ", a + b)
print("subtration: ", a - b)
print("Multiplication: ", a * b)
print("Modulo: ", a % b)
print("Power: ", a ** b)
print("Division: ", a / b)
print("Floor Division: ", a // b)


# data types

int_type = 10 
float_type = 10.3
str_type = "hello"
bool_type = True
none_type = None
complex_type = 3+2j

# type casting 
# implicit
print("\nTYPE CASTING _ IMPLICIT\n")
int_number = 10
float_number = 20.8
print("implicit_cast: ", int_number + float_number)
# str + int or str + float errors 
# error print("TRUE" + True)

#explicit

print("\nTYPE CASTING _ EXPLICIT\n")
int_num = 10
float_num = 10.22
str_chars = "hi"
str_num = "22"
print("int to float: ", float(int_num) )
print("float to int:  ",int(float_num) )
print("str to int: ", int(str_num) )
print("bool to int: ", int(True))
print("bool to int: ", int(False))
print("bool to str: ", str(True))
print("str to bool:" , bool("true"))
print("complex : " , complex(3, 3))

#docstrings
print("\nDOCSTRINGS\n")
def person(age, name):
    '''
    input:
    age: int
    name: str
    '''
    print("doctring of function:" ,person.__doc__)
person(20, "sriya")



#strings
print("\nSTRINGS\n")
'''
Array of characters
Immutable: even if we perform operations then the original string is not changed, should store into anoher or can print
In indexing runs untill n - 1
'''
name ="bhuvaneswari"
greeting = "good morning !!!"
# name[0] = "k" error immutable
print("length of string: ", len(name))
print("string slicing: ", name[2:10])
print("string slicing no start: ", name[:10])
print("string slicing no end: ", name[2:])
print("string slicing with step: ", name[2:10:2])
print("string with negative indexing: ", name[-4:-1])
# -4 we use len-4 then it is simple , 12 - 4 = 8 to 12 - 1 =11

#methods 
print("convert to upper case: ", name.upper())
print("convert to lower case: ", name.lower())
print("checks is upper: ", name.isupper)
print("checks is lower: ", name.islower())
print("rstrip removes trailing chars:  ", greeting.rstrip("!"))
print("Split into list: ", greeting.split(" "))
print("replaces the word with another: ", name.replace("bhuvaneswari", "dhanvika"))
print("capitalize converts first char into upper and all others into small: ", name.capitalize())
print("title converts first letter of every word into upper case: ", greeting.title())
print("check title: ", greeting.istitle())
print("count occurances: ", name.count("b"))
print("find and return first occurance and returns -1 if not found: " ,greeting.find("goods"))
print("index find  and return first occurance and raise error if not found: " ,greeting.index("good"))
print("checks ends with:  ", greeting.endswith("!"))
print("checks starts with: ", greeting.startswith("!"))
print("checks is alph , num: ", greeting.isalnum())
print("if printable not like newlines : ",greeting.isprintable())
print("Swaps the cases: ", greeting.swapcase())


# conditional statements
print("\nCONDITIONAL STATEMENTS\n")
age = int(input("enter age to check whether you are eligible to vote"))
if age > 18:
    print("You are adult, you can vote")    
elif age < 18:
    print("You are a child, you cant vote")
else:
     print("it is your first vote ")

#match case 
print("\nMATCH CASE\n")
age = int(input("enter age to check your activities match case"))
match age:
    case 10:
        print("You need to study ")
    case 3:
        print("You can stay at home and play")
    case _ if age > 20:
        print("You can do a job")
    case _:
        print("You do nothing ")


#loops 
print("\nLOOPS \n")
#for loop
number = int(input("enter a limit"))
for i in range(number):
    print(i, end = ",")
fruits=['apple', 'banana']
print("printing fruits in a list")
for fruit in fruits:
    print(fruit)

#range function

print("\nRANGE FUNCTION\n")
print("range function with start,end,step :",end = ",")
for i in range(0,10,2):
    print(i, end = ",")
print("\nrange function with start: ", end = ",")
for i in range(3):
    print(i, end = ",")

print("\nrange function with start,end: ",end = ",")
for i in range(0,2):
    print(i, end = ",")


#while loop

print("\nWHILE LOOP \n")
num = int(input("\nenter the num to print the table"))
i = 1
while num!= 0 and i<=10:
    print(f"{num} X {i} = {num*i}")
    i = i + 1

#do while loop 

print("\nDO WHILE LOOP \n")
number = int(input("enter any number , this loop prints nums untill 30 "))
while(True):
    print(number,end = ",")
    if number >= 30 : 
        break 
    number = number + 1

#functions:
print("\nFUNCTIONS \n")
def person(name,age):
    output = f"\nyour name is {name}, your age is {age}"
    return output
name = input("\nenter name to pass as arg to function")
age = input("\nenter age to pass as arg to function")
function_output = person(name,age)
print(function_output)

def fruits(*fruits_names):
    print(fruits_names)
fruits_output = fruits('apple', 'banana')

#lists
print("LISTS")
'''
Mutable
allows duplicates
different data types
ordered
'''
colors = ['orange', 'red' , 'green']
fruits = ['grapes', 'mango', 'blueberry']
colors.append('black')
print("appended a new item to list: ", colors)
colors.extend(fruits)
print("extend another list: ", colors)
colors.insert(2,"yellow")
print("insert item at required position: ", colors)
colors.pop(2)
print("pop the item in the given  position: ", colors)
colors.remove("red")
print("remove the given item: ", colors)

colors.reverse()
print("reverse the items: ",colors)
colors.sort()
print("after sort: ",colors)
colors.sort(reverse = True)
print("sort in reverse (descending): ",colors)
new_colors = colors.copy()
print("new list by copying: ", colors)
concat_lists = fruits + colors
print("concatinating 2 lists: ", concat_lists)
print("count element in list: ", concat_lists.count("mango"))
print("index of item in list return error if not found: ",colors.index("black"))
#slicing can also be performed on lists 

#tuples

print("\nTUPLES \n")
'''
Immutable
allows duplicates
different data types
ordered
'''
single_element_tuple = (1)
print("type of var with single element  without , in (): ",type(single_element_tuple ))
single_element_tuple = (1,)
print("type of var with single element , commma in (): ", type(single_element_tuple ))
numbers_tuple1 = (1,2,3)
numbers_tuple2 = (4,5,6)
numbers_tuple3 = numbers_tuple1 + numbers_tuple2
# numbers_tuple_1[0] =9 error
print("count item in tuple: ",numbers_tuple1.count(1))
print("index of element in tuple, raise error if not found: ",numbers_tuple2.index(6))

#sets
print("\nSETS\n")
'''
mutable
Unique values no duplicates
different data types
unordered
'''
num_set = {1,2,3,4,4}
char_set = {'a', 'b', 2}
print("printing the set" ,num_set)
num_set.add(33)
print("added element :" ,num_set)
print("remove element raise error if item not present :", num_set.remove(33))
print("discard element not raise error :", num_set.discard(33))
# print(num_set[0]) because no order
combo_set = num_set.union(char_set)
#no update on original set 
num_set.update(char_set)
print("first set updated with second set items: ", num_set)
combo_2 = num_set.intersection(char_set)
print("intersection of two sets: ", combo_2)
num_set.intersection_update(char_set)
print("intersection_updates the first set with the output: ",num_set)
#symmetric difference set means the items that are not common 
print("symmetric_differenece displays the data that is not common of both sets: ", num_set.symmetric_difference(char_set))
#difference is presen in first set but noyt in second set 
print("diplays the elements that are present in first set but not in second set: ", num_set.difference(char_set))

#dictionary
'''
dict Mutable
immutable, unique keys
ordered 
'''
print("\nDICTIONARY\n")
person ={"name":"tabu", "age":19}
person2 = {"name":"kiara", "age":20}
print("printing dict",person)
print("using get to obtain the value: " ,person.get("name"))
print("using accessing", person["name"])
print("using update to add additional items", person.update({"eligible":True}))
print("using update to add another dict: ", person.update(person2))
print("using pop to remove required item: ", person.pop("eligible"))
print("using popitem to remove the last item: ", person.popitem())
print("using clear to remove the items in the list: ", person.clear())
del person2["name"]
#del can be used in lists also 


#exception handling 
print("EXCEPTION HANDLING\n")
def exception_handling():
    try:
        num1 = int(input("enter the numerator"))
        num2 = int(input("enter the denominator"))
        divide = num1 / num2
        return divide
    except ValueError:
       return "values is not correct"
    except ZeroDivisionError :
        return "num cant divide by zero"
    finally:
       print("Division operation uses the 2 operands")
    #finally is the main code that is to be worked even if the code has no errors or the code has errors
exception_call = exception_handling()
print(exception_call)

try: 
    number = int(input("enter a number greater than 10 to check the raise exception"))
    if number > 10 :
        raise ValueError("The entered valueis invalid ")
except ValueError:
    print("this is a error occured due to adding the value more than 10")


#shorthand if else
age = 100
pension = True if age > 70 else False 
print(pension)