class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return result

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))



mc_1 = Matrix([[31, 22], [37, 43], [51, 86]])
mc_2 = Matrix([[3, 5], [2, 4], [-1, 64]])

print(mc_1)
print(mc_2)
print(mc_1+mc_2)
