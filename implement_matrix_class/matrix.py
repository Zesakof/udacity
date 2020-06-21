import math
from math import sqrt
import numbers

def zeroes(height, width):
    """
    Creates a matrix of zeroes.
    """
    g = [[0.0 for _ in range(width)] for __ in range(height)]
    return Matrix(g)

    
def identity(n):
    """
    Creates a n x n identity matrix.
    """
    I = zeroes(n, n)
    for i in range(n):
        I.g[i][i] = 1.0
    return I
    
    
def dot_product(vector_one, vector_two):
    """
    Calculates the dot product of two vectors
    """
    total = 0

    for i in range(len(vector_one)):
        total += vector_one[i] * vector_two[i]

    return total

    
class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #
    # Math methods not taught in this nano-degree (minors, adjoints, cofactors)
    # were learned from here: https://ltcconline.net/greenl/courses/203/MatricesApps/cofactors.htm
    #############################
    
    
    def getMinorMatrix(self, row_num, col_num):
        """
        Returns the minor matrix obtained by removing the row and column 
        associated with the desired entry
        """
        # Initialize
        minorMatrix = []
        row = []
        
        # Look over rows, skipping the specified row when we come to it
        for i in range(self.h):
            if i == row_num:
                continue
            
            # Look over columns, skipping the specified column when we come to it
            for j in range(self.w):
                if j == col_num:
                    continue
                
                # Store values not in the specified row or column
                row.append(self.g[i][j])
            
            # Build output matrix row by row             
            minorMatrix.append(row)
            row = []
            
        return Matrix(minorMatrix)
    
    
    def getCofactor(self, row_num, col_num):
        """
        Computes the cofactor for the specified entry.
        The cofactor is defined as the determinant of the minor matrix times 1 or -1
        """
        minor = self.getMinorMatrix(row_num, col_num)
        det = minor.determinant()
        sign = math.pow(-1, (row_num + 1) + (col_num + 1))
        
        cofactor = sign * det
        
        return cofactor
    
    
    def getCofactorMatrix(self):
        """
        Returns the cofactor matrix. A cofactor is defined as the determinant 
        of a minor matrix, or the determinant of a matrix produced by dropping 
        the row and column associated with a specific entry
        """
        # Initialize
        cofactorMatrix = []
        row = []
        
        # Loop over all entries so output will have same dimensions
        # as the input matrix
        for i in range(self.h):
            for j in range(self.w):
                
                # Add one cofactor to the current row
                cofactor_temp = self.getCofactor(i, j)
                
                row.append(cofactor_temp)
            
            # Build cofactor matrix row-by-row
            cofactorMatrix.append(row)
            row = []
        
        return Matrix(cofactorMatrix)
        
 
    def determinant(self):
        """
        Calculates the determinant of the matrix
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        
        # If the matrix is 1x1, then the determinant is just the single element
        if self.h == 1:
            det = self.g[0][0]
            
        # If the matrix is 2x2, then the determinant is given by ad-bc
        elif self.h == 2:
            a, b, c, d = self.g[0][0], self.g[0][1], self.g[1][0], self.g[1][1]
            det = a*d - b*c
        
        # For larger matrices, use a recursive algorithm
        else:
            # Initialize determinant to be built incrementally
            det = 0
            
            # Loop over the first row since any row will give the same determinant
            for j in range(self.w):
                
                # Incrementally add terms to the determinant
                cofactor_temp = self.getCofactor(0, j)
                
                # Add next term to the determinant running total
                det += self.g[0][j] * cofactor_temp
        
        return det
    

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        
        total = 0
        
        # Loop through each value in the matrix and only add those along the diagonal
        for i in range(self.h):
            for j in range(self.w):
                if i == j:
                    total += self.g[i][j]
        
        return total
    

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        # Check that our matrix is square and of size 1x1 or 2x2
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.determinant == 0:
            raise(ValueError, "Determinant of 0 means Matrix does not have an inverse.")

        # Compute the inverse matrix using the determinant function for a 1x1 or 2x2 matrix
        if self.h == 1:
            inverse = Matrix([[1 / self.determinant()]])
                       
        elif self.h == 2:
            # Compute inverse of 2x2 by using a shortcut method
            a, b, c, d = self.g[0][0], self.g[0][1], self.g[1][0], self.g[1][1]
                       
            det = 1 / self.determinant()
            inverse = Matrix([
                [d * det, -b * det],
                [-c * det, a * det]
            ])
            
        else:
            # Use general algorithm to compute inverse of matrices larger than 2x2.
            # Specifically, the inverse is defined as (1/determinant) * (transpose of cofactor matrix)
            # The transpose of the cofactor matrix is also known as the adjoint
                  
            cofactorMatrix = self.getCofactorMatrix()
            adjointMatrix = cofactorMatrix.T()
            inverse = (1 / self.determinant()) * adjointMatrix

        return inverse

    
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        matrix_transpose = []
        row = []
                       
        # Traverse the matrix by column first, then by row to construct the transpose row-by-row
        for j in range(self.w):
            for i in range(self.h):
                row.append(self.g[i][j])
            matrix_transpose.append(row)
            row = []
    
        return Matrix(matrix_transpose)

        
    def is_square(self):
        """
        Returns true is the matrix is a square matrix and false otherwise
        """
        return self.h == self.w

    
    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    
    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    
    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
            
        # Initialize matrix to hold the results
        matrixSum = []

        # Initialize list to hold a row for appending sums of each element
        row = []

        # Perform element-wise addition of two matrices
        for i in range(self.h):
            for j in range(self.w):

                summed_value = self.g[i][j] + other.g[i][j]
                row.append(summed_value)

            # Append row to matrixSum and reinitialize row as an empty list
            matrixSum.append(row)
            row = []

        return Matrix(matrixSum)
    

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        
        # Return the matrix scalar-multiplied by -1
        matrix_neg = self.__rmul__(-1)
        
        return matrix_neg
    

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        
        # Multiply the other matrix by -1
        other_neg = other.__neg__()
        
        # Perform subtraction by adding a negative
        matrixSum = self.__add__(other_neg)
        
        return matrixSum


    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        product = []
        row = []
        
        # Transpose the other matrix to simplify traversing the matrices
        matrixBT = other.T()

        # Iterate through the rows of the matrix and the rows of the tranpose of the other matrix
        for i in range(self.h):
            for j in range(matrixBT.h):

        # Calculate the dot product between each row of matrix A
        # with each row in the transpose of matrix B
                dp = dot_product(self.g[i], matrixBT.g[j])
                row.append(dp)
            
            # Append rows to the output product matrix and reset the row storage
            product.append(row)
            row = []

        return Matrix(product)
    

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        
        if isinstance(other, numbers.Number):
            
            # Initialize scalar multiplied matrix and list for appending rows
            rmul_matrix = []
            row = []
            
            # Multiply each value in the matrix by the scalar other and append to rmul_matrix
            for i in range(self.h):
                for j in range(self.w):
                    
                    rmul_value = self.g[i][j] * other
                    row.append(rmul_value)
                
                rmul_matrix.append(row)
                row = []
        
        return Matrix(rmul_matrix)
    
            