# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 


# def pascal_triangle(n):
#    trow = [1]
#    y = [0]
#    for x in range(max(n,0)):
#       print(trow)
#       trow=[l+r for l,r in zip(trow+y, y+trow)]
#    return n>=1
# pascal_triangle(6)
def pascal(n):
    Pascal = np.zeros((N, N), dtype=object)
    Pascal[0, 0] = 1
    Pascal[1,0] = Pascal[1,1] = 1
    for n in range(2, N):
        for r in range(0, n+1):
            Pascal[n, r] = Pascal[n-1, r-1] + Pascal[n-1, r]
def fun_pascaltrianglevalue(row, col):

   return 