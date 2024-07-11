def transpose(matrix):
    if not matrix or not matrix[0]:
        return []
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return transposed


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = transpose(matrix)
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed:
    print(row)
