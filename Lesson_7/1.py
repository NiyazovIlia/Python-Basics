class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self):
        new_list_1 = str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.list_1]))
        new_list_2 = str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.list_2]))
        return print(f'Первая матрица: {new_list_1}\n'
                     f'Вторая матрица: {new_list_2}')


my_matrix = Matrix([[5, 18, 11],
                    [6, 17, 23],
                    [41, 50, 9]],
                   [[45, 8, 2],
                    [6, 7, 93],
                    [24, 5, 97]])

print(my_matrix.__add__())
