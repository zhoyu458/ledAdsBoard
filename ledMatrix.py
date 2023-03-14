import machine
import neopixel
import time
from constants import ASCII_WIDTH, ASCII_HEIGHT
from constants import TOTAL_MATRIX_ROWS, TOTAL_MATRIX_COLS, TOTAL_MATRIX_LEDS
from constants import SINGLE_MATRIX_ROWS, SINGLE_MATRIX_COLS, SINGLE_MATRIX_LEDS
from constants import PIN

from asciiBinary import ASCII_MAP

from utils import positionToNumber
class LedMatrix:
    def __init__(self):
        self.totalRows = TOTAL_MATRIX_ROWS
        self.totalCols = TOTAL_MATRIX_COLS
        self.totalLeds = TOTAL_MATRIX_LEDS
        self.leds = neopixel.NeoPixel(machine.Pin(PIN),  self.totalLeds)
        
        
#     def showAscii(self, binaryArray : list[list], rgbTuple : tuple):
#         rows = len(binaryArray)
#         cols = len(binaryArray[0])
#         for r in range(rows):
#             for c in range(cols):
#                 if binaryArray[r][c] == 0:
#                     num = positionToNumber(r, c)
#                     # if the led number is out of range, do not write to the matrix
#                     if num >= 0 and num < self.totalLeds:
#                         self.leds[num] = rgbTuple
#                         self.leds.write()
    
    def clear(self):
        for i in range(self.totalRows * self.totalCols):
            self.leds[i] = (0,0,0)
        self.leds.write();
        
    
#     def rollToRight(self, binaryChar : list[list[int]],  interval: int, rgbTuple : tuple, verticalShift : int = 0):
# 
#         # rolling image to right 
#         for step in range (self.totalRows):
#             for r in range (ASCII_HEIGHT):
#                 for c in range (ASCII_WIDTH):
#                     
#                     newRow = r + verticalShift
#                     newCol = c + step
#                     
#                     
#                     num = positionToNumber(newRow, newCol)
#                     
#                     # if the coorindation is out of the matrix, continue 
#                     if newRow < 0 or newRow >= self.totalRows or newCol < 0 or newCol >= self.totalCols:
#                         continue
#                     
#                     if binaryChar[r][c] == 0:
#                         self.leds[num] = rgbTuple
#                            
#             self.leds.write()
#             time.sleep(interval)
#             self.clear()
        
        
        
            
#     def rollToLeft(self, binaryChar : list[list[int]],  interval: int, rgbTuple : tuple, verticalShift : int = 0):
# 
#         # rolling image to right 
#         for step in range (self.totalRows - 1, -1, -1):
#             for r in range (ASCII_HEIGHT):
#                 for c in range (ASCII_WIDTH):
#                     
#                     newRow = r + verticalShift
#                     newCol = c + step
#                     
#                     
#                     num = positionToNumber(newRow, newCol)
#                     
#                     # if the coorindation is out of the matrix, continue 
#                     if newRow < 0 or newRow >= self.totalRows or newCol < 0 or newCol >= self.totalCols:
#                         continue
#                     
#                     if binaryChar[r][c] == 0:
#                         self.leds[num] = rgbTuple
#                            
#             self.leds.write()
#             time.sleep(interval)
#             self.clear()
            
            
    def rollToLeftV2(self, inputStr : str,  interval: int, rgbTuple : tuple, verticalShift : int = 0):
        if len(inputStr) <= 0:
            return
        
        Arrays = self.build2DArray(inputStr)
        
        ##############################
        

        
        
        
        #############################
        
        totalStep = self.totalCols  + len(Arrays) * len(Arrays[0])
        
        for step in range (totalStep):
            for index in range(len(Arrays)):
                binaryChar = Arrays[index]
                
                for r in range (ASCII_HEIGHT):
                    for c in range (ASCII_WIDTH):
                        
                        if binaryChar[r][c] == 1:
                            continue
                        
                        newRow = r + verticalShift
                        colOffset = self.totalCols + (ASCII_WIDTH * index)
                        newCol = c + colOffset - step
                        
                        num = positionToNumber(newRow, newCol)
                        
                        if newRow < 0 or newRow >= self.totalRows or newCol < 0 or newCol >= self.totalCols:
                            continue
                        
                        if binaryChar[r][c] == 0:
                            self.leds[num] = rgbTuple
                            
            self.leds.write()
#             time.sleep(interval)
            self.clear()
                
            
            

            
            
            
    def build2DArray(self, inputStr:str) -> list[list[list[int]]]:
        res = []
        lowerStr = inputStr.lower()
        for c in lowerStr:
            if c in ASCII_MAP:
                res.append(ASCII_MAP[c])
                
        return res
            
            
        

  
        
        
