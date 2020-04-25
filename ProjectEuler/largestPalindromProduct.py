# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def largestPalindropProduct(a:int, b:int) -> str:
    product = 0
    largestPalindrom = 0
    for numa in range(b, a, -1):
        for numb in range(b, numa+1, -1):
            product = numa * numb
            prodStr = str(product)

            if prodStr == prodStr[::-1] and largestPalindrom < product:
                largestPalindrom = product
    return largestPalindrom

if __name__ == '__main__':
    result = largestPalindropProduct(99, 999)
    print(f"LargestPalindrom Product is: {result}")
