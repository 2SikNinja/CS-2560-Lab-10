#Authors: Peter Nguyen
#Assignment: Lab #10
#Completed (or last revision): 11/27/22

from math import sqrt

#Task 1
def punctuationRemover(string):
     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
     for element in string:
          if element in punctuations:
               string = string.replace(element, "")
     string = string.replace(" ", "")
     return string

def checkPalindrome(string):
     if len(string) == 0:
          return True
     if string[0] == string[-1]:
          return checkPalindrome(string.replace(string[0],""))
     else:
          return False
   

def main():
     userInput = input("What would you like to check if it is a palindrome? ")
     newString = (punctuationRemover(userInput))
     if(checkPalindrome(newString) == True):
          print("The string is a palindrome")
     else:
          print("The string isn't a palindrome")

main()

# Task 1 Outputs
# What would you like to check if it is a palindrome? race car
# The string is a palindrome

# What would you like to check if it is a palindrome? no lemon, no melon    
# The string is a palindrome

# What would you like to check if it is a palindrome? never odd or even
# The string is a palindrome





#Task 2
intList = [5, 2, 12, 4, 9, 13, 22, 1, 6, 17]
nameList =  ["Kate", "Sam", "Kate", "Jolly", "Alp", "Beta", "Alpine", "Samuel", "Bob", "Joy"]
intNameList = [("Kate", 3), ("Sam", 2), ("Kate", 5), ("Jolly", 1), ("Alp", 2), ("Beta", 3), ("Alp", 1), ("Alpine", 2), ("Sam", 4), ("Bob", 2), ("Sam", 3)]

def sort(list):
     n = len(list)
     if(isinstance(list[0],str)):
          for i in range(n):
               for j in range(0, n - i - 1):
                    if list[j] > list[j + 1]:
                         list[j], list[j + 1] = list[j + 1], list[j]
     elif(isinstance(list[0],tuple)):
          for i in range(n):
               for j in range(0, n - i - 1):
                    if list[j] > list[j + 1]:
                         list[j], list[j + 1] = list[j + 1], list[j]
          for i in range(n):
               for j in range(0, n - i - 1):
                    if list[j][0] == list[j + 1][0] and list[j][1] < list[j+1][1]:
                         list[j], list[j + 1] = list[j + 1], list[j]
     else:
          for i in range(n):
               for j in range(0, n - i - 1):
                    if list[j] < list[j + 1]:
                         list[j], list[j + 1] = list[j + 1], list[j]
     return list

def main():
     print(sort(intList))
     print(sort(nameList))
     print(sort(intNameList))
     
main()

#Task 2 Output
# [22, 17, 13, 12, 9, 6, 5, 4, 2, 1]
# ['Alp', 'Alpine', 'Beta', 'Bob', 'Jolly', 'Joy', 'Kate', 'Kate', 'Sam', 'Samuel']
# [('Alp', 2), ('Alp', 1), ('Alpine', 2), ('Beta', 3), ('Bob', 2), ('Jolly', 1), ('Kate', 5), ('Kate', 3), ('Sam', 4), ('Sam', 3), ('Sam', 2)]





#Task 3
L = [x for x in range(1,101)]

def functionOne(list):
     return list * 2

def functionTwo(list):
     if list % 2 != 0:
          return list*list
     else:
          return list
     
def functionThree(list):
     if list <= 1 :
          return
     for fac in range (2, int(sqrt(list))+1) :
          if list % fac == 0 :
               return
     return list


#Task 3 Number 1
print("Problem 1")
print("Original List", L, "\n")
result1 = map(functionOne, L)
print("New List", list(result1), "\n")

#Task 3 Number 2
print("Problem 2")
print("Original List", L, "\n")
result2 = map(functionTwo, L)
print("New List", list(result2), "\n")

#Task 3 Number 3
print("Problem 3")
print("Original List", L, "\n")
result3 = filter(functionThree, L)
print("New List", list(result3), "\n")

#Task 3 Outputs
# Problem 1
# Original List [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 
# 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# New List [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]

# Problem 2
# Original List [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 
# 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# New List [1, 2, 9, 4, 25, 6, 49, 8, 81, 10, 121, 12, 169, 14, 225, 16, 289, 18, 361, 20, 441, 22, 529, 24, 625, 26, 729, 28, 841, 30, 961, 32, 1089, 34, 1225, 36, 1369, 38, 1521, 40, 1681, 42, 1849, 44, 2025, 46, 2209, 48, 2401, 50, 2601, 52, 2809, 54, 3025, 56, 3249, 58, 3481, 60, 3721, 62, 3969, 64, 4225, 66, 4489, 68, 4761, 70, 5041, 72, 5329, 74, 5625, 76, 5929, 78, 6241, 80, 6561, 82, 6889, 84, 7225, 86, 7569, 88, 7921, 90, 8281, 92, 8649, 94, 9025, 96, 9409, 98, 9801, 100]

# Problem 3
# Original List [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 
# 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# New List [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]