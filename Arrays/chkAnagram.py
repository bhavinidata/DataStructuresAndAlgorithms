# Construct an algorithm to check whether two words (or phrases) 
# are anagrams or not!
# ================================================

def chkAnagramStr(inputStr1, inputStr2):
    result = True
    inputStr1.strip()
    inputStr2.strip()
    inputStr1 = inputStr1.replace(" ", "")
    inputStr2 = inputStr2.replace(" ", "")
    inputStr1 = inputStr1.lower()
    inputStr2 = inputStr2.lower()
    print(inputStr1)
    print(inputStr2)
    if len(inputStr1) != len(inputStr2):
        return False
    else:
        for chr in inputStr1:
            if chr not in inputStr2:
                return False
        return result

if __name__ == '__main__':
    # inputStr1 = "William Shakespeare"
    # inputStr2 = "I am a weakish speller"
    inputStr1 = "restful"
    inputStr2 = "fluster"
    result = chkAnagramStr(inputStr1, inputStr2)
    if result == True:
        print("Input strings are anagram")
    else:
        print("input strings are not anagram")