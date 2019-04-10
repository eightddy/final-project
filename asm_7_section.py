import sys, os
import numpy as np

def asm_sections(asm_code):
    section_names = []
    dem = 0
    for row in asm_code:
        if row.find(':') != -1:
            k = row.index(':')
            section_name = [row[0:k]]
        print section_name
        dem += 1
        print dem
        if section_name != 'HEADER':
            section_names += section_name
    #sys.exit()
    known_sections = ['.text', '.data', '.bss', '.rdata', '.edata', '.idata', '.rsrc', '.tls', '.reloc']
    sections_values = [0]*24
    unknown_sections = []
    unknown_lines = 0
    number_of_sections = len(section_names)

    for section in section_names:

        if section in known_sections:
            section_index = known_sections.index(section)
            sections_values[section_index] += 1
        else:
            unknown_sections.append(section)
            unknown_lines += 1

    uni_section_names_len = len(np.unique(section_names))
    uni_unknown_section_names_len = len(np.unique(unknown_sections))
    uni_known_section_names_len = 0
    for i in range(0,8):
        if sections_values[i] != 0:
            uni_known_section_names_len += 1

    sections_values[9] = uni_section_names_len
    sections_values[10] = uni_unknown_section_names_len
    sections_values[11] = unknown_lines

    for i in range(0,8):
        sections_values[i + 12] = float(sections_values[i])/ number_of_sections

    sections_values[21] = float(uni_known_section_names_len) / uni_section_names_len
    sections_values[22] = float(uni_unknown_section_names_len) / uni_section_names_len
    sections_values[23] = float(unknown_lines) / number_of_sections

    print sections_values
    #return sections_values, section_names

#file_path = "samples/01IsoiSMh5gxyDYTl4CB.asm"
#file_path = "samples/1x2u5Ws7tzFRAgyqoJBV.asm"
#file_path = "samples/CTv0Q8ujqlZc5dGnfeaw.asm"
file_path = "samples/dLVM6kPA8ru3EeKlqRZB.asm"
#file_path = "samples/01SuzwMJEIXsK7A8dQbl.asm"
#jIzgiMTcuZPt4eJNr2Yw.asm.gz

with open(file_path) as f:
    byte_code = f.readlines()

print asm_sections(byte_code)