#!/usr/bin/env python

########## Test ##########
from DecimalRomanConverter import DRConverter

# Test decimal to roman
ans = DRConverter.convertToRoman(1)
assert ans == "I", "Failed"
print(ans)
ans = DRConverter.convertToRoman(4000)
assert ans == "MMMM", "Failed"
print(ans)

# Test roman to decimal
ans = DRConverter.convertToDecimal("I")
assert ans == 1, "Failed"
print(ans)
ans = DRConverter.convertToDecimal("MMMM")
assert ans == 4000, "Failed"
print(ans)
