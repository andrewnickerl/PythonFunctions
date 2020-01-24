def func1(): #uses colon + white space vs curly braces to indicate scope
    print("I am a function") #this function takes no parameter and returns no value--only executes print

def func2(arg1, arg2): #this function returns no value, only prints the two parameters it is passed
    print(arg1, " ", arg2)

def cube(x): #this function takes one parameter and returns that argument multiplied by itself three times
    return x*x*x

def power(num, x=1):  #this function takes two arguments and calculates num raised to a power x by looping x number of times and returning result
    result = 1
    for i in range(x):
        result = result * num
    return result

print(power(2))  #calls the function using x's default value
print(power(2,3)) #specifies a value for each argument
print(power(x=3, num=2)) #Python allows you to pass arguments out of order by specifying their name

def multi_add(*args): #allows a variable number of arguments (notated by *) and adds each argument to result using a for loop, then returns result
    result = 0
    for x in args: 
        result = result + x
    return result

print(multi_add(10, 4, 3, 2, 8))