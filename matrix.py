"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    toString=""
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            toString+=str(matrix[row][col])+" "
        toString+="\n"
    print(toString)


#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            matrix[row][col]=0
            if(row==col):
                matrix[row][col]=1

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    temp=[]
    dot=0
    for col2 in range(len(m2)):
        for col1 in range(len(m1)):
            for row1 in range(len(m1[0])):
                dot+=m1[row1][col1]*m2[col2][row1]
            temp.append(dot)
            dot=0
        m2[col2]=temp
        temp=[]



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
