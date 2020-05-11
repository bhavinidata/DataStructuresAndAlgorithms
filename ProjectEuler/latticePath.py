# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


# How many such routes are there through a 20×20 grid?
# ====================================================

def findFactorial(num):
    if num == 0: return 1
    else:
        factorial = num * findFactorial(num-1)
    return factorial

#below function will return the binomial coefficient of c,a
def findLatticePath(c, a)->int:
    routes = findFactorial(c)/(findFactorial(b)*findFactorial(c-b))
    return int(routes)

if __name__ == '__main__':
    # # for 2*2 grid
    # a, b = 2, 2
    # 20*20 grid
    a, b = 20, 20
    #Number of lattice paths from (0,0) to (a,b) is given by
    #binomial coefficient C(a+b,a)

    #binomial coefficient function
    #https://en.wikipedia.org/wiki/Binomial_coefficient
    # https://mathworld.wolfram.com/LatticePath.html
    # The number of paths of length a+b from the origin (0,0) to a point (a,b) 
    # which are restricted to east and north steps is given by the 
    # binomial coefficient (a+b; a).

    # The binomial coefficient (n; k) is the number of ways of 
    # picking k unordered outcomes from n possibilities, also 
    # known as a combination or combinatorial number. 
    # The symbols _nC_k and (n; k) are used to denote a binomial 
    # coefficient, and are sometimes read as "n choose k."

    # (n; k) therefore gives the number of k-subsets possible 
    # out of a set of n distinct items. For example, The 2-subsets 
    # of {1,2,3,4} are the six pairs {1,2}, {1,3}, {1,4}, {2,3}, 
    # {2,4}, and {3,4}, so (4; 2)=6. The number of lattice paths from
    #  the origin (0,0) to a point (a,b) is the binomial 
    # coefficient (a+b; a)

    # The value of the binomial coefficient for nonnegative n 
    # and k is given explicitly by
    #  _nC_k=(n; k)=(n!)/((n-k)!k!)
     
    c = a+b
    routes = findLatticePath(c,a)
    print(f"Number of lattice paths are: {routes}")