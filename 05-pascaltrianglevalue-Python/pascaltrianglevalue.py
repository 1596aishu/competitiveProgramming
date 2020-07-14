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



def fun_pascaltrianglevalue(row, col):
   a = []
   for i in range(row+1):
      a.append([])
      a[i].append(1)
      for j in range(1,i):
         a[i].append(a[i-1][j-1]+a[i-1][j])
         if(row!=0 and i!=0):
            a[i].append(1)
   b = a[row]
   if(len(b)>=col):
      return(b[col])
   else:
      return(0)
      