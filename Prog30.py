# Bit Manipulation operators: & (AND), | (OR), ~ (COMPLEMENT), ^ (XOR), << (LEFT SHIFT), >> (RIGHT SHIFT)
data1 = 100  # 100 = 64 + 32 + 4 = 0110 0100
data2 = 50   # 50 = 32 + 16 + 2  = 0011 0010
result = data1 & data2  # 0110 0100
#                       & 0011 0010
#                         ---------
#                         0010 0000 => 32
print(f"So {data1} & {data2} = {result}")