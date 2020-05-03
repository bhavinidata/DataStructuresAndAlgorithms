# "A palindrome is a string that reads the same forward and backward"

# For example: radar or madam

# Our task is to design an optimal algorithm for checking whether a given string is palindrome or not! 
# =============================================
# Time complexity is O(N)

# Option:1
# def isPalindrom(inputStr):
#     result = True
#     inputStr = inputStr.lower()
#     for i in range(len(inputStr)//2):
#         if inputStr[i] != inputStr[-1-i]:
#             result = False   
#     return result

# Option:2
# def isPalindrom(inputStr):
#     result = False
#     originalStr = inputStr
#     reversedStr = inputStr[::-1]
#     if originalStr == reversedStr:
#         result = True
#     return result

# Option:3
def isPalindrom(inputStr):
    #  if we are not considering case then first transfer string to lower 
    #  inputStr = inputStr.lower()
    return inputStr == ''.join(inputStr[::-1])

if __name__ == '__main__':
    inputStr = "radar"
    # inputStr = "rAdar"
    # inputStr = "hello"
    result = isPalindrom(inputStr)
    if result == False:
        print("Input string is not palindrom")
    else:
        print("Input string is palindrom")