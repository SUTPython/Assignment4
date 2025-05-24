class MatrixRotator:
    def __init__(self, matrix, rotations):  # Fixed method name from init to __init__
        self.matrix = matrix
        self.r = rotations
        self.m = len(matrix)
        self.n = len(matrix[0])

    def rotate(self):
        layers = min(self.m, self.n) // 2
        for layer in range(layers):
            self._rotate_layer(layer)

    def _rotate_layer(self, layer):
        elements = self._extract_layer(layer)
        rot = self.r % len(elements)
        rotated = elements[rot:] + elements[:rot]
        self._insert_layer(layer, rotated)

    def _extract_layer(self, layer):
        elems = []
        for i in range(layer, self.n - layer):
            elems.append(self.matrix[layer][i])
        for i in range(layer + 1, self.m - 1 - layer):
            elems.append(self.matrix[i][self.n - 1 - layer])
        for i in range(self.n - 1 - layer, layer - 1, -1):
            elems.append(self.matrix[self.m - 1 - layer][i])
        for i in range(self.m - 2 - layer, layer, -1):
            elems.append(self.matrix[i][layer])
        return elems

    def _insert_layer(self, layer, values):
        idx = 0
        for i in range(layer, self.n - layer):
            self.matrix[layer][i] = values[idx]
            idx += 1
        for i in range(layer + 1, self.m - 1 - layer):
            self.matrix[i][self.n - 1 - layer] = values[idx]
            idx += 1
        for i in range(self.n - 1 - layer, layer - 1, -1):
            self.matrix[self.m - 1 - layer][i] = values[idx]
            idx += 1
        for i in range(self.m - 2 - layer, layer, -1):
            self.matrix[i][layer] = values[idx]
            idx += 1

    def print_matrix(self):
        for row in self.matrix:
            print(" ".join(map(str, row)))


if __name__ == "__main__":
    m, n, r = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(m)]
    rotator = MatrixRotator(matrix, r)
    rotator.rotate()
    rotator.print_matrix()
