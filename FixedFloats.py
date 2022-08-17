
# Live streamed on YouTube by ItsTato.

"""
MIT License

Copyright (c) 2022 ItsTato

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

class FixedFloats():
	def __init__(self) -> None:
		return
	
	def add(num1,num2):

		num1Decimals = 0
		num2Decimals = 0
		outputDecimals = 0 # 3.14 + 3.1415    4 decimals     == 6 . 2815
		output = 0
		outputDecimalsVal = 0

		try:
			num1Decimals = len(str(num1).split(".")[1]) # 3.14: 3 | 14, num1Decimals: 2
		except:
			pass

		try:
			num2Decimals = len(str(num2).split(".")[1])
		except:
			pass

		if num1Decimals > num2Decimals:
			outputDecimals = num1Decimals
		elif num1Decimals < num2Decimals:
			outputDecimals = num2Decimals
		elif num1Decimals == num2Decimals:
			outputDecimals = num1Decimals

		output = float(num1)+float(num2)

		try:
			outputDecimalsVal = int(str(output).split(".")[1])
		except:
			pass

		if outputDecimalsVal == 0:
			return int(round(float(num1)+float(num2)))
		else:
			return round(float(num1)+float(num2), outputDecimals) # round( num , maxAmountOfDecimals )
	
	def substract(num1, num2):

		num1Decimals = 0
		num2Decimals = 0
		outputDecimals = 0  # 3.14 + 3.1415    4 decimals     == 6 . 2815
		output = 0
		outputDecimalsVal = 0

		try:
			num1Decimals = len(str(num1).split(".")[1])  # 3.14: 3 | 14, num1Decimals: 2
		except:
			pass

		try:
			num2Decimals = len(str(num2).split(".")[1])
		except:
			pass

		if num1Decimals > num2Decimals:
			outputDecimals = num1Decimals
		elif num1Decimals < num2Decimals:
			outputDecimals = num2Decimals
		elif num1Decimals == num2Decimals:
			outputDecimals = num1Decimals

		output = float(num1)-float(num2)

		try:
			outputDecimalsVal = int(str(output).split(".")[1])
		except:
			pass

		if outputDecimalsVal == 0:
			return int(round(float(num1)-float(num2)))
		else:
			# round( num , maxAmountOfDecimals )
			return round(float(num1)-float(num2), outputDecimals)

if __name__ == "__main__":
	import sys
	sys.exit(0)
