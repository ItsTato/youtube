
# ✅ Adding
# ✅ Substraction

# Live streamed on YouTube by ItsTato.

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
