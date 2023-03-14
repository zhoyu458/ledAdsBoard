

from constants import TOTAL_MATRIX_ROWS
from constants import TOTAL_MATRIX_COLS
from constants import TOTAL_MATRIX_LEDS

from constants import SINGLE_MATRIX_ROWS
from constants import SINGLE_MATRIX_COLS
from constants import SINGLE_MATRIX_LEDS

# The function convert a coordinatio to led number on the matrix
# The coordination system start at the top left coner with [0, 0]
def positionToNumber(rowIndex : int,  colIndex: int) -> int:
    
    matrixBlockOffset = colIndex // SINGLE_MATRIX_COLS
    rowIndex = rowIndex % SINGLE_MATRIX_ROWS
    colIndex = colIndex % SINGLE_MATRIX_COLS
    

    
    ledNum = 0
    
    if(rowIndex % 2 == 0):
        ledNum = (SINGLE_MATRIX_ROWS - rowIndex - 1) * SINGLE_MATRIX_ROWS + (SINGLE_MATRIX_COLS - colIndex - 1)
        ledNum += matrixBlockOffset * SINGLE_MATRIX_LEDS
    else:
        
        ledNum = (SINGLE_MATRIX_ROWS - rowIndex - 1) * SINGLE_MATRIX_ROWS + colIndex
        ledNum += matrixBlockOffset * SINGLE_MATRIX_LEDS
        

        
    
    
    return ledNum 
        
    
    

    
    # the variable is for multiple matrix connect together
#     matrixBlockNumber = col // SINGLE_MATRIX_COLS
#     
#     newRowNum = row % SINGLE_MATRIX_ROWS
#     newColNum = col % SINGLE_MATRIX_COLS
#     
#     
#     newRowNum = SINGLE_MATRIX_ROWS - row - 1
# 
#     if newRowNum % 2 == 0:
#         newColNum = col 
#     else:
#         newColNum = SINGLE_MATRIX_COLS - col - 1
#         
#         
#     return (SINGLE_MATRIX_ROWS * newRowNum) + newColNum 
    
    





    
    
    







        
        
    
        