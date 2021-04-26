

class Cell:

    def __init__(self, cells, rows):
        self.cells = cells
        self.rows = rows

    def make_order(self):
        return '\n'.join(['*'*self.rows for _ in range(self.cells//self.rows)]) + '\n' + '*'*(self.cells % self.rows)

    def __add__(self, other):
        self.new_cells = self.cells + other.cells
        return '\n'.join(['*' * self.rows for _ in range(self.new_cells // self.rows)]) + '\n' + '*' * (self.new_cells % self.rows)

    def __sub__(self, other):
        if self.cells - other.cells > 0:
            self.new_cells = self.cells - other.cells
            return '\n'.join(['*' * self.rows for _ in range(self.new_cells // self.rows)]) + '\n' + '*' * (self.new_cells % self.rows)
        else:
            return 'вычитание невозможно'

    def __mul__(self, other):
        self.new_cells = self.cells * other.cells
        return '\n'.join(['*' * self.rows for _ in range(self.new_cells // self.rows)]) + '\n' + '*' * (self.new_cells % self.rows)

    def __truediv__(self, other):
        self.new_cells = self.cells // other.cells
        return '\n'.join(['*' * self.rows for _ in range(self.new_cells // self.rows)]) + '\n' + '*' * (self.new_cells % self.rows)


c1 = Cell(17, 5)
c2 = Cell(12, 7)

print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)