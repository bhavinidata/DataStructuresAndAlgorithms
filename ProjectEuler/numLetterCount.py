# If the numbers 1 to 5 are written out in words: one, two, three, four, 
# five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written 
# out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

# ========================================================================
def findLetterCount(num):
    # Creation of lists containing the words
    units = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve' , 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    other = ['hundred', 'thousand', 'and']
    result = 0

    for i in range (1, num+1):
        #Extracting the digit of the units, tens, hundreds, thousands in variables
        unit = i% 10
        ten = (i // 10)% 10
        hundred = (i // 100)% 10
        thousand = (i // 1000)% 10

        if thousand != 0:
            # case for one thousand
            result += len(units[0])+len(other[1])

        if hundred != 0:
            result += len(units[hundred-1]) + len(other[0])
            if ten != 0 or unit != 0:
                # case for adding "and" after hundred (if tenth or unit place no is not 0)
                result += len(other[2])
        # for numbers like 200, 300... no need to count for tens and units
        if i%100 != 0:
            if ten>=2:
                result += len(tens[ten-2])
                if unit !=0:
                    result += len(units[unit-1])
            elif ten < 2 and ten != 0:
                result += len(units[(i%100)-1])
            elif ten == 0:
                result += len(units[unit-1])
    return result

if __name__ == '__main__':
    # this program is made to work for numbers upto thousand
    num = 1000
    letterCount = findLetterCount(num)
    print(f"Letter count from 1 to {num}: {letterCount}")