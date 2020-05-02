# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

# ====================================================

def findSeqLength(startingNum:int)->int:
    term = 0
    if startingNum == 0:
        return term
    # find if the starting number is odd or even
    if startingNum in hash_store:
        term = hash_store[startingNum]
        return term
    if startingNum %2 == 0:
        # if even then divide by 2
        term = findSeqLength(startingNum//2)
    else:
        # otherwise multiply by 3 and add 1
        term = findSeqLength((startingNum*3)+1)
    # increase number of term
    term +=1
    hash_store[startingNum] = term
    return term

if __name__ == '__main__':
    hash_store = {1:1}
    resultNum = 0
    num = 1000000
    max_count = 0
    for startingNum in range(num+1):
        seqLength = findSeqLength(startingNum)
        if seqLength> max_count:
            resultNum = startingNum
            max_count = seqLength
    print(f"Number with max callatz {max_count} term is: {resultNum}")