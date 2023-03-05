def sum_elements(matrix):
    m = len(matrix)
    n = len(matrix[0])
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum([matrix[i][j] for i in range(m)]) for j in range(n)]
    diagonal1_sum = sum([matrix[i][i] for i in range(min(m, n))])
    diagonal2_sum = sum([matrix[i][n-i-1] for i in range(min(m, n))])
    return row_sums, col_sums, diagonal1_sum, diagonal2_sum
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

row_sums, col_sums, diagonal1_sum, diagonal2_sum = sum_elements(matrix)
print('Row sums:', row_sums)
print('Column sums:', col_sums)
print('Diagonal 1 sum:', diagonal1_sum)
print('Diagonal 2 sum:', diagonal2_sum)
