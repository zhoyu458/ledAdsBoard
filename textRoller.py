class TextRoller:
    def __init__(self, matrix):
        self.matrix = matrix
        
    def test(self):
        self.matrix[1] = (1,1,1)
        self.matrix.write()
        

