class MatrixOperations:
    def __init__(self):
        self.get_matrix = []
        self.row = int(input("ENTER NUMBER OF ROWS\n"))
        self.cols = int(input("ENTER NUMBER OF COLS\n"))
        for i in range(self.row):
            row1 = []
            for j in range(self.cols):
                elements = int(input("Enter element row wise"))
                row1.append(elements)
            self.get_matrix.append(row1)
        

    # Function for Addition of matrices
    def Add_matrix(self, B):
        if self.row != B.row or self.cols != B.cols:
            print("Addition not possible")
        else:
            ans_matrix = []
            for i in range(self.row):
                row1 = []
                for j in range(self.cols):
                    values = self.get_matrix[i][j] + B.get_matrix[i][j]
                    row1.append(values)
                ans_matrix.append(row1)
            for ROWS in ans_matrix:
                print(ROWS,end = " ")
                print()

    # Function for Subtraction of matrices
    def Subtract_matrix(self, B):
        if self.row != B.row or self.cols != B.cols:
            print("Subtraction Not possible")
        else:
            ans_matrix = []
            for i in range(self.row):
                row1 = []
                for j in range(self.cols):
                    values = self.get_matrix[i][j] - B.get_matrix[i][j]
                    row1.append(values)
                ans_matrix.append(row1)
            for ROWS in ans_matrix:
                print(ROWS, end=" ")
                print()

    # Function for Multiplication of matrices
    def Multiply_matrix(self, B):
        if self.cols != B.row:
            print("Multiplication not possible")
        else:
            ans_matrix = []
            for i in range(self.row):
                row1 = []
                for j in range(B.cols):
                    SUM_PROD = 0
                    for k in range(self.cols):
                        SUM_PROD += self.get_matrix[i][k] * B.get_matrix[k][j]
                    row1.append(SUM_PROD)
                ans_matrix.append(row1)
            for row in ans_matrix:
                print(row, end=" ")
                print()

    # Function for Transpose of a matrix
    def Transpose_matrix(self):
        ans_matrix = []
        for j in range(self.cols):
            row1 = []
            for i in range(self.row):
                row1.append(self.get_matrix[i][j])
            ans_matrix.append(row1)
        for row in ans_matrix:
            print(row, end=" ")
            print()


# Main code
matrix_A = MatrixOperations()
matrix_B = MatrixOperations()
while True:
    print("--------Choice----------")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. TRANSPOSE")
    choice = int(input("Enter chpoice\n"))
    if choice == 1:
        
        print("\nMatrix A + Matrix B:")
        matrix_A.Add_matrix(matrix_B)

    elif choice == 2:
        print("\nMatrix A - Matrix B:")
        matrix_A.Subtract_matrix(matrix_B)

    elif choice ==3:
        print("\nMatrix A * Matrix B:")
        matrix_A.Multiply_matrix(matrix_B)
    
    elif choice == 4:
        print("\nTranspose of Matrix A:")
        matrix_A.Transpose_matrix()

    elif choice == 5:
        print("BYE!!!!!")

    else:
        break
