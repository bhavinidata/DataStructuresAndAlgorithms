# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
# it cannot be solved by brute force, and requires a clever method! ;o)

# ===============================================================
# Dynamic Programming implementation of Max path sum problem in a triangle

def findMaxPathSum(triangle)-> int:
    #Transformation of the character string into a list containing
    #sub lists (representing the lines) which contain
    #the numbers of each line
    tri = [[int (j) for j in i.strip().split()] for i in triangle.strip().split("\n")]
    # length will be the number of rows in the triangle
    length = len(tri)
    # start with the second last row. 
    #for loop for bottom-up approach
    # iteration of i means going from second last row to first row
    for i in range(length-2, -1, -1):
        # each row will have the elements corresponding to its row number
        # for ex. 3rd row (i=2) will have 3 elements (i.e i+1)
        # so here range of j is upto i
        # iteration of j is iteration within perticular row. 
        for j in range(i+1):
            # for each element, check both elements just below the number 
            # and below right to the number 
            # add the maximum of them to it 
            tri[i][j] += max(tri[i+1][j], tri[i+1][j+1])
    return tri[0][0]


if __name__ == '__main__':
    triangle = """75
    95 64
    17 47 82
    18 35 87 10
    20 4 82 47 65
    19 1 23 75 3 34
    88 2 77 73 7 63 67
    99 65 4 28 6 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 4 68 89 53 67 30 73 16 69 87 40 31
    4 62 98 27 23 9 70 98 73 93 38 53 60 4 23 """

    # # Otherwise store in .txt file and read the file
    # with open('p67triangle.txt') as f:
    #     # All the numbers in the file
    #     triangle = f.read()
    maxPathSum = findMaxPathSum(triangle)
    print(maxPathSum)