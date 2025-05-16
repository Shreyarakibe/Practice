
#REVERSE A STRING
s = "Hello"
print(s[::-1])

#FIND MAX ELEMENT FROM A LIST
num = [2,8,10,17,80,3]
print(max(num))

#SUM OF ALL ELEMENTS OF A LIST
l = [1,2,3,4,5]
print(sum(l))

#MOVE ALL ZEROES AT THE END OF THE LIST
a = [0,3,45,0,6,0,2,12,60,4,45, 0]
for i in a:
    if i ==0:
        a.remove(i)
        a.append(i)
print(a)

#REARRANGE ELEMENTS IN A LIST ACCORDING TO THE GIVEN INDEX
b = [50,40,70,60,90]
c = [3,0,4,1,2]

def rearrange(b, c):
    new = [0] * len(b)
    for i in range(len(b)):
        new[c[i]] = b[i]
    return new

print(rearrange(b, c))

#FIND REPEATING ELEMENTS IN A STRING
n = "ShreyaRakibe"
res = []

for c in set(n):
    if n.count(c)>1:
        res.append(c)
print(res)        
        
#FIND THIRD LARGEST ELEMENT 
m = [3, 5, 1, 7, 2, 22, 10]
sorted = m.sort(reverse = True)
print(m[2])

#SHIFT ALL NEGATIVE ELEMENTS AT THE END
l = [1, -1, 3, 2, -7, -5, 11, 6]
if i<0:
    l.remove(i)
    l.append(i)
    print(l)    

#CHECK IF SECOND STRING IS PRESENT IN FIRST STRING
s1 = "Shreya"
s2 = "abc"
if s2 in s1:
    print("Yes")
else:
    print("No")    

#FIND MIN ELEMENT IN ARRAY
a1 = [78, 69, 45, 55, 37, 89]
print(min(a1))

#FIND ELEMENT WHICH IS GREATER THAN ITS NEIGHBOURS 
h = [12, 45, 22, 78, 36, 55]
for i in range(len(h)-1):
  if h[i] > h[i-1] and h[i] > h[i+1]:
      print(h[i])

#CREATE A MATRIX
import numpy as np
r = [["shreya", 42, "it"], 
     ["samiksha", 20, "comp"],
     ["urvi", 56, "it"]]

print(np.array(r))  
#TRANSPOSE A MATRIX
print(np.transpose(r))
       
#FIND THE NO OF ZEROES INN A ARRAY
w = [45, 3, 0, 3, 0 , 5, 0, 6, 0, 0, 7, 3]
print(w.count(0))     

#REMOVE DUPLICATE ELEMENTS FORM AN ARRAY
g = [1, 5, 4, 5, 3, 6, 7, 8, 2, 1, 9, 5, 6, 4]
print(list(set(g)))

#ADDITION OF BINAFRY NUMBERS
a = "11"
b = "1"

result = bin(int(a,2) + int(b,2))
print(result[2:])

##Show the current time
# import time
# # timestamp = time.strftime('%H:%M:%S')
# # print("The current time is:", timestamp) 
# hour = int(input("Enter the time: "))

# if hour > 0 and hour < 12:
#     print("Good Morning")

# elif hour >= 12 and hour < 17:
#     print("Good Afternoon")

# else:
#     print("Good Evening")        


# #swapping two numbers
# num1 = 10
# num2 = 20

# print("value of num1 before swapping: ", num1)
# print("value of num2 before swapping: ", num2)

# temp = num1
# num1 = num2
# num2 = temp

# print("value of num1 after swapping: ", num1)
# print("value of num2 after swapping: ", num2)

##Roman to Integer
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         a = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#         total = 0
#         prev = 0
#         for char in s:
#             value = a[char]
#             if value > prev:
#                 total = total + value - 2 * prev
#             else:
#                 total = total + value
#             prev = value
#         return total 
        
# s = Solution()
# roman_string = input("Enter the roman string: ")
# print(s.romanToInt(roman_string))


