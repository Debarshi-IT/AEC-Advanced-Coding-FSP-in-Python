def caseConversion(ch):
    return chr(ord(ch) ^ 0x20)
mychr = 'a'
print(mychr, caseConversion(mychr))
mychr = 'A'
print(mychr, caseConversion(mychr))