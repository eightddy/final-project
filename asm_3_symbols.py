import sys, re

def asm_symbols(asm_code):
    symbols = [0]*8
    dem = 0
    for row in asm_code:
        if '*' in row:
            symbols[0] += row.count("*")
        if '-' in row:
            symbols[1] += row.count("-")
        if '+' in row:
            symbols[2] += row.count("+")
        if '[' in row:
            symbols[3] += row.count("[")
        if ']' in row:
            symbols[4] += row.count("]")
        if '@' in row:
            symbols[5] += row.count("@")
        if '?' in row:
            symbols[6] += row.count("?")
        for i in range(len (row)):
            if (ord(row[i]) >= 128 and ord(row[i]) <= 255):
                symbols[7] += 1
    return symbols

file_path = "samples/01IsoiSMh5gxyDYTl4CB.asm"
#file_path = "samples/01SuzwMJEIXsK7A8dQbl.asm"
with open(file_path) as f:
    byte_code = f.readlines()

print asm_symbols(byte_code)