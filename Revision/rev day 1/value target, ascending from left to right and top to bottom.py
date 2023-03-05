def search_matrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    i, j = 0, n-1
    
    while i < m and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            i += 1
        else:
            j -= 1
    
    return False
m = int(input('Enter the number of rows: '))
n = int(input('Enter the number of columns: '))

matrix = []

for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f'Enter element ({i+1},{j+1}): '))
        row.append(element)
    matrix.append(row)

print('Input matrix:')
for row in matrix:
    print(row)

target=int(input("Target: "))
print(search_matrix(matrix, target))
