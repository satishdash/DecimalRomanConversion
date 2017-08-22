#!/usr/bin/env python

##############################################################################################
# A definition to convert decimal number to roman numeral and vice-versa
#
# @author : Satish Dash
# 
###############################################################################################

class DRConverter(object):
	'''Exposes API's to convert decimal number to\
	Roman numeral and vice-versa
	'''
	# roman to decimal association
	values = [ ("M", 1000), ("CM", 900),\
			   ("D", 500), ("CD", 400),\
			   ("C", 100), ("XC", 90),\
			   ("L", 50), ("XL", 40),\
			   ("X", 10), ("IX", 9),\
			   ("V", 5), ("IV", 4),\
			   ("I", 1)\
	]

	# roman-decimal mapping
	roman_dict = {k:v for k,v in values}

	@staticmethod
	def convertToRoman(number):
		''' Converts decimal to roman numeral
			int -> str
			@param number Number to be converted to roman context
		'''
		roman = ""
		i = 0
		n = number
		if 0 < n <= 4000:			
			while n > 0:
				for _ in range(n // DRConverter.values[i][1]):
					roman += DRConverter.values[i][0]
					n -= DRConverter.values[i][1]
				i += 1
			return roman
		return "Invalid input: number must be in the range from (0, 4000]."


	@staticmethod
	def convertToDecimal(roman_str):
		''' Converts roman numeral to decimal number
			str -> int
			@param roman Roman numeral string to be converted to decimal context
						 range is [I, MMMM]
		'''
		length = len(roman_str)
		n = 0
		if isinstance(roman_str, str):
			roman = roman_str.upper()		
			for i in range(length):
				if i > 0 and DRConverter.roman_dict[roman[i]] > DRConverter.roman_dict[roman[i-1]]:
					n += DRConverter.roman_dict[roman[i]] - (2 * DRConverter.roman_dict[roman[i-1]])
				else:
					n += DRConverter.roman_dict[roman[i]]
			return n
		return "Invalid input: Roman numeral must be string in range [I, MMMM]."
