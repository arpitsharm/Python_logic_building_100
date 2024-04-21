# ex1

number_1 = int(input("Enter Your Number 1 :- "))
number_2 = int(input("Enter Your Number 2 :- "))

if number_1 > number_2:
    print("The number 1 is greater")

elif number_1 < number_2:
    print("The number 2 is greater")

else:
    print("Must Be both of number are same")

# ex2

def count_words(string):
    words = string.split()
    return len(words)

string = input("Enter a string :- ")
print(count_words(string))

# ex3

string = input("Enter a string :- ")
print(len(string))

# ex4

value = int(input("Enter a value :- "))

if value % 7 == 0:
    print("yes, its divisible by 7")


else:
    print("no, its divisible by 7")

# ex5

value = int(input("Enter a value :- "))

if value % 2 == 0:
    print("even")


else:
    print("odd")