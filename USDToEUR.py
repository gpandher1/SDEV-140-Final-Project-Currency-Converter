# Program name: Forex
# Author: Gurlal Pandher
# Date: 5/16/2022
# Summary: GUI that converts USD to EUR, and EUR to USD
# Variables:
#   number: user-entered number for USD or EUR (float)
#   result: the number converted to the other measurement (float)

from breezypythongui import EasyFrame
import math

class USDToEURGUI (EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title = "USD to EUR Converter")

        # Label and field for the input
        self.addLabel (text = "USD/EUR",
                       row = 0,
                       column = 0)
        self.inputField = self.addFloatField(value = 0,
                                             row = 0,
                                             column = 1,
                                             width = 10)

        # Label and field for the output
        self.outputLabel = self.addLabel (text = "Conversion:",
                                          row = 1,
                                          column = 0)
        self.outputField = self.addFloatField(value = 0.0,
                                              row = 1,
                                              column = 1,
                                              width = 10,
                                              precision = 2,
                                              state = "readonly")

        # Buttons for the third row
        self.addButton(text = "USD to EUR",
                       row = 2,
                       column = 0,
                       command = self.computeUSDToEUR)

        self.addButton(text = "EUR to USD",
                       row = 2,
                       column = 1,
                       command = self.computeEURToUSD)

    # Function for converting USD to EUR
    def computeUSDToEUR (self):
        # Inputs the USD, computes and outputs EUR
        number = self.inputField.getNumber()
        result = 0.95 * number
        self.outputLabel["text"] = "Converted to EUR :"
        self.outputField.setNumber(result)

    # Function for converting EUR to USD
    def computeEURToUSD (self):
        # Inputs the EUR, computes and outputs USD
        number = self.inputField.getNumber()
        result = 1.05 * number
        self.outputLabel["text"] = "Converted to USD :"
        self.outputField.setNumber(result)

def main():
    # Instantiate and pop up the window
    USDToEURGUI().mainloop()

main()
    
                                
