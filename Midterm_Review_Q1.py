# One of your colleagues has written the following functions.
# Get_Score(user_name)
# which returns a test score for the user student_name.
# and
#
# Get_average(total, number_of_students)
# which returns the average of all the scores.
# They have saved these functions in a file named scores.py.
# Using these two functions, write a function main() that does the following
#
# Assuming that there are 100 students in the class, use For Loop to
# 1.1 Ask user to enter their name
# 1.2 Use the Get_score(user_name)function to get the user’s score
# Calculate the total score
# Calculate the test score average by using the function Get_average(total, number_of_students) function
# Note: You are required to use the two functions that your colleague has written to perform the tasks of getting
# user inputs and calculating the total. Do not define these functions again.
# Without comments, your program should be no longer than 7-8 lines


def factorial(n):
    print(f"factorial() called with n = {n}")
    return_value = 1 if n <= 1 else n * factorial(n -1)
    print(f"-> factorial({n}) returns {return_value}")
    return return_value


def is_palindrome(input):
    # """Return True if word is a palindrome, False if not."""
    if len(input) <= 1:
        return True
    else:
        return input[0] == input[-1] and is_palindrome(input[1:-1])


def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)

def power(num, topwr):
    if topwr == 0:
        return 1
    else:
        return num * power(num, topwr - 1)


def sumnums(n):
    if n == 1:
        return 1
    return n + sumnums(n - 1)


def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]


def GCD(a, b):
	low = min(a, b)
	high = max(a, b)

	if low == 0:
		return high
	elif low == 1:
		return 1
	else:
		return GCD(low, high%low)

def toh(n,start,end,aux):
  if(n==1):
    print("Move disk 1 from",start,"to",end)
    return
  toh(n-1,start,aux,end)
  print("Move disk",n,"from",start,"to",end)
  toh(n-1,aux,end,start)

def LCM(a, b):
    t = a % b
    if t == 0:
        return a
    return a * LCM(b, t) / t

def sumDigits(no):
    if no == 0:
        return 0
    else :
        return int(no % 10) + sumDigits(int(no / 10))

# Q1

numStudents = 100
totalScore = 0

for i in range(0, numStudents):
    studentName = input("Enter your name")
    totalScore += Get_score(studentName)
average = Get_average(totalScore, numStudents)











num_students=100
total=0
for i in range(num_students):
    name=input("Enter your name \n")
    total+=Get_score(name)
average=Get_average(total,num_students)