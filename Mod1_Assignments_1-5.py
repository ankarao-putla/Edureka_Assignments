
# 1. Write a program to find the factors of a given  number and check whether the factor is even or odd

x = eval(input("Enter a positive integer number : "))

for i in range (1,x,1):
    if x%i==0:
        if i%2==0:
            print(i, " : Factor is even")
        else:
            print(i, " : Factor is odd")
    else:
        continue


# 2. Write a code that accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.
# Hint: Use split() to split the string into a list and then apply sort()

x=input("Enter a string which is to be split into words and to be sorted alphabetically : ")
y=x.split()
y.sort()
print(y)

# 3. Write a program that will find all the numbers between 1000 and 3000 (both excluded) such that each digit of a number
#    is an odd number.    Print the number of such elements

for i in range (1001, 2999, 1):
    w=i//1000
    x=(i%1000)//100
    y=(i%100)//10
    z=i%10
    if w%2==1 and x%2==1 and y%2==1 and z%2==1 :
        print(i)
    else:
        continue

# 4. Write a program that accepts a string and calculates the number of letters and digits
#x=input ("Enter a string : ")
#x=['a']
#print(bin(x[0]))

x=input("Enter any alpha numeric string : ")
alpha=0
digit=0

for i in x:
    if i.isalpha():
        alpha=alpha+1
    elif i.isdigit():
        digit=digit+1

print(f"Given string is having {alpha} alphabets and {digit} digits")







# 5. Design a code which will find whether the given number is Palindrome number or not.
x=eval(input("Enter any integer value to check whether it is palyndrome or not : "))
x1=x
for i in range(1,1000,1):
    y=x//(10**i)
    if y==0:
        z=i   # z saves the length of the given number
        break
lst=[]
for i in range (1,z+1,1):
    lst.append(x1%10)
    x1=x1//10
#print(lst)
rev=0
for i in range(-1,-(len(lst)+1),-1):
    rev=rev+lst[i]*10**(-i-1)
if x==rev:
    print (f"Given value {x} is a palyndrome..")
else:
    print(f"Given value {x} is NOT a palyndrome")

