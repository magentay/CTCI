# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.

def setZeros(matrix):
    n = len(matrix)
    m = len(matrix[0])
    row = [0]*n
    column = [0]*m
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = 1
                column[j] = 1
    
    for i in range(n):
        for j in range(m):
             if row[i] == 1 or column[j] ==1:
                 matrix[i][j] = 0
                 
                 
    return matrix
