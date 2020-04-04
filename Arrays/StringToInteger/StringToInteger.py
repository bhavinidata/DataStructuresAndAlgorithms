class Solution:
    def myAtoi(self, str: str) -> int:

        # Remove leading spaces
        str = str.strip()
        # check that string is not empty
        if not str:
            return 0
        negative = False
        result = 0
        # Check if there is -ve or +ve sign in front place, set the negative variable accordingly.
        if str[0] == "-":
            negative = True
        elif str[0] == "+":
            negative = False
        # check if first character is number. if not number then return zero.
        elif not str[0].isnumeric():
            return 0
        # Get the ASCII value of character and subtract ASCII value of 0 from that.
        # It will give the real integer number. 
        else:
            result = ord(str[0])-ord("0")
        # Loop through the whole input string starting from 2nd character (As first already been done.)
        for i in range(1, len(str)):
            if str[i].isnumeric():
                result = result * 10 + (ord(str[i]) - ord("0"))
                if not negative and result >= 2147483647:
                    return 2147483647
                if negative and result >= 2147483648:
                    return -2147483648
            else:
                break
        if not negative:
            return result
        else:
            return -result


if __name__ == '__main__':
    solution = Solution()
    myResult = solution.myAtoi("42")
    print(myResult)
    myResult = solution.myAtoi("-42")
    print(myResult)
    myResult = solution.myAtoi("4193 with words")
    print(myResult)
    myResult = solution.myAtoi("words and 987")
    print(myResult)
    myResult = solution.myAtoi("-91283472332")
    print(myResult)
    myResult = solution.myAtoi(" ")
    print(myResult)

