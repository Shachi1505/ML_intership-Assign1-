#Q.1
a = int(input("first num: "))
b = int(input("second num: "))
sum = print(a+b)

#Q.2
num = int(input("Enter value "))
if(num%2==0):
    print("even")
else:
    print("odd")

#Q.3
def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fact(n - 1)

# Get user input
n = int(input("Enter val: "))

# Print the factorial of the input number
print(fact(n))

#Q.4
name = input("Enter name: ")
print("Namaste ", name)

#Q5
def toFile():
    user = input("Enter string")
    with open("otp.txt", "w") as f:
        f.write(user)
toFile()

#Q6
def fromFile():
    with open("otp.txt", "r") as f:
        cont = f.read()
        print(cont)

fromFile()

#Q.7
s = input("string is: ")
print(len(s))
 
#Q.8
s1 = "move"
s2 = " away"
print(s1+ "" + s2)

#Q.9
def present(main_str, substr):
    return substr in main_str

main_str = "May God bless us"
substr = "bless"

if present(main_str, substr):
    print("yes")
else:
    print("no")

#Q.10
s = "lily"
print(s.upper())

#Q11 : Fibonacci 
def fib(n):
    if n<=0:
      return []
    fib = [0,1]
    while len(fib) < n:
       fib.append(fib[-1] + fib[-2])
    return fib[:n]

n=10
fib = fib(n)
print(fib)

#Q12
num = 123
sum=0
for dig in str(num):
    sum += int(dig)
print(sum)

#Q13
birthyr = int(input("Enter you year of birth "))
age = 2024-birthyr
print("age is: " , age)

#Q14: reads multiple lines of input from the user until they 
#enter an empty line, then prints all the lines.
def read_lines():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if line == "":
            break
        lines.append(line)
    
    print("\nYou entered:")
    for line in lines:
        print(line)

read_lines()

#Q16: that counts the frequency of each character
def cnt(input_str):
    char_frq = {}
    for char in input_str:
        if char in char_frq:
            char_frq[char] +=1
        else:
            char_frq[char] = 1

    return char_frq

input_str = "chandra chai"
dict = cnt(input_str)

for char, freq in dict.items():
    print(freq)
#Q17
s = "chandra gupta maurya"
print(s.title())

#Q18 -> Anagrams?
s1 = "king"
s2 = "ingwk"
s1 = sorted(s1)
s2 = sorted(s2)
if(s1==s2):
    print("true")
else:
    print("false")

#Q19 ->  removes all punctuation from a given string
def rem_punc(s):
    trans = str.maketrans('', '', string.punctuation)
    return s.translate(trans)

print(rem_punc("Hello, world! How's it going?"))

#Q20 -> takes a list of numbers and returns their sum
li = [2, 3, 4]
sum=0
for val in li:
    sum += int(li)
print(sum)



