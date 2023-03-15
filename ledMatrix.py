import machine
import neopixel
import time
from constants import ASCII_WIDTH, ASCII_HEIGHT
from constants import TOTAL_MATRIX_ROWS, TOTAL_MATRIX_COLS, TOTAL_MATRIX_LEDS
from constants import PIN

from asciiBinary import ASCII_MAP

from utils import positionToNumber


class LedMatrix:
    def __init__(self):
        self.totalRows = TOTAL_MATRIX_ROWS
        self.totalCols = TOTAL_MATRIX_COLS
        self.totalLeds = TOTAL_MATRIX_LEDS
        self.leds = neopixel.NeoPixel(machine.Pin(PIN), self.totalLeds)

    def clear(self):
        for i in range(self.totalRows * self.totalCols):
            self.leds[i] = (0, 0, 0)
        self.leds.write()

    def rollToLeftV2(self, inputStr: str, interval: int, rgbTuple: tuple, verticalShift: int = 0):
        if len(inputStr) <= 0:
            return
        
        
        # binaryImage is a 2D array
        binaryImage = self.buildBinaryArray(inputStr)
        
        imageWidth = len(binaryImage[0])
        
        colsToShiftLeft = self.totalCols + imageWidth
        
        
        for step in range(colsToShiftLeft):
            
            for r in range(len(binaryImage)):
                for c in range(len(binaryImage[0])):
                    newRow = r + verticalShift
                    newCol = c +  self.totalCols - step
                    
                    if newRow < 0 or newRow >= self.totalRows or newCol < 0 or newCol >= self.totalCols:
                        continue
                    
                    ledNum = positionToNumber(newRow, newCol)
            
            
                    if binaryImage[r][c] == 0:
                        self.leds[ledNum] = rgbTuple
                        
            self.leds.write()
            time.sleep(interval)
            self.clear()
        




    def convertStrsToBinaryChars(self, inputStr: str) -> list[list[list[int]]]:
        res = []
        lowerStr = inputStr.lower()
        for c in lowerStr:
            if c in ASCII_MAP:
                res.append(ASCII_MAP[c])

        return res
    
    
    
    def concatenateBinaryArray(self,  binaryChars : list[list[list[int]]], rows : int =  6) -> list[list[int]]:
        res = []
        for r in range(rows):
            tempList = []
            for b in binaryChars:
                tempList += b[r]

            res.append(tempList)

        return res
    
    def buildBinaryArray(self, inStr:str) -> list[list[int]]:
        binaryChars = self.convertStrsToBinaryChars(inStr)
        
        result  = self.concatenateBinaryArray(binaryChars)
        
        return result;
            
            
        
