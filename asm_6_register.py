import sys, os, re


def asm_registers(asm_code):
    registers = ['edx','esi','es','fs','ds','ss','gs','cs','ah','al',
                 'ax','bh','bl','bx','ch','cl','cx','dh','dl','dx',
                 'eax','ebp','ebx','ecx','edi','esp']
    registers_values = [0]*len(registers)
    for row in asm_code:
        row = row.lower()
        for register in registers:
            if register in row:
                registers_values[registers.index(register)] += sum(1 for match in re.finditer(r"\b"+register+r"\b", row))
    return registers_values

file_path = "samples/01IsoiSMh5gxyDYTl4CB.asm"
#file_path = "samples/01SuzwMJEIXsK7A8dQbl.asm"
with open(file_path) as f:
    byte_code = f.readlines()

print asm_registers(byte_code)