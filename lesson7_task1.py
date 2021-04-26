list_1 = [[30, 20, 10], [20, 60, 80], [18, 25, 96]]
list_2 = [[56, 82, 10], [20, 15, 84], [31, 47, 61]]

class Matrix:

    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        list_3 = []
        for i in range (len(self.lists)):
            list_3.append([])
            for j in range(len(self.lists[0])):
                list_3[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, list_3))


m1 = Matrix(list_1)
m2 = Matrix(list_2)
print(m1)
print(m2)
print(m1 + m2)