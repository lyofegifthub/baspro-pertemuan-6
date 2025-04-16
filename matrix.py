A = [
    [30, 2, 3, 4, 5],
    [6, 26, 8, 9, 10],
    [11, 12, 13, 14, 7],
    [16, 17, 18, 19, 1],
    [21, 22, 23, 24, 31],
]

B = [
    [2, 3, 4, 5, 6],
    [15, 16, 17, 18, 19],
    [100, 101, 102, 103, 104],
    [25, 26, 27, 28, 29],
    [29, 30, 31, 32, 33],
]

def add_matrices(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result
print("Hasil Penjumlahan Matriks A dan B:")
result = add_matrices(A, B)
for row in result:
    print(row)