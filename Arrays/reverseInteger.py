# Our task is to design an efficient algorithm to reverse 
# a given integer. For example if the input of the algorithm 
# is 1234 then the output should be 4321.

# ====================================================

def reverseNum(inputNum):
    reversedNum = 0
    reminder = 0
    while(inputNum>0):
        reminder = inputNum%10 
        reversedNum = reversedNum*10 + reminder 
        inputNum =inputNum//10
    return reversedNum

if __name__ == '__main__':
    inputNum = 1234
    reversedNum = reverseNum(inputNum)
    print(f"Reversed number is: {reversedNum}")