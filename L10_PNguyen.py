#Authors: Peter Nguyen
#Assignment: Lab #10
#Completed (or last revision): 11/27/22

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

#Task 1 Outputs
# What would you like to check if it is a palindrome? race car
# The string is a palindrome

# What would you like to check if it is a palindrome? no lemon, no melon    
# The string is a palindrome

# What would you like to check if it is a palindrome? never odd or even
# The string is a palindrome


# #Task 2
# intList = [5, 2, 12, 4, 9, 13, 22, 1, 6, 17]
# nameList =  ["Kate", "Sam", "Kate", "Jolly", "Alp", "Beta", "Alpine", "Samuel", "Bob", "Joy"]
# intNameList = [("Kate", 3), ("Sam", 2), ("Kate", 5), ("Jolly", 1), ("Alp", 2), ("Beta", 3), ("Alp", 1), ("Alpine", 2), ("Sam", 4), ("Bob", 2), ("Sam", 3)]

# def sort(list):
#      n = len(list)
#      if(isinstance(list[0],str)):
#           for i in range(n):
#                for j in range(0, n - i - 1):
#                     if list[j] > list[j + 1]:
#                          list[j], list[j + 1] = list[j + 1], list[j]
#      elif(isinstance(list[0],tuple)):
#           for i in range(n):
#                for j in range(0, n - i - 1):
#                     if list[j] > list[j + 1]:
#                          list[j], list[j + 1] = list[j + 1], list[j]
#           for i in range(n):
#                for j in range(0, n - i - 1):
#                     if list[j][0] == list[j + 1][0] and list[j][1] < list[j+1][1]:
#                          list[j], list[j + 1] = list[j + 1], list[j]
#      else:
#           for i in range(n):
#                for j in range(0, n - i - 1):
#                     if list[j] < list[j + 1]:
#                          list[j], list[j + 1] = list[j + 1], list[j]
#      return list

# def main():
#      print(sort(intList))
#      print(sort(nameList))
#      print(sort(intNameList))
     
# main()

# #Task 2 Output
# # [22, 17, 13, 12, 9, 6, 5, 4, 2, 1]
# # ['Alp', 'Alpine', 'Beta', 'Bob', 'Jolly', 'Joy', 'Kate', 'Kate', 'Sam', 'Samuel']
# # [('Alp', 2), ('Alp', 1), ('Alpine', 2), ('Beta', 3), ('Bob', 2), ('Jolly', 1), ('Kate', 5), ('Kate', 3), ('Sam', 4), ('Sam', 3), ('Sam', 2)]