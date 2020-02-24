from display import *
from draw import *
from matrix import *
import math
import random
print("\nimg.png\n\n")
s = new_screen()
c = [ 0, 255, 0 ]
print("matrix m1=:\n")
matrix = new_matrix()
print_matrix(matrix)
#p1 45,390
#p2 452,390
#p3 468,26
#p4 16,40
#matrix[0]=[45,450,20,1]
#matrix[1]=[452,378,20,1]
#draw_lines(matrix,s,c)
#matrix[2]=[452,378,20,1]
#matrix[3]=[468,26,20,1]
#draw_lines(matrix,s,c)
#matrix[4]=[468,26,20,1]
#matrix[5]=[16,40,20,1]

#matrix[6]=[16,40,20,1]
#matrix[7]=[45,450,20,1]

def land(m,count):
    if(count==0):
        matrix_lines(m,s)
    else:
        temp=new_matrix(4,8)
        averagex=int((m[0][0]+m[2][0]+m[4][0]+m[6][0])//4)
        offset1=random.randint(0,10)+random.randint(0,10)
        averagey=int((m[0][1]+m[2][1]+m[4][1]+m[6][1])//4)+offset1
        px=[]
        py=[]
        offset2=[]
        for i in range(4):
            offset2.append(random.randint(0,10)+random.randint(0,10))
            px.append(int((m[2*i][0]+m[2*i+1][0])/2))
            py.append(int((m[2*i+1][1]+m[2*i][1])/2 +offset2[len(offset2)-1]))
        for i in range(2):
            i=2*i
            temp[0]=[m[2*i][0],m[2*i][1],m[2*i][2],1]
            temp[1]=[px[i],py[i],m[2*i][2]+offset2[i],1]
            temp[3]=[averagex,averagey,m[2*i][2]+offset1,1]
            temp[5]=[px[(i-1)%4],py[(i-1)%4],m[2*i][2]+offset2[(i-1)%4],1]
            temp[2]=temp[1]
            temp[4]=temp[3]
            temp[6]=temp[5]
            temp[7]=temp[0]
            land(temp,count-1)
#land(matrix,6)
#c=[255,0,0]
#plot(s,c,0,0)

print("\nmaking identity matrix, m2:\n")
identity = new_matrix()
ident(identity)
print_matrix(identity)

print("\ntesting add edge. Adding: (50 450 0)(100 450 0) to m1:\n")
add_edge(matrix, 50, 450, 0, 100, 450, 0);
print_matrix(matrix)
print("\nadded more edges\n")
add_edge(matrix, 50, 450, 0, 50, 400, 0);
add_edge(matrix, 100, 450, 0, 100, 400, 0);
add_edge(matrix, 100, 400, 0, 50, 400, 0);

add_edge(matrix, 200, 450, 0, 250, 450, 0);
add_edge(matrix, 200, 450, 0, 200, 400, 0);
add_edge(matrix, 250, 450, 0, 250, 400, 0);
add_edge(matrix, 250, 400, 0, 200, 400, 0);

add_edge(matrix, 150, 400, 0, 130, 360, 0);
add_edge(matrix, 150, 400, 0, 170, 360, 0);
add_edge(matrix, 130, 360, 0, 170, 360, 0);

add_edge(matrix, 100, 340, 0, 200, 340, 0);
add_edge(matrix, 100, 320, 0, 200, 320, 0);
add_edge(matrix, 100, 340, 0, 100, 320, 0);
add_edge(matrix, 200, 340, 0, 200, 320, 0);
print("\n after adding a lot of edges, m1:")
print_matrix(matrix)

print("\nMultiplying identity matrix, m1, with matrix m2:\n")
matrix_mult(identity, matrix)

print_matrix(matrix)

draw_lines( matrix, s, c )

display(s)

save_extension(s,'img.png')
