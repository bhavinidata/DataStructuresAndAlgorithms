# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000?
# ======================================================

def findPowerDigitSum(num, power):
    powDigtSum = 0
    totPower = num ** power
    for num in str(totPower):
        powDigtSum += int(num)
    return powDigtSum

if __name__ == '__main__':
    num = 2
    power = 1000
    powDigtSum = findPowerDigitSum(num, power)
    print(f"Power Digit sum: {powDigtSum}")